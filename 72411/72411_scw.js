const getCombinations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]); 
    // n개중에서 1개 선택할 때(nC1), 바로 모든 배열의 원소 return

    arr.forEach((fixed, index, origin) => {
      const rest = origin.slice(index + 1); 
      // 해당하는 fixed를 제외한 나머지 뒤
      const combinations = getCombinations(rest, selectNumber - 1); 
      // 나머지에 대해서 조합을 구한다.
      const attached = combinations.map((el) => [fixed, ...el]); 
      //  돌아온 조합에 떼 놓은(fixed) 값 붙이기
      results.push(...attached); 
      // 배열 spread syntax 로 모두다 push
    });

    return results; // 결과 담긴 results return
}

function solution(orders, course) {
    var answer = [];
    let order_list = {};

    let course_dic = {};
    for(let ele of course){
        course_dic[ele] =''
    }

    orders.forEach((order)=>{
        course.forEach((co)=>{
            order = [...order].sort()
            console.log(order)
            let comb_order = getCombinations(order,co)

            comb_order.forEach((comb_co)=>{
                if(!order_list[comb_co]){
                    order_list[comb_co] = 1
                } else {
                    order_list[comb_co]++
                }
            })
        })
    })

    
    const sort_order_list = Object.entries(order_list).sort((a,b) => {
        return a[0].length - b[0].length
        })
    
    console.log(sort_order_list)
    for(let ele of sort_order_list){
        if(course_dic[ele[0].replace(/,/g,"").length.toString()] !==""){
            if(course_dic[ele[0].replace(/,/g,"").length.toString()][0][1] < ele[1]){
                course_dic[ele[0].replace(/,/g,"").length.toString()] = [[ele[0].replace(/,/g,""), ele[1]]]
            } else if(course_dic[ele[0].replace(/,/g,"").length.toString()][0][1] === ele[1]){
                course_dic[ele[0].replace(/,/g,"").length.toString()].push([ele[0].replace(/,/g,""), ele[1]])
            }
        } else {
            if(ele[1]>=2){
                course_dic[ele[0].replace(/,/g,"").length.toString()] = [[ele[0].replace(/,/g,""), ele[1]]]
            }
        }
    }

    Object.values(course_dic).forEach((ele)=>{
        for(let value of ele){
            answer.push(value[0])
        }
    })

    // Object.values(course_dic).forEach((ele)=>{
    //     ele.forEach((ele_2)=>{
    //         answer.push(ele_2[0])
    //     })
    // })

    answer.sort();

    return answer;
}

console.log(solution(["XYZ", "XWY", "WXA"], [2,3,4]))