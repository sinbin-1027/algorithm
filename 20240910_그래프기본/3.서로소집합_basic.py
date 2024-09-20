def make_set(n):
    p = [i for i in range(n)]  # 각 원소의 부모를 자신으로 초기화
    return p


def find(x):

    if parents[x] == x:  # x 자기자신이 x 를 바라본다 == 해당 집합의 대표자를 찾았다
        return x

    return find(parents[x]) # x의 부모가 가리키고 있는 정점부터 다시 대표자를 탐색

def union(x, y):
    # x 와 y 의 대표자를 찾자.
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:  # 이미 같은 집합이면 끝
        return

    # 다른 집합이라면 더 작은 루트노트에 합친다.
    # 문제에 따라 다르다.
    if root_x < root_y:
        parents[root_y] = root_x  # y 가 바라보는 부모는 x 의 대표자
        parents[y] = root_x # y가 바라보는 부모는 x의 대표자
    else:
        parents[root_x] = root_y


# 예제 사용법
n = 7  # 원소의 개수
parents = make_set(n)  # 집합생성. parents 에 부모 정보들을 저장

union(1, 3)
union(2, 3)
union(5, 6)

print(parents)  # 대표자의 수 == 집합의 수

print('find_set(6) = ', find(6))

target_x = 3
target_y = 4

# 원소 1과 원소 2가 같은 집합에 속해 있는지 확인
if find(target_x) == find(target_y):
    print(f"원소 {target_x}과 원소 {target_y}는 같은 집합에 속해 있습니다.")
else:
    print(f"원소 {target_x}과 원소 {target_y}는 다른 집합에 속해 있습니다.")
