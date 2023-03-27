function solution(skill, skill_trees) {
    let answer = 0;
    const obj = {};
    for (let i = 0; i < skill.length; i += 1) {
        obj[skill[i]] = i;
    }
    for (const skill_tree of skill_trees) {
        let curStep = 0;
        for (let i = 0; i < skill_tree.length; i += 1) {
            if (obj.hasOwnProperty(skill_tree[i])) {
                if (obj[skill_tree[i]] === curStep) curStep += 1;
                else {
                    curStep = -1;
                    break;
                }
            }
        }
        if (curStep >= 0) answer += 1;
    }
    return answer;
}
