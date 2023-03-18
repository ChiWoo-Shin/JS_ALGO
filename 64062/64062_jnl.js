function BinarySearch(stones, k, min, max) {
    if (min === max) return min;
    const mid = ((min + max) / 2) >> 0;
    let cnt = 0;
    for (let i = 0; i < stones.length; i += 1) {
        if (cnt === k) break;
        if (stones[i] - mid <= 0) cnt += 1;
        else cnt = 0;
    }
    if (cnt === k) {
        return BinarySearch(stones, k, min, mid);
    } else {
        return BinarySearch(stones, k, mid + 1, max);
    }
}

function solution(stones, k) {
    return BinarySearch(stones, k, 1, 200000000);
}
