#!/usr/bin/env python
# coding: utf-8

# In[1]:


#수 자료형
#정수형
a = 1000
print(a)

a=-7
print(a)

a=0
print(a)


# In[3]:


#실수형
a = 157.93
print(a)

a=-1837.2
print(a)

a=5.
print(a)

a=-.7
print(a)

a=1e9
print(a)


# In[5]:


#지수표현
a = 75.25e1
print(a)

a=3945e-3
print(a)


# In[6]:


#정확한 실수 표현 불가
a=0.3+0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)


# In[7]:


#반올림
a=0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)


# In[9]:


#수자료형의 연산
a=7
b=3

#나누기
print(a/b)
#나머지
print(a%b)
#몫
print(a//b)
#거듭제곱
print(a**b)


# In[11]:


#리스트 자료형
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

print(a[4])

#리스트 선언방법
a = list()
print(a)

a = []
print(a)


# In[23]:


#리스트 0으로 초기화
n = 10
a = [0] * n
print(a)

#리스트 인덱싱과 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1])
print(a[-3])
a[3] = 7
print(a)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:4])

#리스트 컴프리헨션
array = [i for i in range(20) if i%2 == 1]
print(array)
array = [i*i for i in range(1,10)]
print(array)

#N X M 2차원 리스트
n=3
m=4
array = [[0] * m for _ in range(n)]
print(array)
array = [[0]*m]*n
print(array)
array[1][1]=5
print(array) #내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식 => 리스트 컴프리헨션해야함.


# In[24]:


a = [1, 4, 3]
print("기본 리스트: ", a)

a.append(2)
print("삽입: ", a)
a.sort()
print("오름차순 정렬: ", a)
a.sort(reverse = True)
print("내림차순 정렬: ", a)
a.reverse()
print("원소 뒤집기: ", a)
a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)
print("값이 3인 데이터 개수: ", a.count(3))
a.remove(1)
print("값이 1인 데이터 삭제: ", a)


# In[25]:


a=[1,2,3,4,5,5,5]
remove_set={3, 5}

#remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)


# In[30]:


#문자열
data = 'Hello World'
print(data)
data = "Don't you know \"Python\"?"
print(data)

a = "Hello"
b = "World"
print(a+" "+b)
a = "String"
print(a*3)
a="ABCDEF"
print(a[2:4])


# In[31]:


#튜플 자료형
a=(1,2,3,4)
print(a)

a[2]=7#오류가 나는데 튜플은 대입 연산자를 사용하여 값을 변경할 수 없다. 튜플은 주로 주로 그래프 알고리즘에 자주 사용된다.


# In[38]:


#사전 자료형 => 해시테이블로 사용
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)
if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")
key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])


# In[42]:


#집합 자료형
data = set([1,1,2,3,4,4,5])
print(data)

data = {1,1,2,3,4,4,5}
print(data)

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a | b)
print(a & b)
print(a - b)

data = set([1,2,3])
print(data)

data.add(4) #1개 추가
print(data)
data.update([5,6]) #여러개 추가
print(data)
data.remove(3) #제거
print(data)


# In[ ]:





# In[ ]:




