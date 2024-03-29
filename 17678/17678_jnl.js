class MinHeap {
    constructor() {
        this.heap = [null];
    }
    size() {
        return this.heap.length - 1;
    }
    getMin() {
        return this.heap[1] ? this.heap[1] : null;
    }
    swap(a, b) {
        [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
    }
    heappush(value) {
        this.heap.push(value);
        let curIdx = this.heap.length - 1;
        let parIdx = (curIdx / 2) >> 0;

        while (curIdx > 1 && this.heap[parIdx] > this.heap[curIdx]) {
            this.swap(parIdx, curIdx);
            curIdx = parIdx;
            parIdx = (curIdx / 2) >> 0;
        }
    }
    heappop() {
        const min = this.heap[1];
        if (this.heap.length <= 2) this.heap = [null];
        else this.heap[1] = this.heap.pop(); // 맨 뒤에 있는 노드를 루트 노드로 올림

        let curIdx = 1;
        let leftIdx = curIdx * 2;
        let rightIdx = curIdx * 2 + 1;

        if (!this.heap[leftIdx]) return min; // 왼쪽 자식 노드가 없다. -> cur노드가 리프노드
        if (!this.heap[rightIdx]) {
            // 왼쪽 자식은 있지만 오른쪽 자식이 없다.
            if (this.heap[leftIdx] < this.heap[curIdx]) this.swap(leftIdx, curIdx);
            return min;
        }
        // 왼쪽 오른쪽 자식 모두 있다.
        while (this.heap[leftIdx] < this.heap[curIdx] || this.heap[rightIdx] < this.heap[curIdx]) {
            const minIdx = this.heap[leftIdx] > this.heap[rightIdx] ? rightIdx : leftIdx;
            this.swap(minIdx, curIdx);
            curIdx = minIdx;
            leftIdx = curIdx * 2;
            rightIdx = curIdx * 2 + 1;
        }
        return min;
    }
}

function makeAnswerForm(num) {
    let hour = (num / 60) >> 0;
    let min = num % 60;
    if (hour < 10) hour = "0" + hour;
    if (min < 10) min = "0" + min;
    return hour + ":" + min;
}

function solution(n, t, m, timetable) {
    if (timetable.length < m) {
        const total = 540 + (n - 1) * t;
        return makeAnswerForm(total);
    }
    const minHeap = new MinHeap();

    for (const elem of timetable) {
        let [hour, min] = elem.split(":");
        hour = parseInt(hour) * 60;
        min = parseInt(min);
        minHeap.heappush(hour + min);
    }

    let now = 540;
    for (let i = 0; i < n - 1; i += 1) {
        for (let j = 0; j < m; j += 1) {
            const crew = minHeap.heappop();
            if (now < crew) {
                minHeap.heappush(crew);
                break;
            }
        }
        now += t;
    }

    const lastShuttle = [];
    for (let i = 0; i < m; i += 1) {
        if (minHeap.size() <= 0) break;
        const crew = minHeap.heappop();
        if (crew <= now) lastShuttle.push(crew);
        else break;
    }
    if (lastShuttle.length === m) {
        return makeAnswerForm(lastShuttle[m - 1] - 1);
    } else {
        return makeAnswerForm(now);
    }
}
