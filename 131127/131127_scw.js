function solution(want, number, discount) {
    var answer = 0;


    function check_array(dic, arr) {
        let cnt = 0
        for (let i = 0; i < arr.length; i++) {
            if (!dic[arr[i]]) {
                return false
            } else if (dic[arr[i]] > 0) {
                cnt++;
                dic[arr[i]] -= 1;
            } else {
                return false
            }

            if (cnt === 10) {
                break;
            }
        }
        return true
    }

    for (let j = 0; j <= discount.length - 10; j++) {
        let temp_arr = discount.slice(j, j + 10)
        var dic = {};
        for (let i = 0; i < want.length; i++) {
            dic[want[i]] = number[i]
        }
        let flag = check_array(dic, temp_arr);
        if (flag) answer++;
    }


    return answer;
}

console.log(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))