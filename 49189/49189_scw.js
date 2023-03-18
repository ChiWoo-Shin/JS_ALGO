// 우선순위큐 구현
class PriorityQueue {
  constructor(dist) {
    this.queue = [];
    this.dist = dist;
  }

  enqueue(nodeIndex) {
    this.queue.push(nodeIndex);
  }

  dequeue() {
    let entry = 0;
    let entryIndex = this.queue[entry];

    this.queue.forEach((nodeIndex, idx) => {
      if (this.dist[entryIndex] > this.dist[nodeIndex]) {
        entryIndex = nodeIndex;
        entry = idx;
      }
    });

    return this.queue.splice(entry, 1);
  }
}

function solution(n, edge) {
  // 간선 연결
  const map = new Array(n).fill(null).map(()=> new Array());
  for(let [u, v] of edge){
    map[u - 1].push([v -1, 1]);
    map[v - 1].push([u -1, 1]);
  }

  const dist = new Array(n).fill(Infinity);
  const isVisited = new Array(n).fill(false);
  const pq = new PriorityQueue(dist);

  pq.enqueue(0);
  dist[0] = 0;

  // 다익스트라
  while (pq.queue.length >0){
    const [curr] = pq. dequeue();
    
    if(isVisited[curr]) continue;

    isVisited[curr] = 1;

    for(const [next, temp] of map[curr]){
      if(dist[next] > dist[curr] +1){
        dist[next] = dist[curr] +1
        pq.enqueue(next);
      }
    }
  }

  
  return dist.filter(x => x=== Math.max(...dist)).length;
}

console.log(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))