function solution(order) {
    const sub_container =[];

    let order_idx = 0;
    for(let i=1; i<order.length+1; i++){
        if (i=== order[order_idx]){
            order_idx++;
            while(sub_container.length>0 && sub_container.at(-1) === order[order_idx]){
                sub_container.pop();
                order_idx++;
            }

        } else {
            sub_container.push(i)
        }
    }

    return order_idx;
}

console.log(solution([5, 4, 3, 2, 1]))