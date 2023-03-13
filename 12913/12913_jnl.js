function solution(land) {
    const N = land.length;
    for (let row = 1; row < N; row += 1) {
        for (let col1 = 0; col1 < 4; col1 += 1) {
            let maxValue = 0;
            for (let col2 = 0; col2 < 4; col2 += 1) {
                if (col2 !== col1) {
                    if (maxValue < land[row - 1][col2]) maxValue = land[row - 1][col2];
                }
            }
            land[row][col1] += maxValue;
        }
    }
    return Math.max(...land[N - 1]);
}
