# https://docs.python.org/ko/3/library/index.html
# 내장 함수
result = sum([1,2,3,4,5])
print(result)

result = min(7, 3, 5, 2)
print(result)

result = max(7, 3, 5, 2)
print(result)

result = eval("(3+5) * 7")
print(result)

result = sorted([9,1,8,5,4])
print(result)

result = sorted([9,1,8,5,4], reverse=True)
print(result)

result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result)

data=[9,1,8,5,4]
data.sort()
print(data)

#itertools
from itertools import permutations
data = ['A', 'B', 'C'] #데이터 준비
result = list(permutations(data, 2)) #모든 순열 구하기
print(result)

from itertools import combinations
data = ['A', 'B', 'C'] #데이터 준비
result = list(combinations(data, 2)) #2개를 뽑는 모든 조합 구하기
print(result)

from itertools import product
data = ['A', 'B', 'C'] #데이터 준비
result = list(product(data, repeat=2)) #2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

from itertools import combinations_with_replacement
data = ['A', 'B', 'C'] #데이터 준비
result = list(combinations_with_replacement(data, 2)) #2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)

#heapq
import heapq

def heapsort(iterable): # min heap
    h=[]
    result=[]
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

def heapsort(iterable): # max heap
    h=[]
    result=[]
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# bisect
from bisect import bisect_left, bisect_right

a=[1,2,4,4,8]
x=4

print(bisect_left(a, x))
print(bisect_right(a, x))
#정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구할 때 용이

#값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

#리스트 선언
a = [1,2,3,3,3,3,4,4,8,9]
#값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))
#값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))

#collections
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

#math
import math
print(math.factorial(5)) #팩토리얼
print(math.sqrt(7)) #제곱근
print(math.gcd(21, 14)) #최대공약수
print(math.pi)
print(math.e)