const set = new Set();

function dfs(arr, visited, cur, limit, tmp) {
    if (cur === limit) {
        set.add(tmp.sort().toString());
        return;
    }
    for (let i = 0; i < arr[cur].length; i += 1) {
        if (!visited[arr[cur][i]]) {
            visited[arr[cur][i]] = 1;
            dfs(arr, visited, cur + 1, limit, tmp.concat([arr[cur][i]]));
            visited[arr[cur][i]] = 0;
        }
    }
}

function solution(user_id, banned_id) {
    const arr = [];
    for (let i = 0; i < banned_id.length; i += 1) {
        const bId = banned_id[i];
        const tmp = [];
        for (let j = 0; j < user_id.length; j += 1) {
            const uId = user_id[j];
            let flag = true;
            if (bId.length !== uId.length) continue;
            for (let k = 0; k < bId.length; k += 1) {
                if (bId[k] !== uId[k] && bId[k] !== "*") {
                    flag = false;
                    break;
                }
            }
            if (flag) tmp.push(j);
        }
        arr.push(tmp);
    }
    const visited = new Array(user_id.length).fill(0);
    dfs(arr, visited, 0, banned_id.length, []);
    return set.size;
}
