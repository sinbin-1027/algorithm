# 그리디의 핵심 조건
# 탐욕적 선택 조건(Greedy Choice Property): 각 단계의 선택이 이후 선택에 영향을 주지 않는다.
# 최적 부분 구조(Optimal Substructure): 각 단계의 최선의 선택이, 전체 문제의 최선의 해가 된다.
# 예시) 대구 - 충주 - 대전 - 역삼 멀티캠퍼스

# 1. 각 단계에서 최적해를 찾아야 한다.
# 2. 단계의 결과들을 합하는 방법을 찾아야 한다.
# 3. 각 단계의 합 == 전체 문제의 합이라는 것을 증명해야 한다.

coin_list = [500, 100, 50, 10]
target = 1730
cnt = 0

for coin in coin_list:
    possible_cnt = target // coin  # 사용 가능한 동전의 수로 나눔 (ex) 500원이라면 3개 가능)
    
    cnt += possible_cnt  # 동전의 수를 정답에 추가
    target -= coin * possible_cnt  # 동전 금액 만큼 빼준다.

print(cnt)
