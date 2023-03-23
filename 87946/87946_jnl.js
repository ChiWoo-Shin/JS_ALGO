let answer = 0;
function dfs(visited, N, cur, temp, k, dungeons) {
    if (cur === N) return (answer = Math.max(answer, temp));
    for (let i = 0; i < N; i += 1) {
        if (!visited[i]) {
            visited[i] = 1;
            if (k >= dungeons[i][0]) {
                dfs(visited, N, cur + 1, temp + 1, k - dungeons[i][1], dungeons);
            } else {
                dfs(visited, N, cur + 1, temp, k, dungeons);
            }
            visited[i] = 0;
        }
    }
}

function solution(k, dungeons) {
    const N = dungeons.length;
    for (let i = 0; i < N; i += 1) {
        const visited = new Array(N).fill(0);
        dfs(visited, N, 0, 0, k, dungeons);
    }
    return answer;
}
