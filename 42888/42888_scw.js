function solution(record) {
    var answer = [];
    var answer_temp = [];
    var id_dic = {}
    
    for(let i=0;i<record.length;i++){
        let temp = record[i].split(' ');
        if(temp[0]==='Enter' || temp[0]==='Leave'){
            answer_temp.push([temp[0], temp[1]])
        }

        if(temp[0]==='Enter' || temp[0]==='Change'){
            id_dic[temp[1]] = temp[2]
        }
    }

    for(let i=0;i<answer_temp.length;i++){
        if(answer_temp[i][0]==='Enter'){
            answer.push(id_dic[answer_temp[i][1]]+"님이 들어왔습니다.")
        } else {
            answer.push(id_dic[answer_temp[i][1]]+"님이 나갔습니다.")
        }
    }

    return answer;
}

console.log(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))