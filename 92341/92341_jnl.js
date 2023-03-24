function solution(fees, records) {
    const [baseTime, baseFee, unitTime, unitFee] = fees;
    const obj = {};
    for (const record of records) {
        const [strTime, id, action] = record.split(" ");
        const [hour, minute] = strTime.split(":");
        const intTime = parseInt(hour) * 60 + parseInt(minute);
        if (obj.hasOwnProperty(id)) {
            if (action === "OUT") {
                //action === "OUT"
                obj[id].action = action;
                obj[id].totalTime += intTime - obj[id].time;
            } else {
                //action === "IN"
                obj[id].action = action;
                obj[id].time = intTime;
            }
        } else {
            obj[id] = { action: "IN", time: intTime, totalTime: 0 };
        }
    }
    const answer = [];
    const lastExit = 23 * 60 + 59;
    const sortedKeyArr = Object.keys(obj).sort((a, b) => a - b);
    for (const key of sortedKeyArr) {
        let temp = baseFee;
        if (obj[key].action === "IN") {
            // 나간 기록이 없는 차량
            obj[key].totalTime += lastExit - obj[key].time;
        }
        if (obj[key].totalTime > baseTime) {
            temp += Math.ceil((obj[key].totalTime - baseTime) / unitTime) * unitFee;
        }
        answer.push(temp);
    }
    return answer;
}
