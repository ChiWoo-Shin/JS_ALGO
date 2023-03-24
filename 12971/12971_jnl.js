function solution(sticker) {
    const N = sticker.length;
    if (N === 1) return sticker[0];

    const dp1 = new Array(N).fill(0); // 첫 번째 스티커를 뗀 경우
    const dp2 = new Array(N).fill(0); // 첫 번째 스티커를 떼지 않은 경우

    dp1[0] = sticker[0];
    dp1[1] = sticker[0];
    dp2[1] = sticker[1];

    for (let i = 2; i < N - 1; i += 1) {
        dp1[i] = Math.max(dp1[i - 2] + sticker[i], dp1[i - 1]);
    }

    for (let i = 2; i < N; i += 1) {
        dp2[i] = Math.max(dp2[i - 2] + sticker[i], dp2[i - 1]);
    }
    console.log(dp1, dp2);
    return Math.max(dp1[N - 2], dp2[N - 1]);
}
