const Node = function (index, prev) {
    this.index = index;
    this.prev = prev;
    this.next = null;
};

function solution(n, k, cmd) {
    const answer = new Array(n).fill("O");
    let prevNode = new Node(0, null);
    let select = prevNode;

    for (let i = 0; i < n; i += 1) {
        const curNode = new Node(i, prevNode);
        prevNode.next = curNode;
        prevNode = curNode;
        if (i === k) {
            select = curNode;
        }
    }
    const bin = [];
    for (let i = 0; i < cmd.length; i += 1) {
        const elem = cmd[i].split(" ");
        let num;

        switch (elem[0]) {
            case "D":
                num = parseInt(elem[1]);
                while (num > 0) {
                    select = select.next;
                    num -= 1;
                }
                break;
            case "U":
                num = parseInt(elem[1]);
                while (num > 0) {
                    select = select.prev;
                    num -= 1;
                }
                break;
            case "C":
                bin.push(select);
                answer[select.index] = "X";
                if (select.next === null) {
                    select.prev.next = null;
                    select = select.prev;
                } else {
                    select.prev.next = select.next;
                    select.next.prev = select.prev;
                    select = select.next;
                }
                break;
            case "Z":
                const node = bin.pop();
                answer[node.index] = "O";
                const p = node.prev;
                const n = node.next;
                if (p) p.next = node;
                if (n) n.prev = node;

                break;
        }
    }
    return answer.join("");
}
