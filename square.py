# print("Square")
# n = int(input("Enter how many rows"))
# for i in range(1,n,1):
#     print("* "*n)

# for row in range(1,n+1):
#      for col in range(1,n+1):
#         if row==1 or row==n or col==1 or col==n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#      print()

n = int(input("triangle rows"))
for i in range(n):
    for x in range(n-i-1):
        # print(x, i)
        print(" ",end="")
    for x in range(i+1):
        print("*",end=" ")
    print()

