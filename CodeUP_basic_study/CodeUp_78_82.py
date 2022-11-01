#6078 #78
# while True: 
#     a = input()
    
#     if a == 'q':
#         print(a)
#         break
#     else:
#         print(a)

#6079 #79
# a = int(input())
# number = 0
# sum = 0

# while True:
#     number += 1
#     sum += number
#     if sum >= a:
#         break
    
# print(number)

#6080 #80
# a, b = map(int, input().split())

# for i in range(1, a+1):
#     for j in range(1, b+1):
#         print(f"{i} {j}")

#6081 #81
# a = input()
# a = int(a,16)

# for i in range(1,16):
#     print('%X'%a, '*%X'%i, '=%X'%(a*i), sep="")

#6082 #82
# a = int(input())

# for i in range(1, a+1):
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         print("X", end =" ")
#     else:
#         print(i, end=" ")

