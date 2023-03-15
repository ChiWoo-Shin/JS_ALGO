function permutation(arr, selectNum) {
    let result = [];
    if (selectNum === 1) return arr.map((v) => [v]);
  
    arr.forEach((v, idx, arr) => {
      const fixer = v;
      const restArr = arr.filter((_, index) => index !== idx);
      const permuationArr = permutation(restArr, selectNum - 1);
      const combineFixer = permuationArr.map((v) => [fixer, ...v]);
      result.push(...combineFixer);
    });
    return result;
}

function check_id(user, banner) {
    user = user.sort((a,b) => a.length - b.length);
    banner = banner.sort((a,b) => a.length - b.length);
    
    for(let i=0; i<user.length; i++){
        if(user[i].length !== banner[i].length){
            return false;
        }
        for(let j=0;j<banner.length;j++){
            if(user[i][j] !== banner[i][j] && banner[i][j] !=='*'){
                return false;
            }
        }
    }

    return true;
}

function solution(user_id, banned_id) {
    const permUser = permutation(user_id, banned_id.length);
    const value = permUser.filter(v => check_id(v, banned_id))
    const answer = [...new Set(value.map(v=> v.sort().join('')))];
    return answer.length;
}



console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))

// dic로 했을때 중복처리를 할 수 없음
// function solution(user_id, banned_id) {
//     var answer = 1;

//     for(let i=0; i<banned_id.length; i++){
//         let cnt =0;
//         for(let j=0; j<user_id.length; j++){
//             if(banned_id[i].length === user_id[j].length){
//                 let len_cnt = 0;
//                 for(let k=0; k<banned_id[i].length; k++){
//                     if(banned_id[i][k]==='*'){
//                         len_cnt++;
//                     } else if(banned_id[i][k] !== user_id[j][k]){
//                         break
//                     } else {
//                         len_cnt++;
//                     }
                    
//                     if(len_cnt === banned_id[i].length){
//                         cnt++;
//                     }
//                 }
//             }
//         }

//         answer *=cnt;
//     }

//     return answer;
// }