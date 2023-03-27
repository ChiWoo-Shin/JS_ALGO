function solution(n, t, m, timetable) {
    var answer = '';
    const start = 9*60 // 9시부터 시작

    const timetable_min=timetable.map((v) =>{
        let [h, m] = v.split(":").map(Number)
        return h*60+m
    })
    timetable_min.sort((a,b) => a-b)

    const bus_timetable = new Array(n).fill([start, 0])
    const bus_timetable_min = bus_timetable.map((v, i) => { 
        return [v[0]+ t*i, 0]
        })

    let bus_idx =0;

    for(let i =0;i<timetable_min.length;i++){
        if(bus_idx === bus_timetable_min.length) break;
        if((timetable_min[i]<=bus_timetable_min[bus_idx][0]) && (bus_timetable_min[bus_idx][1]< m)){
            bus_timetable_min[bus_idx][1]++;
            // if(bus_timetable_min[bus_idx][1]===m){
            //     bus_idx++;
            // }
        } else {
            while(timetable_min[i]>bus_timetable_min[bus_idx][0]){
                bus_idx++;

                if(bus_idx === bus_timetable_min.length) break;
            }
            if(bus_idx === bus_timetable_min.length) break;
            if(timetable_min[i]<=bus_timetable_min[bus_idx][0] && bus_timetable_min[bus_idx][1]< m)
            bus_timetable_min[bus_idx][1]++;
        }
    }
    
    if (bus_timetable_min[n-1][1] === 0){
        let find_ = n-1;
        while(find_>0 && bus_timetable_min[find_][1] === 0){
            find_--;
            if(find_<0){
                find_ = 0;
                break;
            }
        }

        if (bus_timetable_min[find_][1] <m){
            if((Math.floor(bus_timetable_min[find_][0]/60)).toString().length <2){
                answer +='0'+ (Math.floor(bus_timetable_min[find_][0]/60)).toString();
            } else{
                answer += (Math.floor(bus_timetable_min[find_][0]/60)).toString();
            };
            answer +=":";
            if((bus_timetable_min[find_][0]%60).toString().length <2){
                answer +='0'+ (bus_timetable_min[find_][0]%60).toString();
            } else{
                answer += (bus_timetable_min[find_][0]%60).toString();
            };
        } else {
            if((Math.floor(bus_timetable_min[find_][0]/60)).toString().length <2){
                answer +='0'+ (Math.floor(bus_timetable_min[find_][0]/60)).toString();
            } else{
                answer += (Math.floor(bus_timetable_min[find_][0]/60)).toString();
            };
            answer +=":";
            if((bus_timetable_min[find_][0]%60-1).toString().length <2){
                if(bus_timetable_min[find_][0]%60-1 <0){
                    answer = (Number(answer.split(":")[0])-1).toString()+":59"
                }
                else{
                    answer +='0'+ (bus_timetable_min[find_][0]%60-1).toString();
                }
            } else{
                if(bus_timetable_min[find_][0]%60-1 <0){
                    answer = (Number(answer.split(":")[0])-1).toString()+":59"
                }else{
                    answer += (bus_timetable_min[find_][0]%60-1).toString();
                }
            };
            
        }
        
    } else {
        let find_ = n-1;
        if (bus_timetable_min[find_][1] <m){
            if((Math.floor(bus_timetable_min[find_][0]/60)).toString().length <2){
                answer +='0'+ (Math.floor(bus_timetable_min[find_][0]/60)).toString();
            } else{
                answer += (Math.floor(bus_timetable_min[find_][0]/60)).toString();
            };
            answer +=":";
            if((bus_timetable_min[find_][0]%60).toString().length <2){
                answer +='0'+ (bus_timetable_min[find_][0]%60).toString();
            } else{
                answer += (bus_timetable_min[find_][0]%60).toString();
            };
        } else {
            if((Math.floor(bus_timetable_min[find_][0]/60)).toString().length <2){
                answer +='0'+ (Math.floor(bus_timetable_min[find_][0]/60)).toString();
            } else{
                answer += (Math.floor(bus_timetable_min[find_][0]/60)).toString();
            };
            answer +=":";
            if((bus_timetable_min[find_][0]%60-1).toString().length <2){
                if(bus_timetable_min[find_][0]%60-1 <0){
                    answer = (Number(answer.split(":")[0])-1).toString()+":59"
                }
                else{
                    answer +='0'+ (bus_timetable_min[find_][0]%60-1).toString();
                }
            } else{
                if(bus_timetable_min[find_][0]%60-1 <0){
                    answer = (Number(answer.split(":")[0])-1).toString()+":59"
                }else{
                    answer += (bus_timetable_min[find_][0]%60-1).toString();
                }
            };
            
        }
    }

    return answer;
}

console.log(solution(1, 1, 1, ["23:59"]))