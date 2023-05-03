def biggerIsGreater(w):
    start = -1
    for i in range(len(w)-1, 0, -1):
        # 자신보다 오른쪽에 더 작은 수가 있는지
        if w[i] > w[i-1]:
            start = i-1
            break
    if start < 0:
        return 'no answer'
    arr = list(w)
    end = start+1
    for i in range(start+1, len(w)):
        # end 포인터: start 포인터가 가리키는 문자보다 큰 문자 중 가장 작은 문자를 가리키도록
        if ord(w[end]) > ord(w[i]) and ord(w[i]) > ord(w[start]):
            end = i
    arr[start], arr[end] = arr[end], arr[start]
    result = arr[:start+1]+sorted(arr[start+1:])
    return ''.join(result)