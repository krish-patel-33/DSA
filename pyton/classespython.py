# n = int(input("Enter the number"))

# isprime =  True

# if n < 2:
#     isprime = False

# else:
#     for i in range(2,n//2 + 1):
#         if n % i == 0:
#             isprime = False
#             break


# if isprime:
#     print()


# for num in range(2, 51):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")


# n = int(input("enter the number"))
# isprime = True

# if n < 2:
#     isprime = False
# else:
#     for i in range(2 , n // 2 + 1):
#         if n % i == 0:
#             isprime = False
#             break
# print(f"{n} is {'Prime' if isprime else 'not prime'}")


# n = int(input("enter the number "))
# count = 0 
# while n > 0:
#     n = n //10
#     count += 1 
# print(f"Number of digits : {count}")    

a, b = 48, 18

# Method 1: Using Euclidean algorithm
# x, y = a, b
# while y != 0:
#     x, y = y, x % y
# print(f"GCD of {a} and {b} = {x}")


# arr = [12,45,7,89,23,56]
# first = second = float('-inf')

# for num in arr:
#     if num > first:
#         second = first
#         first = num
#     elif num > second and num != first:
#         second = num  

# print(f"first: {first}, second: {second}")


# rev = 0

# while n>0:
#     digit  = n % 10
#     rev = rev *10 + digit
#     n = n // 10

# print(f"Reversed : {rev}")


# a,b = 0,1

# for _ in range(n):
#     print(a, end=" ")
#     a,b = b , a+b


# factorial = 1
# i =1

# while i<=n:
#     factorial = factorial * i
#     i = i + 1

# print(f"factorial of {n} = {factorial}")
