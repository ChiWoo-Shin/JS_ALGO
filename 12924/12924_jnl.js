function solution(n) {
    let answer = 0;
    for (let i = 1; i <= n; i += 1) {
        if (i % 2) {
            const mok = n / i;
            const rest = n % i;
            if (rest === 0 && mok - Math.floor(i / 2) > 0) answer += 1;
        } else {
            const t = n - i / 2;
            const mok = t / i;
            const rest = t % i;
            if (rest === 0 && mok - (i - 1) / 2 > 0) answer += 1;
        }
    }
    return answer;
}
