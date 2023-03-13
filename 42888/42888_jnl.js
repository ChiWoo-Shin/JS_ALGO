function solution(record) {
    const answer = [];
    const user = {};
    for (let i = 0; i < record.length; i += 1) {
        const [action, uid, nickname] = record[i].split(" ");
        switch (action) {
            case "Enter":
                user[uid] = nickname;
                answer.push("+ " + uid);
                break;
            case "Leave":
                answer.push("- " + uid);
                break;
            case "Change":
                user[uid] = nickname;
                break;
        }
    }
    for (let i = 0; i < answer.length; i += 1) {
        const [action, uid] = answer[i].split(" ");
        if (action === "-") {
            answer[i] = user[uid] + "님이 나갔습니다.";
        } else {
            answer[i] = user[uid] + "님이 들어왔습니다.";
        }
    }
    return answer;
}
