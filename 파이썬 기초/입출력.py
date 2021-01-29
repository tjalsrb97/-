"""
# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)
"""

"""
# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)
"""

"""
# sys라이브러리를 사용함으로써 한 줄 입력 가능
import sys
data = sys.stdin.readline().rstrip()
print(data)
"""

""""
a = 1
b = 2

print(a, b)
print(a)
print(b)
"""
'''
# 출력할 변수들
answer = 7
print("정답은 " + str(answer) +"입니다")
print("정답은", str(answer), "입니다")
print(f"정답은 {answer}입니다")
'''




