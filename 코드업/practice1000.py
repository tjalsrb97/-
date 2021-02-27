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
a = input()
if(a == "A"):
    print("best!!!")
elif(a == "B"):
    print("good!!")
elif(a == "C"):
    print("run!")
elif(a == "D"):
    print("slowly~")
else:
    print("what?")

