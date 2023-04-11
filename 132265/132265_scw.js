function solution(topping) {
    var answer = 0;

    let A = Array(10001).fill(0)
    let B = Array(10001).fill(0)
    let A_size = 0
    let B_size = 0

    topping.forEach((element, i) => {
        B[element]++
    });

    B_size = B.filter(element => element !==0).length
    
    topping.forEach((element) => {
        if(A[element] === 0) A_size++;
        A[element]++;
        B[element]--;

        if(B[element] === 0) B_size--;
        if(A_size===B_size) answer++;
    })
    
    return answer;
}

console.log(solution([1, 2, 1, 3, 1, 4, 1, 2]))


// function solution(topping) {
//     var answer = 0;
//     for(let i=0;i<topping.length;i++){
//         a = new Set(topping.slice(0,i))
//         b = new Set(topping.slice(i,topping.length))

//         if(a.size === b.size){
//             answer++;
//         }
//     }
//     return answer;
// }