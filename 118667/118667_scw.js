function solution(queue1, queue2) {
    var answer = 0;
    let pur =0;
    let max_cnt = queue1.length *3
    pur = (queue1.reduce((acc, cur)=>acc+cur) - queue2.reduce((acc, cur) => acc+cur))/2 >>0;
    
    let [idx1,idx2] = [0,0];

    while (pur !==0 && answer< max_cnt){
        if(pur > 0){
            const val_1 = queue1[idx1];
            idx1++, (pur -=val_1), queue2.push(val_1);
        } else {
            const val_2 = queue2[idx2];
            idx2++, (pur +=val_2), queue1.push(val_2);
        }
        answer++;
    }
    
    return pur !==0 ? -1: answer;
}

console.log(solution([3, 2, 7, 2], [4, 6, 5, 1]))