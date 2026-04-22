# text=input("enter a test: ")
# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("not a palindrome")

n=int(input("enter number of terms: "))
a=0
b=1
print("fibonoci series")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c