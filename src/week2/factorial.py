# class factorial:
#   def _call_(self, (n-1)):
#   obj1 = factorial(null)
# print obj1(n)

# n = int(input("Enter a number:"))

# obj = Factorial()
# x = obj.factorials(n)
# print("Factorial is:", x)

# #   def factorial(n*self(n-1)):
# #     print("Factorial is"+ self.n*self(n-1))

# # obj = factorial
# class factorial:
# def recur_factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * recur_factorial(n-1)

# num = int(input("Enter a number for factorial: "))
#     # check if the number is negative

# # if num < 0:
# #   print("Sorry, factorial does not exist for negative numbers")
# # else:
# #   print("The factorial of", num, "is", recur_factorial(num))


    
# class Factorial:
#     def factorials(self, n):
#         x = 1
#         for i in range(1, n + 1):
#             x = x * i
#         return x

# n = int(input("Enter a number:"))

# obj = Factorial()
# x = obj.factorials(n)
# print("Factorial is:", x)

def driver():
  class factorials:
    def __init__(self):
      self.fact = [1]
    def __call__(self,n):
      if n < len(self.fact):
        return 1
      else:
        fact_number = n * self(n-1)
        self.fact.append(fact_number)
      return self.fact[n]
    factorial_of_n = factorials()
    n = int(input("Value for n: "))
    print(factorial_of_n(n))

