# n=int(input("Enter a number:"))
# a=int(input("Enter 1 to "))
# for i in range(1,n+1,1):
#     print(i,end=',')
#     n=int(input("Enter a number:"))
# for i in range(1,n+1,1):
#     print(i)
try: 
 num=int(input())
 a=[3,6]
 print(a[num])
except IndexError:
    print("index Error")
except ValueError:
    print("Invalid Input")
    #finally always executes in the code whether there is a error in a code or not.
finally :
    print("i am always executed")