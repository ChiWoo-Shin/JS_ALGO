import sys
input = sys.stdin.readline
N = int(input())
arr1 = list(map(int, input().split(' ')))
M = int(input())
arr2 = list(map(int, input().split(' ')))

def binarySearch(target):
    s = 0
    e = N
    while s < e:
        mid = (s+e)//2
        if target == arr1[mid]:
            return True
        elif target > arr1[mid]:
            s = mid+1
        else:
            e = mid
    return False

def solution():
    arr1.sort()
    for elem in arr2:
        if binarySearch(elem):
            print('1')
        else:
            print('0')

solution()