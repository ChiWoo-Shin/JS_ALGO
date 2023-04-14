function bracket_modify(bracket){
    console.log("bracket",bracket)
    bracket = [...bracket]
    bracket_temp = bracket.slice(1, bracket.length-1)

    for(let i=0; i<bracket_temp.length; i++){
        if (bracket_temp[i] === '('){
            bracket_temp[i] = ')'
        } else if (bracket_temp[i] === ')'){
            bracket_temp[i] = '('
        }
    }
    

    return bracket_temp.join("");
}

function is_correct(bracket){
    let check =0;

    for(const i of bracket){
        if(i==="("){
            check++;
        } else {
            check--;
        }

        if(check<0){
            return false
        }
    }

    return true
}

function solution(p) {
    var answer = '';
    let answer_u='';
    let answer_v='';
    let check_bracket =0;

    if(p===""){
        return ""
    } else{
        for(let i =0;i<p.length;i++){
            console.log("0",answer)
            if(p[i] === '('){
                answer_u +='(';
                check_bracket++;
            } else if (p[i]===')'){
                answer_u +=')';
                check_bracket--;
            }

            if(check_bracket === 0){
                if(is_correct(answer_u)){
                    answer += answer_u;
                    console.log("1",answer_u)
                    answer_u =''
                } else {
                    answer_v += "(" + solution(p.substr(i+1,p.length)) + ")"
                    console.log("2",answer_v)
                    answer += answer_v +  bracket_modify(answer_u);
                    console.log("3", answer)
                    return answer
                }
            }
        }
    }

    return answer;
}

console.log(solution("()))((()"))

