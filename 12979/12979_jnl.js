function solution(n, stations, w) {
    let answer = 0;
    let station = stations.shift();
    let idx = 1;
    while (idx <= n) {
        if (idx < station - w) {
            answer += Math.ceil((station - w - idx) / (2 * w + 1));
            idx = station + w + 1;
        } else {
            idx = station + w + 1;
        }
        if (stations.length <= 0) break;
        else station = stations.shift();
    }

    if (idx <= n) {
        answer += Math.ceil((n - idx + 1) / (2 * w + 1));
    }
    return answer;
}
