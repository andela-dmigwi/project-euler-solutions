# Solution 2
# def fib(num, l=[]):
#   a=b=1
#   while(True):
#     a+=b
#     if a % 2 == 0:
#       l.append(a)
#     a,b=b,a
#     if a >= num:
#       break
#   return l

# print(sum(fib(4000000)))


#  Solution 3
# import math


# def factors(num):
#     factors_list = []
#     for value in range(2, math.ceil(math.sqrt(num))):
#         if not num % value:
#             factors_list.append(value)
#             factors_list.append(num / value)
#     return factors_list


# def prime_factors():
#     facts = factors(600851475143)
#     primes = []
#     for num in facts:
#         for val in range(2, math.ceil(math.sqrt(num))):
#             if not num % val:
#                 break
#         else:
#             primes.append(num)
#     return primes


# print(prime_factors())

# Solution 4
palindrome = []
for val in range(2, 1000)[::-1]:
    for value in range(2, val)[::-1]:
        str_int = str(val * value)
        if list(str_int) == list(str_int)[::-1]:
            palindrome.append((val * value))
print (max(palindrome))
