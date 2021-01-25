#!/usr/bin/env python
# coding: utf-8

# In[4]:


i = 1
result = 0

while i<=9:
    result += i
    i+=1
print(result)


# In[5]:


i = 1
result = 0

while i<=9:
    if i%2 == 1:
        result += i
    i+=1
print(result)


# In[6]:


result = 0

for i in range(1, 10):
    result += i
print(result)


# In[7]:


scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다.")


# In[8]:


scores = [90, 85, 77, 65, 97]
cheating_list = {2,4}

for i in range(5):
    if i+1 in cheating_list:
        continue #반복문의 처음으로 돌아간다.
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다.")


# In[10]:


for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i*j)
#print()


# In[14]:


def add(a, b):
    return a+b

print(add(3,7))


# In[15]:


def add(a, b):
    print('함수의 결과: ', a+b)
add(3, 7)
add(b = 3, a = 7) #매개변수 순서 달라도 상관없음


# In[16]:


a=0

def func():
    global a #함수 바깥에 선언된 변수를 바로 참조
    a+=1
    
for i in range(10):
    func()
    
print(a)


# In[18]:


#람다 표현식
def add(a, b):
    return a+b

print(add(3, 7))

print((lambda a, b: a+b)(3, 7))


# In[ ]:




