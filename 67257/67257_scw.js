function solution(expression) {
    var answer = 0;

    function calculator (num1, num2, oper){
        switch (oper){
            case '+':
                return num1+num2;
            case '-':
                return num1-num2;
            case '*':
                return num1*num2;
        }
    }

    const comb = [
        ["+", "-", "*"],
        ["+", "*", "-"],
        ["-", "+", "*"],
        ["-", "*", "+"],
        ["*", "+", "-"],
        ["*", "-", "+"],
    ];

    comb.forEach((operator) => {
        const num = expression.match(/[0-9]+/g).map(Number);
        const op_array = expression.match(/[\+\-\*]/g);

        operator.forEach((op)=>{
            let idx = op_array.indexOf(op);
            while (idx!==-1){
                num[idx] = calculator(num[idx], num[idx+1], op);
                num.splice(idx+1,1);
                op_array.splice(idx,1);
                idx = op_array.indexOf(op);
            }
        });
        if (answer < Math.abs(num[0])) answer = Math.abs(num[0]);
    })
    return answer;
}

console.log(solution("100-200*300-500+20"))