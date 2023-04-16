function solution(n, k) {
    const answer =[];
    const arr = Array.from({length: n}, (_, i)=> i+1);

    function getNum(arr) {
        let factorial = 1
        for(let i=1;i<arr.length;i++){
            factorial *=i
        }
    
        const idx = Math.ceil(k/factorial) -1;
    
        k = k-idx*factorial;
    
        return arr[idx]
    }


    for(let i =1;i<n+1;i++){
        const num = getNum(arr);
        arr.splice(arr.indexOf(num),1);
        answer.push(num);
    }
    

    return answer;
}

console.log(solution(3, 5))

// permutaion 효율성 실패 + 런타임에러
// const getPermutations = function (arr, selectNumber) {
//     const results = [];
//     if (selectNumber === 1) return arr.map((el) => [el]); 
//     // n개중에서 1개 선택할 때(nP1), 바로 모든 배열의 원소 return. 1개선택이므로 순서가 의미없음.
//     arr.forEach((fixed, index, origin) => {
//       const rest = [...origin.slice(0, index), ...origin.slice(index+1)] 
//       // 해당하는 fixed를 제외한 나머지 배열 
//       const permutations = getPermutations(rest, selectNumber - 1); 
//       // 나머지에 대해서 순열을 구한다.
//       const attached = permutations.map((el) => [fixed, ...el]);
//       //  돌아온 순열에 떼 놓은(fixed) 값 붙이기
//       results.push(...attached); 
//       // 배열 spread syntax 로 모두다 push
//     });

//     return results; // 결과 담긴 results return
// }



// function solution(n, k) {
//     const arr = Array.from({length: n}, (_, i)=> i+1)

//     const answer_list = getPermutations(arr,n)

//     const answer = answer_list[k-1]

//     return answer;
// }