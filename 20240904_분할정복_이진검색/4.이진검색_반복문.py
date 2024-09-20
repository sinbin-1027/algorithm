arr = [2, 4, 7, 9, 11, 19, 23]
# 이진 탐색은 정렬된 데이터에 적용 가능하다.
# arr.sort()


def binary_search(target):
    low = 0
    high = len(arr) - 1
    # 탐색 횟수 카운팅
    cnt = 0

    while low <= high:
        mid = (low + high) // 2
        cnt += 1

        if arr[mid] == target:
            return mid, cnt
        elif arr[mid] > target:  # 왼쪽을 확인해야 한다 = high 값을 mid - 1 로 설정
            high = mid - 1
        else:   # 오른쪽을 확인해야 한다 = low 값을 mid + 1 로 설정
            low = mid + 1
    return -1, cnt


print(f'9 = {binary_search(9)}')
print(f'2 = {binary_search(2)}')
print(f'20 = {binary_search(20)}')
