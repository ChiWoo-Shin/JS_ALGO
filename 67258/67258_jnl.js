/* Map 1차
function solution(gems) {
    const N = new Set(gems).size;
    const gemMap = new Map();
    const answer = [1, gems.length];
    for (let i = 0; i < gems.length; i += 1) {
        const gem = gems[i];
        gemMap.delete(gem);
        gemMap.set(gem, i);
        if (gemMap.size === N) {
            const cand = [gemMap.values().next().value + 1, i + 1];
            if (answer[1] - answer[0] > cand[1] - cand[0]) [answer[0], answer[1]] = [cand[0], cand[1]];
        }
    }
    return answer;
}*/

/* Map 2차 */
function solution(gems) {
    const N = new Set(gems).size;
    let start = 0;
    let end = 0;
    const gemMap = new Map(); // (보석 이름, 보석 빈도수)
    gemMap.set(gems[0], 1);
    const answer = [1, gems.length];
    while (end < gems.length) {
        if (gemMap.size === N) {
            if (answer[1] - answer[0] > end - start) {
                [answer[0], answer[1]] = [start + 1, end + 1];
            }

            gemMap.set(gems[start], gemMap.get(gems[start]) - 1);
            if (gemMap.get(gems[start]) === 0) gemMap.delete(gems[start]);
            // start를 오른쪽으로 이동
            start += 1;
        } else {
            end += 1;
            const eIdx = gemMap.get(gems[end]);
            gemMap.set(gems[end], eIdx ? eIdx + 1 : 1);
        }
    }
    return answer;
}
