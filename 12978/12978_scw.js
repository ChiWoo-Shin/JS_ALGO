function solution(N, road, K) {
    const dist =[0,...Array(N-1).fill(Infinity)];
    const visited = Array(N).fill(false);
    const costs = Array.from(new Array(N), ()=>
        Array.from(new Array(N), () => Infinity)
    );

    for(let i=0;i<road.length;i++){
        costs[road[i][0]-1][road[i][1]-1] = Math.min(costs[road[i][0]-1][road[i][1]-1], road[i][2]);
        costs[road[i][1]-1][road[i][0]-1] = Math.min(costs[road[i][1]-1][road[i][0]-1], road[i][2]);
    }

    const queue = [0];
    while(queue.length>0){
        let cur = 0;
        let idx = 0;
        let point = Infinity;

        for(let j=0; j<queue.length;j++){
            const item = queue[j];
            if(point > dist[item]){
                cur = item;
                point = dist[item];
                idx = j;
            }
        }

        queue.splice(idx, 1);
        visited[cur] = true;

        for(let j=0; j<costs[cur].length; j++){
            const cost = costs[cur][j]+point;

            if(cost !==Infinity && cost<dist[j] && !visited[j]){
                dist[j] = cost;
                queue.push(j);
            }
        }
    }
    
    return dist.filter((x) => x<=K).length;
}

console.log(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))

