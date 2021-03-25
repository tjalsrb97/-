#1014
# a, b = input().split()
# print(b, a)

#1015
# n=float(input())
# print("%.2f" % n)

#1017
# n=int(input())
# print(n, n, n)

#1018
# a, b = input().split(":")
# print('%s:%s' %(a,b))

#1019
# y, m, d = input().split(".")
# print("%04d.%02d.%02d" %(int(y),int(m),int(d)))

#1020
# front, back = input().split("-")
# print(front+back)

#1021
# input1 = str(input())
# print(input1)

#1022
# import sys
# data = sys.stdin.readline().rstrip()
# print(data)

#6023
# data = input().split(':')
# print(data[1])

#6024
# sentence = input().split(' ')
# print(sentence[0]+sentence[1])

#6025
# a = input().split(' ')
# print(int(a[0])+int(a[1]))

#6026
# fn = input()
# sn = input()
# print(float(fn)+float(sn))

#6027
# a = input()
# n = int(a)
# print('%x' % n)

#6028
# a = input()
# n = int(a)
# print('%X' % n)

#6029
# a = input()
# n = int(a, 16)
# print('%o' % n)

#6030
# n = ord(input())
# print(n)

#6031
# c = int(input())
# print(chr(c))

#6032
# n=int(input())
# print(-n)

#6033
# n=ord(input())
# print(chr(int(n)+1))

#6034
# a, b = input().split(' ')
# print(int(a) - int(b))

#6035
# a, b = input().split(' ')
# print(float(a) * float(b))

#6036
# w, n = input().split(' ')
# print(w*int(n))

#6037
# n = input()
# s = input()
# print(int(n)*s)

#6038
# a, b = input().split(' ')
# print(int(a) ** int(b))

#6039
# a, b = input().split(' ')
# print(float(a) ** float(b))

#6040
# a, b = input().split(' ')
# print(int(a)//int(b))

#6041
# a, b = input().split(' ')
# print(int(a)%int(b))

#6042
# a = float(input())
# print(round(a, 2))

#6043
# a, b = input().split(' ')
# a1 = float(a)
# b1 = float(b)
# print('%.3f' %round(a1/b1, 3))

#6044
# a1, b1 = input().split(' ')
# a = int(a1)
# b = int(b1)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)
# print(round(a/b, 2))

#6045
# a, b, c = input().split(' ')
# m = int(a) + int(b) + int(c)
# print(m, round(m/3, 2))

#6046
# a = input()
# print(2*int(a))
# print(int(a)<<1)

#6047
# a, b = input().split(' ')
# a = int(a)
# b = int(b)
# print(a * 1<<b)

#6048
# a, b = input().split(' ')
# a = int(a)
# b = int(b)
# print(a<b)

#6049
# a, b = input().split(' ')
# a = int(a)
# b = int(b)
# print(a==b)

#6050
# a, b = input().split(' ')
# a = int(a)
# b = int(b)
# print(a<=b)

#6051
# a, b = input().split(' ')
# a = int(a)
# b = int(b)
# print(a!=b)

#6052
# a = int(input())
# print(bool(a))

#6053
# a = bool(int(input()))
# print(not a)

#6054
# a, b = input().split(' ')
# print(bool(int(a)) and bool(int(b)))

#6055
# a, b = input().split(' ')
# print(bool(int(a)) or bool(int(b)))

#6056
# a, b = input().split(' ')
# a = bool(int(a))
# b = bool(int(b))
# print((a and (not b)) or ((not a) and b))

#6057
# a, b = input().split(' ')
# a = bool(int(a))
# b = bool(int(b))
# print(not((a and (not b)) or ((not a) and b)))

#6058
# a, b = input().split(' ')
# a = bool(int(a))
# b = bool(int(b))
# print((not a) and (not b))

#6059
# a = int(input())
# print(~a)

#6060
# a, b = input().split(' ')
# a = int(a)
# b = int(b)
# print(a&b)

#6061
# a, b = input().split(' ')
# a = int(a)
# b = int(b)
# print(a|b)

#6062
# a, b = input().split(' ')
# a = int(a)
# b = int(b)
# print(a^b)

#6063
# a, b = input().split(' ')
# a = int(a)
# b = int(b)
# print(a if (a>=b) else b)

#6064
# a, b, c = input().split(' ')
# a = int(a)
# b = int(b)
# c = int(c)
# print((a if (a<b) else b) if ((a if (a<b) else b)<c) else c)

#6065
# a, b, c = input().split(' ')
# a = int(a)
# b = int(b)
# c = int(c)
# if(a%2==0): print(a)
# if(b%2==0): print(b)
# if(c%2==0): print(c)

#6066
# a, b, c = input().split(' ')
# a = int(a)
# b = int(b)
# c = int(c)
# if(a%2==0): print("even") 
# else: print("odd") 
# if(b%2==0): print("even")
# else: print("odd")
# if(c%2==0): print("even")
# else: print("odd")

#6067
# a = int(input())
# if a<0:
#     if a%2==0:
#         print("A")
#     else:
#         print("B")
# else:
#     if a%2==0:
#         print("C")
#     else:
#         print("D")

#6068
# a = int(input())
# if (90 <= a) & (a <= 100):
#     print("A")
# elif (70 <= a) & (a <= 89):
#     print("B")
# elif (40 <= a) & (a <= 69):
#     print("C")
# else:
#     print("D")

#6069
# a = input()
# if(a == "A"):
#     print("best!!!")
# elif(a == "B"):
#     print("good!!")
# elif(a == "C"):
#     print("run!")
# elif(a == "D"):
#     print("slowly~")
# else:
#     print("what?")

#6070
# a = int(input())
# if(a//3==1): print("spring")
# elif(a//3==2):print("summer")
# elif(a//3==3):print("fall")
# elif((a//3==4) | (a//3==0)): print("winter")

#6071
# while(1):
#     a = int(input())
#     if(a==0): break
#     else: print(a)

#6072
# a = int(input())
# while(a!=0):
#     print(a)
#     a=a-1

#6073
# a = int(input())
# while(a!=0):
#     print(a-1)
#     a=a-1

#6074
# x = ord(input())
# temp = ord("a")
# while(x>=temp):
#     print(chr(temp), end=" ")
#     temp=temp+1

#6075
# a = int(input())
# temp=0
# while(temp!=a+1):
#     print(temp)
#     temp=temp+1

#6076
# a = int(input())
# for i in range(a+1):
#     print(i)

#6077
# a = int(input())
# temp = 0
# for i in range(1, a+1):
#     if i%2 == 0:
#        temp += i
# print(temp) 

#6078
# while(1):
#     a = input()
#     if(a == "q"):
#         print(a)
#         break
#     else:
#         print(a)
#         continue

#6079
# a = int(input())
# sum = 0
# for i in range(1, 1000):
#     if(a<=sum): 
#         print(i-1)
#         break
#     else: 
#         sum+=i
#         continue

#6080
# n, m = input().split()
# n = int(n)
# m = int(m)
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i, j)

#6081
# a = input()
# a = int(a, 16)
# for i in range(1, int('F', 16)+1):
#     print('%X'%a, '*%X'%i, '=%X'%(a*i), sep='')

#6082
# a = int(input())
# for i in range(1, a+1):
#     if i%10==3:
#         print("X", end=' ')
#     elif i%10==6:
#         print("X", end=' ')
#     elif i%10==9:
#         print("X", end=' ')
#     else:
#         print(i, end=' ')

#6083
# r, g, b = input().split(' ')
# r = int(r)
# g = int(g)
# b = int(b)
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(i, j, k)
# print(r*g*b)

#6084
# h, b, c, s = input().split(' ')
# h = int(h)
# b = int(b)
# c = int(c)
# s = int(s)
# print(round(float((h*b*c*s)/(8*1024*1024)), 1), end='')
# print(" MB")

#6085
# w, h, b = input().split(' ')
# w = int(w)
# h = int(h)
# b = int(b)
# print('%.2f' %round(float((w*h*b)/(8*1024*1024)), 2), end='')
# print(" MB")

#6086
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum += i
#     if(n<=sum):
#         print(sum)
#         break

#6087
# n = int(input())
# for i in range(1, n+1):
#     if(i%3==0):
#         continue
#     else:
#         print(i, end=' ') 

#6088
# a, d, n = input().split(' ')
# a = int(a)
# d = int(d)
# n = int(n)
# sum = 0
# for i in range(1, n, 1):
#     sum = a + i*d
# print(sum)

#6089
# a, d, n = input().split(' ')
# a = int(a)
# d = int(d)
# n = int(n)
# mul = a
# for i in range(1, n):
#     mul = mul*d
# print(mul)

#6090
# a, b, c, d = input().split(' ')
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# for i in range(1, d):
#     a = a * b + c
# print(a)

#6091
# person1, person2, person3 = input().split(' ')
# person1 = int(person1)
# person2 = int(person2)
# person3 = int(person3)
# day = 1
# while day%person1!=0 or day%person2!=0 or day%person3!=0:
#     if person1 > 100 or person2 > 100 or person3 > 100:
#         print("number over 100")
#         break
#     else:
#         day += 1

# if day != 1:
#     print(day)

#6092
# num = int(input())
# attend = list(map(int, input().split(' ')))

# for i in range(num):
#     attend[i] = int(attend[i])

# student = []
# for i in range(24):
#     student.append(0)

# for i in range(num):
#     student[attend[i]] += 1

# for i in range(1, 24):
#     print(student[i], end=' ')

#6093
# num = int(input())
# attend = input().split(' ')

# for i in range(num):
#     attend[i] = int(attend[i])

# for i in range(num-1, -1, -1):
#     print(attend[i], end=' ')

#6094
# num = int(input())
# attend = input().split(' ')

# for i in range(num):
#     attend[i] = int(attend[i])

# low_num = attend[0]
# for i in range(num):
#     if low_num>attend[i]:
#         low_num=attend[i]
# print(low_num) 

#6095
num = int(input())
baduk = [[0 for _ in range(20)] for _ in range(20)]
for _ in range(num):
    position = input().split(' ') 
    position[0] = int(position[0])
    position[1] = int(position[1])
    for i in range(20):
        for j in range(20):
            if (i==position[0]) and (j==position[1]):
                baduk[i][j]=1
            else:
                continue

for i in range(1, 20):
    for j in range(1, 20):
        print(baduk[i][j], end=' ')
    print()

        




