function solution(n, t, m, p) {
    var answer = '';
    let i=0;
    let order =1;
    check_: while(true){
        let temp = i.toString(n).toUpperCase();
        for(let i=0;i<temp.length;i++){
            if(order === p){
                answer+=temp[i];
                if(answer.length === t){
                    break check_;
                }
            }

            order++;

            if(order>m){
                order -=m;
            }
        }
        
        i++;
    }

    return answer;
}

console.log(solution(2, 4, 2, 1))

