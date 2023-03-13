function solution(dirs) {
    let answer = 0;
    const map = [];
    for (let i = 0; i < 11; i += 1) {
        const temp = [];
        for (let j = 0; j < 11; j += 1) {
            temp.push([]);
        }
        map.push(temp);
    }
    let curX = 5;
    let curY = 5;
    for (let i = 0; i < dirs.length; i += 1) {
        const dir = dirs[i];
        let nx,
            ny = 0;
        switch (dir) {
            case "U":
                ny = curY - 1;
                if (ny < 0) continue;
                if (map[curX][curY].includes(`${curX} ${ny}`)) {
                    curY = ny;
                } else {
                    map[curX][curY].push(`${curX} ${ny}`);
                    map[curX][ny].push(`${curX} ${curY}`);
                    curY = ny;
                    answer += 1;
                }
                break;
            case "D":
                ny = curY + 1;
                if (ny > 10) continue;
                if (map[curX][curY].includes(`${curX} ${ny}`)) {
                    curY = ny;
                } else {
                    map[curX][curY].push(`${curX} ${ny}`);
                    map[curX][ny].push(`${curX} ${curY}`);
                    curY = ny;
                    answer += 1;
                }
                break;
            case "R":
                nx = curX + 1;
                if (nx > 10) continue;
                if (map[curX][curY].includes(`${nx} ${curY}`)) {
                    curX = nx;
                } else {
                    map[curX][curY].push(`${nx} ${curY}`);
                    map[nx][curY].push(`${curX} ${curY}`);
                    curX = nx;
                    answer += 1;
                }
                break;
            case "L":
                nx = curX - 1;
                if (nx < 0) continue;
                if (map[curX][curY].includes(`${nx} ${curY}`)) {
                    curX = nx;
                } else {
                    map[curX][curY].push(`${nx} ${curY}`);
                    map[nx][curY].push(`${curX} ${curY}`);
                    curX = nx;
                    answer += 1;
                }
                break;
        }
    }
    return answer;
}

/*
배열이 아니라 문자열로 방문했던 길인지 기록한 코드

function solution(dirs){
    const set = new Set();
    const [min, max] = [-5, 5];
    let curX = 0;
    let curY = 0;
    let prev = '';
    
    for (let i = 0; i < dirs.length; i+=1){
        prev = "" + curX + curY;
        const dir = dirs[i];
        switch(dir){
            case 'U':
                if (curY + 1 <= max) curY += 1;
                else continue;
                break;
            case 'D':
                if (curY -1 >= min) curY -= 1;
                else continue;
                break;
            case 'R':
                if (curX + 1<= max) curX += 1;
                else continue;
                break;
            case 'L':
                if(curX - 1 >= min) curX -= 1;
                else continue;
                break;
            
        }
        set.add(`${curX}${curY}${prev}`);
        set.add(`${prev}${curX}${curY}`);
    }
    return set.size / 2;
}
*/
