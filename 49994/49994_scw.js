function solution(dirs) {
    var answer = 0;
    var dic ={
        'U' : [-1,0],
        'D' : [1,0],
        'L' : [0,-1],
        'R' : [0,1]
    }

    function removeDup(arr) {
        return [...new Set(arr.join("|").split("|"))]
          .map((v) => v.split(","))
          .map((v) => v.map((a) => +a));
    }

    var visited =[];
    var s = [5,5];
    for (let i=0;i<dirs.length;i++){
        if (0<=s[0]+dic[dirs[i]][0] && s[0]+dic[dirs[i]][0]<11 && 0<=s[1]+dic[dirs[i]][1] && s[1]+dic[dirs[i]][1]<11){
            visited.push([s[0],s[1], s[0]+dic[dirs[i]][0], s[1]+dic[dirs[i]][1]])
            visited.push([s[0]+dic[dirs[i]][0], s[1]+dic[dirs[i]][1], s[0],s[1],])
            s[0] = s[0]+dic[dirs[i]][0]
            s[1] = s[1]+dic[dirs[i]][1]
        }
    }
    let visited_result = removeDup(visited)
    answer = parseInt(visited_result.length/2)
    return answer;
}

console.log(solution("ULURRDLLU"))