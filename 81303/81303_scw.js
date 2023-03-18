function Node (idx, prev) {
    this.idx = idx;
    this.prev = prev;
    this.next = null;
};

function solution(n, k, cmd) {
    const answer = new Array(n).fill('O');
    let preNode = new Node(0, null);
    let cur = preNode;

    for (let i=0;i<n;i++){
        const curNode = new Node(i, preNode);
        preNode.next = curNode;
        preNode = curNode;
        if(i === k) cur = curNode;
    }

    const clip_board =[];
    for (let i=0; i<cmd.length; i++){
        let [ord, num] = cmd[i].split(" ");
        
        switch (ord){
            case "D":
                num = parseInt(num);
                while(num>0){
                    cur = cur.next;
                    num--;
                }
                break;
            case "U":
                num = parseInt(num);
                while(num>0){
                    cur = cur.prev;
                    num--;
                }
                break;
            case "C":
                answer[cur.idx] = 'X'
                clip_board.push(cur);
                if(cur.next === null){
                    cur.prev.next = null;
                    cur = cur.prev;
                }else{
                    cur.prev.next = cur.next;
                    cur.next.prev = cur.prev;
                    cur = cur.next;
                }
                break;
            case "Z":
                const cp_out = clip_board.pop();
                answer[cp_out.idx] = 'O';
                const pre_cp_out = cp_out.prev;
                const next_cp_out = cp_out.next;

                if(pre_cp_out) pre_cp_out.next = cp_out;
                if(next_cp_out) next_cp_out.prev = cp_out;
                break;
        }
    }


    return answer.join("");
}

console.log(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

// 정답 O 효율성 X
// function solution(n, k, cmd) {
//     var answer = new Array(n).fill('X');
//     let arr = new Array(n);
    
//     for(let i=0;i<n;i++){
//         arr[i] = i;
//     }

//     let cursor = k;
//     let clip_board = [];
//     let order_idx = 0;
    
//     while(cmd.length>order_idx){
//         let temp = cmd[order_idx];
//         if(temp[0] === 'D' || temp[0] === 'U'){
//             let [ord, cnt] = temp.split(" ");
//             cnt = parseInt(cnt);
//             if (ord === 'D'){
//                 if(cursor+cnt >n-1){
//                     cursor = n-1;
//                 } else {
//                     cursor +=cnt;
//                 }
//             } else {
//                 if(cursor-cnt <=0){
//                     cursor = 0;
//                 } else {
//                     cursor -=cnt;
//                 }
//             }
//         } else if(temp[0] === 'C'){
//             let cp_in = arr.splice(cursor, 1);
//             clip_board.push([cursor, cp_in[0]])
//             n -=1;
//             if (cursor>n-1) cursor=n-1;
//         } else {
//             let [idx, cp_out] = clip_board.pop();
//             arr.splice(idx, 0, cp_out);
//             n++;
//             if(idx<=cursor) cursor++;
//         }
//         order_idx++;
//     }
    
//     for (const num of arr){
//         answer[num] = 'O'
//     }

//     return answer.join('');
// }