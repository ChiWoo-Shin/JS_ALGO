function solution(sequence, k) {
    let answer = [0, 1000000];
    let [left_idx, right_idx] = [0,0];
    let sum = sequence[0]

    while(right_idx<sequence.length) {
        if(sum === k){
            if(answer[1]-answer[0] > right_idx - left_idx){
                answer[1] = right_idx;
                answer[0] = left_idx;
            }
            sum -=sequence[left_idx++]
            sum +=sequence[++right_idx]
        } else if(sum >k){
            sum -=sequence[left_idx++];
        } else if(sum <k){
            sum +=sequence[++right_idx];
        }
        
    }
    return answer;
}

console.log(solution([1, 1, 1, 2, 3, 4, 5], 5))