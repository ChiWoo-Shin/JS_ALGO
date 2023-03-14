function makePermutation(arr) {
    const N = arr.length;
    const result = [];
    function dfs(tmp, visited) {
        if (tmp.length === N) return result.push(tmp);
        for (let i = 0; i < N; i += 1) {
            if (!visited[i]) {
                visited[i] = 1;
                dfs(tmp.concat([arr[i]]), visited);
                visited[i] = 0;
            }
        }
    }

    for (let i = 0; i < N; i += 1) {
        const visited = new Array(N).fill(0);
        visited[i] = 1;
        dfs([arr[i]], visited);
    }
    return result;
}

function getResult(priority, arr) {
    while (priority.length > 0) {
        const op = priority.pop();
        let idx = arr.findIndex(elem => elem === op);
        let tmp = 0;
        while (idx >= 0) {
            if (op === "+") tmp = arr[idx - 1] + arr[idx + 1];
            else if (op === "-") tmp = arr[idx - 1] - arr[idx + 1];
            else tmp = arr[idx - 1] * arr[idx + 1];

            arr.splice(idx - 1, 3, tmp);
            idx = arr.findIndex(elem => elem === op);
        }
    }
    return Math.abs(arr[0]);
}

function solution(expression) {
    const set = new Set();
    const arr = [];
    let num = "";
    for (let i = 0; i < expression.length; i += 1) {
        if (isNaN(expression[i])) {
            arr.push(parseInt(num));
            arr.push(expression[i]);
            set.add(expression[i]);
            num = "";
        } else num += expression[i];
    }
    arr.push(parseInt(num));

    const permutations = makePermutation(Array.from(set));

    let answer = -1;
    for (let i = 0; i < permutations.length; i += 1) {
        const copy = [...arr];
        const tmp = getResult(permutations[i], copy);
        if (tmp > answer) answer = tmp;
    }
    return answer;
}
