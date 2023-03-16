class Queue {
    constructor() {
        this.storage = {};
        this.front = 0;
        this.rear = 0;
    }

    size() {
        if (this.storage[this.rear] === undefined) return 0;
        else return this.rear - this.front + 1;
    }

    add(value) {
        if (this.size() === 0) {
            this.storage["0"] = value;
        } else {
            this.rear += 1;
            this.storage[this.rear] = value;
        }
    }

    popleft() {
        let temp;
        if (this.size() === 0) temp = undefined;
        else if (this.front === this.rear) {
            temp = this.storage[this.front];
            delete this.storage[this.front];
            this.front = 0;
            this.rear = 0;
        } else {
            temp = this.storage[this.front];
            delete this.storage[this.front];
            this.front += 1;
        }
        return temp;
    }
}

function bfs(distance, queue, obj) {
    let longest = 0;
    while (queue.size() > 0) {
        const start = queue.popleft();
        for (let i = 0; i < obj[start].length; i += 1) {
            const next = obj[start][i]; // 2
            if (distance[next] === -1) {
                distance[next] = distance[start] + 1;
                queue.add(next);
                longest = Math.max(longest, distance[next]);
            }
        }
    }
    return longest;
}

function solution(n, edge) {
    const obj = {};
    for (let i = 0; i < edge.length; i += 1) {
        const [node1, node2] = edge[i];
        if (obj.hasOwnProperty(node1)) obj[node1].push(node2);
        else obj[node1] = [node2];

        if (obj.hasOwnProperty(node2)) obj[node2].push(node1);
        else obj[node2] = [node1];
    }

    const distance = new Array(n + 1).fill(-1);
    distance[1] = 0;
    const queue = new Queue();
    queue.add(1);
    const longest = bfs(distance, queue, obj);
    return distance.filter(elem => elem === longest).length;
}
