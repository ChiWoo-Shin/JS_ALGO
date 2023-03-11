function solution(land) {
    
    for(let i=1; i<land.length;i++){
        land[i][0] += Math.max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += Math.max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += Math.max(land[i-1][1], land[i-1][0], land[i-1][3])
        land[i][3] += Math.max(land[i-1][1], land[i-1][2], land[i-1][0])
    }
    
    return Math.max(...land[land.length-1]);
}

console.log(solution([[0, 1, 2, 10], [1, 2, 3, 100]]))

// 틀린코드 - 예제만 통과 나머진 전부 X
// function solution(land) {
//     var answer = 0;
//     let prev =-1;
//     for(let i =0;i <land.length;i++){
//         let cur_idx = land[i].findIndex(x => x === Math.max(...land[i]));
//         if(prev === -1){
//             prev = cur_idx;
//             answer += land[i][cur_idx];
//         } else {
//             if (cur_idx === prev){
//                 land[i].splice(cur_idx, 1)
//                 answer += Math.max(...land[i])
//             } else {
//                 answer += land[i][cur_idx];
//             }
//         }
//     }

//     return answer;
// }