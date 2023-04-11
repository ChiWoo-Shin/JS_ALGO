const getPermutations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]); 
    // n개중에서 1개 선택할 때(nP1), 바로 모든 배열의 원소 return. 1개선택이므로 순서가 의미없음.

    arr.forEach((fixed, index, origin) => {
      const rest = [...origin.slice(0, index), ...origin.slice(index+1)] 
      // 해당하는 fixed를 제외한 나머지 배열 
      const permutations = getPermutations(rest, selectNumber - 1); 
      // 나머지에 대해서 순열을 구한다.
      const attached = permutations.map((el) => [fixed, ...el]); 
      //  돌아온 순열에 떼 놓은(fixed) 값 붙이기
      results.push(...attached); 
      // 배열 spread syntax 로 모두다 push
    });

    return results; // 결과 담긴 results return
}

function check_bin(num){
    root_num = Math.sqrt(num) >> 0

    for(let i =2; i<root_num+1;i++){
        if(num%i ===0){
            return false
        }
    }

    return true
}

function solution(numbers) {
    var answer = new Set();
    arr = [...numbers]
    for(let i=1;i<arr.length+1;i++){
        arr2 = getPermutations(arr, i)

        arr2.map(x => {
            let temp;
            temp = Number(x.join(""))

            if (!(temp===0||temp===1)){
                if(check_bin(temp)){
                    answer.add(temp)
                }
            }
        })
    }
    
    return answer.size;
}

console.log(solution("17"))