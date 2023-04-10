function solution(n) {
    var answer = 0;

    let a = 1
    let b = 2

    if ( n === 1 ) {
        answer = a
    } else if (n === 2){
        answer = b
    } else {
        let temp =0
        for(let i =0; i<n-2;i++){
            temp = a
            a = b
            b = (a + temp)%1000000007
        }
        answer = b
    }

    return answer;
}

console.log(solution(7))

