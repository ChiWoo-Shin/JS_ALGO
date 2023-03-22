function dfs(map, me, total) {
    if (me === "-") return;
    const mine = total - ((total * 0.1) >> 0);
    map[me][1] += mine;
    if (total - mine > 0) dfs(map, map[me][0], total - mine);
}

function solution(enroll, referral, seller, amount) {
    const map = {};
    for (let i = 0; i < enroll.length; i += 1) {
        map[enroll[i]] = [referral[i], 0];
        // key: 본인, value: 자신의 부모
    }
    for (let i = 0; i < seller.length; i += 1) {
        const name = seller[i];
        const money = amount[i] * 100;
        dfs(map, name, money);
    }
    const result = [];
    for (const key of Object.keys(map)) {
        result.push(map[key][1]);
    }
    return result;
}
