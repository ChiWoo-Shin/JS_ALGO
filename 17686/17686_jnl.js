function solution(files) {
    const obj = {};
    for (let i = 0; i < files.length; i += 1) {
        const file = files[i].toUpperCase();
        let head = "";
        let number = "";

        for (let j = 0; j < file.length; j += 1) {
            if (isNaN(file[j]) || file[j] === " " || file[j] === "." || file[j] === "-") {
                if (!number) head += file[j];
                else break;
            } else number += file[j];
        }

        if (obj.hasOwnProperty(head)) {
            obj[head].push([number, i]);
        } else {
            obj[head] = [[number, i]];
        }
    }
    const keys = Object.keys(obj).sort();
    const arr = [];
    for (let i = 0; i < keys.length; i += 1) {
        const valueArr = obj[keys[i]].sort((a, b) => a[0] - b[0]);

        for (let j = 0; j < valueArr.length; j += 1) {
            const index = valueArr[j][1];
            arr.push(files[index]);
        }
    }
    return arr;
}

/*

정규표현식 사용 풀이

function solution(files){
	return files.sort((a, b)=>{
		const headerA = a.match(/^\D+/)[0].toLowerCase();
		const headerB = b.match(/^\D+/)[0].toLowerCase();
		
		if(headerA < headerB) return -1;
		if(headerA > headerB) return 1;
		
		const numberA = a.match(/\d+/)[0].replace(/^0+/, '');
		const numberB = b.match(/\d+/)[0].replace(/^0+/, '');
		
		return numberA - numberB;
	});
}*/
