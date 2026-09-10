# x = lambda a,b : a + b
# print(x(5,7))

# def check_even_odd(num):
#     return "Even" if num % 2 == 0 else "Odd"
# print("Even/Odd:", check_even_odd(15))
# print("Even/Odd:", check_even_odd(20))

# def find_max(a,b,c):
#     return max(a,b,c)
# print('max:',find_max(22,87,90))

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result
# print(factorial(5))

# def count_vowels(text):
#     vowels= 'aeiouAEIOU'
#     count=0

#     for char in text:
#         if char in vowels:
#             count += 1
#     return count
# print('vowels count:', count_vowels('hello world'))

# def circle_area(radius):
#     pi=3.14
#     return pi*radius*radius
# print("Circle area:", circle_area(6))

# def is_prime(n):
#     if n <= 1:
#         return False
 
#     for i in range(2,n):
#         if n % i == 0:
#             return False
 
#     return True
# print("Prime Check:", is_prime(19))

# def reverse_string(text):
#      return text[::-1]
# print("Reverse String:", reverse_string("Python"))

def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A"
    elif 80 <= marks <= 89:
        return "B"
    elif 70 <= marks <= 79:
        return "C"
    elif 60 <= marks <= 69:
        return "D"
    else:
        return "F"
print("Grade:", calculate_grade(85))
