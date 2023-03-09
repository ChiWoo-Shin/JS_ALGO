/*
    1차 코드
*/
// function solution(want, number, discount) {
//     let answer = 0;
//     const totalNumber = number.reduce((acc, cur)=>acc + cur, 0);
//     for (let i = 0; i <= discount.length-totalNumber; i+= 1){
//         const maxI = (i+10>discount.length) ? discount.length : i+ 10;
//         const subArr = discount.slice(i, maxI);
//         const obj = {};
//         for (let j = 0; j < subArr.length; j+=1){
//             if (obj.hasOwnProperty(subArr[j])) obj[subArr[j]] += 1;
//             else obj[subArr[j]] = 1;
//         }
//         let flag = true;
//         for (let j = 0; j < want.length; j+=1){
//             if (obj.hasOwnProperty(want[j]) && obj[want[j]]>=number[j]) continue;
//             else{
//                 flag = false;
//                 break;
//             }
//         }
//         if (flag) answer += 1
//     }
//     return answer;
// }

/*
    2차 코드
*/
// function getCntObj(arr) {
//     const obj = {};
//     for (let j = 0; j < arr.length; j += 1) {
//         if (obj.hasOwnProperty(arr[j])) obj[arr[j]] += 1;
//         else obj[arr[j]] = 1;
//     }
//     return obj;
// }

// function isAnswer(obj, want, number) {
//     for (let i = 0; i < want.length; i += 1) {
//         if (!obj.hasOwnProperty(want[i]) || obj[want[i]] !== number[i]) return false;
//     }
//     return true;
// }

// function solution(want, number, discount) {
//     let answer = 0;

//     /* 적어도 discount에 남은 product의 개수가 number 총 합보다는 많거나 같아야 한다.
//         따라서 reduce를 사용해 number의 총합을 구했다.
//         그리고 discount 배열을 순회할 때 전체를 돌지 않고 i <= discount.length - totalNumber으로 for문 종료 조건을 정했다.
//     */

//     const totalNumber = number.reduce((acc, cur) => acc + cur, 0);
//     for (let i = 0; i <= discount.length - totalNumber; i += 1) {
//         // const maxI = (i+10>discount.length) ? discount.length : i+ 10;
//         const subArr = discount.slice(i, i + 10);
//         const obj = getCntObj(subArr);

//         if (isAnswer(obj, want, number)) answer += 1;
//     }
//     return answer;
// }

/*
    3차 코드
*/
function solution(want, number, discount) {
    const totalNum = number.reduce((acc, cur) => acc + cur, 0);
    let wantArr = [];
    let answer = 0;
    for (let i = 0; i < want.length; i += 1) {
        for (let j = 0; j < number[i]; j += 1) wantArr.push(want[i]);
    }
    wantArr.sort();
    for (let i = 0; i <= discount.length - totalNum; i += 1) {
        /*Array.prototype.slice(start, end)
            end가 array 길이보다 크다면 배열의 끝까지만 추출한다.
            따라서 알아서 아래의 비교문은 필요 없다.
        */
        // const maxI = (i+10>discount.length) ? discount.length : i+10;
        const tmp = discount.slice(i, i + 10).sort();
        /* js에서 두 배열을 비교하는 방법
            1. arr1.toString() === arr2.toString()
            2. JSON.stringify(arr1) === JSON.stringify(arr2)
        */
        /* 문제에서 "10일 연속으로 일치할 경우"라고 적혀 있다.
            "원하는 개수 <= 살 수 있는 개수" 가 아니라
            "원하는 개수 === 살 수 있는 개수"이어야 한다.
            따라서 아래의 비교문으로 answer의 개수를 구하면 된다. (문제 좀 잘 읽자.)
        */
        answer += wantArr.toString() === tmp.toString();
    }
    return answer;
}
