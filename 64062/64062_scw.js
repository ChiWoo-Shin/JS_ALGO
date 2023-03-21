function checkStone(stones, mid, k){
    let cnt =0;
    
    for(let i =0; i<stones.length;i++){
        if (cnt === k) break;
        if(stones[i]<= mid){
            cnt++;
        }
        else cnt=0;
    }

    if(cnt === k){
        return false;
    } else {
        return true;
    }
}

function solution(stones, k) {
    let left = 1;
    let right = 200000000;

    while(left<= right){
        let mid = ((left + right)/2) >> 0; // 왜 왜왜왜왜오애ㅗ
        
        if(checkStone(stones, mid, k)){
            left = mid+1;
        } else {
            right = mid-1;
        }
    }

    return left;
}

console.log(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

// 효율성 X
// function solution(stones, k) {
//     var answer = Number.MAX_SAFE_INTEGER;
//     for(let i=0; i<=stones.length - k; i++){
//         Math.max(...stones.slice(i, i+k)) < answer ? answer = Math.max(...stones.slice(i, i+k)) : answer
//     }
//     return answer;
// }