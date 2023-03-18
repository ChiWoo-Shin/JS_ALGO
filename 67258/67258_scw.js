function solution(gems){
    const answer =[0, 0];
    const gem_cnt =new Set(gems).size;
    let [s, e] = [0,0];
    const gem_list = new Map();
    gem_list.set(gems[0],1);
    answer[0] = 1;
    answer[1] = gems.length;
    while(e<gems.length){
        console.log(s, e, gem_list)
        if(gem_list.size === gem_cnt){
            if((answer[1]-answer[0]) > e -s){
                answer[1] = e+1;
                answer[0] = s+1;
            }

            gem_list.set(gems[s], gem_list.get(gems[s]) -1);
            if(gem_list.get(gems[s]) === 0) gem_list.delete(gems[s]);

            s++;

        } else {
            e++;
            const endIdx = gem_list.get(gems[e]);
            gem_list.set(gems[e], endIdx ? endIdx+1 : 1);
        }
    }

    return answer;
}

console.log(solution(["DIA", "EM", "EM", "RUB", "DIA"]))

// 효율성 X

// function solution(gems) {
//     const answer = [0,0];
//     const dic =new Set();
//     for(let i =0;i<gems.length; i++){
//         dic.add(gems[i])
//     }

//     const dic_len = dic.size;
    
//     for(let i=0; i<=gems.length-dic_len; i++){
//         const result = new Set();
//         for(let j=i; j<gems.length; j++){
//             result.add(gems[j]);
//             if(result.size === dic_len){
//                 if(answer[0] === 0 && answer[1] ===0){
//                     answer[0] = i+1;
//                     answer[1] = j+1;
//                 } else if((answer[1] - answer[0])>j-i){
//                     answer[0] = i+1;
//                     answer[1] = j+1;
//                 }
//             }
//         }
//     }
//     return answer;
// }