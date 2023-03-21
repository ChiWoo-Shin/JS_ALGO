// 큐 만들기 귀차낭

class Node {
    constructor(val) {
        const self = this;
        self.val = val;
        self.next = null;
    }
}

class Queue {
    constructor() {
        const self = this;
        self.head = null;
        self.tail = null;
    }

    enqueue(val) {
        const self = this;
        const newNode = new Node(val);
        if (!self.head) {
            self.head = newNode;
            self.tail = newNode;
        } else {
            self.tail.next = newNode;
            self.tail = newNode;
        }
    }

    dequeue() {
        const self = this;
        const retVal = self.head.val;
        if (self.head !== self.tail) {
            self.head = self.head.next;
        } else {
            self.head = null;
            self.tail = null;
        }
        return retVal;
    }
}

function solution(board) {
    const queue = new Queue();

    const arr = [];
    for (let i = 0; i < board.length; i++) {
        arr.push([]);
        for (let j = 0; j < board[0].length; j++) {
            arr[i].push(board[i][j]);
            if (board[i][j] === 'R') {
                queue.enqueue([i, j, 0]);
            }
        }
    }

    const dx = [-1, 0, 0, 1];
    const dy = [0, -1, 1, 0];

    while (queue.head) {
        const [x, y, cnt] = queue.dequeue();

        for (let i = 0; i < 4; i++) {
            let x_ = x + dx[i];
            let y_ = y + dy[i];
            if (
                0 <= x_ &&
                x_ < arr.length &&
                0 <= y_ &&
                y_ < arr[0].length &&
                arr[x_][y_] !== 'D' &&
                arr[x_][y_] !== 'X'
            ) {
                while (
                    0 <= x_ + dx[i] &&
                    x_ + dx[i] < arr.length &&
                    0 <= y_ + dy[i] &&
                    y_ + dy[i] < arr[0].length &&
                    arr[x_ + dx[i]][y_ + dy[i]] !== 'D'
                ) {
                    x_ = x_ + dx[i];
                    y_ = y_ + dy[i];
                }
                if (arr[x_][y_] === 'G') {
                    return cnt + 1;
                }
                if (arr[x_][y_] !== 'X') {
                    arr[x_][y_] = 'X';
                    queue.enqueue([x_, y_, cnt + 1]);
                }
            }
        }
    }

    return -1;
}
