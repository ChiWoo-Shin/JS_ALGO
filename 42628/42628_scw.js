class MinHeap {
    constructor() {
        this.heap = [ null ];
    }
    
    size() {
        return this.heap.length - 1;
    }
    
    getMin() {
        return this.heap[1] ? this.heap[1] : null;
    }
    
    swap(a, b) {
        [ this.heap[a], this.heap[b] ] = [ this.heap[b], this.heap[a] ];
    }
    
    heappush(value) {
        this.heap.push(value);
        let curIdx = this.heap.length - 1;
        let parIdx = (curIdx / 2) >> 0;
        
        while(curIdx > 1 && this.heap[parIdx] > this.heap[curIdx]) {
            this.swap(parIdx, curIdx)
            curIdx = parIdx;
            parIdx = (curIdx / 2) >> 0;
        }
    }
    
    heappop() {
        const min = this.heap[1];	
        if(this.heap.length <= 2) this.heap = [ null ];
        else this.heap[1] = this.heap.pop();   
        
        let curIdx = 1;
        let leftIdx = curIdx * 2;
        let rightIdx = curIdx * 2 + 1; 
        
        if(!this.heap[leftIdx]) return min;
        if(!this.heap[rightIdx]) {
            if(this.heap[leftIdx] < this.heap[curIdx]) {
                this.swap(leftIdx, curIdx);
            }
            return min;
        }

        while(this.heap[leftIdx] < this.heap[curIdx] || this.heap[rightIdx] < this.heap[curIdx]) {
            const minIdx = this.heap[leftIdx] > this.heap[rightIdx] ? rightIdx : leftIdx;
            this.swap(minIdx, curIdx);
            curIdx = minIdx;
            leftIdx = curIdx * 2;
            rightIdx = curIdx * 2 + 1;
        }

        return min;
    }
}

function solution(operations) {
    var answer = [];

    const min_heap = new MinHeap;
    const max_heap = new MinHeap;
    const dic ={};

    for(let i=0;i<operations.length;i++){
        let [order, num] = operations[i].split(' ');

        if(order === 'I'){
            min_heap.heappush(Number(num));
            max_heap.heappush(Number(num)*(-1));
            dic[num] =1;
        }
        else if (order === 'D' && num === '1'){
            if(max_heap.size()){
                let v = max_heap.heappop();
                if(dic[-v]){
                    dic[-v]--;
                }
            }
        } else if (order === 'D' && num === '-1'){
            if(min_heap.size()){
                let x = min_heap.heappop();
                if(dic[x]){
                    dic[x]--;
                }
            }
        }

        for(const key in dic){
            if(!dic[key]){
                if(min_heap.heap.includes(Number(key))){
                    let idx = min_heap.heap.findIndex(x => x===(Number(key)))
                    min_heap.heap.splice(idx,1)
                }
                if(max_heap.heap.includes(-key)){
                    let idx = max_heap.heap.findIndex(x => x===(-key))
                    max_heap.heap.splice(idx,1)
                }
            }
        }
    }

    let temp=[]
    for(const key in dic){
        if(dic[key]){
            temp.push(key)
        }
    }
    if(temp.length===0){
        answer = [0, 0]
    } else{
        answer = [Math.max(...temp), Math.min(...temp)]
    }

    return answer;
}

console.log(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))