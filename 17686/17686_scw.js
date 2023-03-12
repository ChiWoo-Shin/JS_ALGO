function solution(files) {
    var answer = [];
    let file_list= [];

    for(let i=0;i<files.length;i++){
        let Head = '';
        let Num = '';
        let Tail = '';
        let prev= '';
        for (let j=0; j<files[i].length;j++){
            if(Object.is(parseInt(files[i][j]), NaN)){
                if(!Object.is(parseInt(prev), NaN)){
                    Tail = files[i].substring(j);
                    break;
                }
                Head+=files[i][j];
                prev = files[i][j];
            } else {
                Num += files[i][j];
                prev = files[i][j];
            }
        }

        file_list.push([Head, Num, Tail])
    }
    file_list.sort((a,b) => {
        if (a[0].toLowerCase() > b[0].toLowerCase()){
            return 1;  
        } else if (a[0].toLowerCase() < b[0].toLowerCase()){
            return -1;
        } else {
            if(parseInt(a[1]) >= parseInt(b[1])){
                return 1;
            } else {
                return -1;
            }
        }
    })

    answer = file_list.map(x => x.join(''));

    return answer;
}

console.log(solution(["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT", "foo9.txt", "foo010bar020.zip", "F-15"]))