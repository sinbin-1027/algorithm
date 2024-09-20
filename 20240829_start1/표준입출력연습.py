# A, B 를 입력받고 더한 값을 출력하세요.
# 2 3

# 코드 제출에는 아래 코드를 반드시 주석처리!!
import sys
# sys.stdin: 표준 입력
# open('input.txt', 'r'): input.txt 를 r(읽기 전용)으로 열겠다.
sys.stdin = open('input.txt', 'r')
# sys.stdout: 표준 출력
# open('output.txt', 'w'): output.txt 를 w(쓰기 전용)으로 열겠다.
sys.stdout = open('output.txt', 'w')

A, B = map(int, input().split())
print(A + B)

