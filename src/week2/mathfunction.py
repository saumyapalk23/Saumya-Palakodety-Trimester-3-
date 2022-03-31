# # Function to find prime numbers in imperative

# #test values
# min = 1
# max = 11

# def findprimes(min, max):
#     for Number in range(min, max + 1):
#         count = 0
#         for i in range(2, (Number // 2 + 1)):
#             if (Number % i == 0):
#                 count = count + 1
#                 break
#         if (count == 0 and Number != 1):
#             print(" %d" % Number, end='  ')
#     print()
# def primes():
#   print("Imperative results:") 
#   findprimes(min, max + 1)

# primes()

# Function to find prime numbers in OOP

#test values
min = 2
max = 200

class primeNumbers:
    def __init__(self):
        pass
    def __call__(self, min, max):
      print("Here are OOP results:")
      for Number in range(min, max + 1):
              count = 0
              for i in range(2, (Number // 2 + 1)):
                  if (Number % i == 0):
                      count = count + 1
                      break
              if (count == 0 and Number != 1):
                  print(" %d" % Number, end='  ')

def driver():
  primes_of = primeNumbers() # object instantiation and run __init__ method
  print(primes_of(min, max)) # object running __call__ method



# # Math functions using classes called from Menuyc.py

# # Find Factors of a Number using classes
# class factors:
#     def __init__(self):
#         self.totalfac = []

#     def __call__(self,num):
#       for value in range(1, num + 1):
#         if num % value == 0:
#           self.totalfac.append(value)
#       return self.totalfac
          
#     # # def tester():
#     # #   facto_of = factors()
#     # #   while True:
#     # #     fact = factors()
#     #     n = input("Enter the number to find factors: ")
#     #     try:
#     #       n = int(n)
#     #       # Validate the value of n
#     #       if n < 2 or n > 99:
#     #         raise ValueError
#     #         # Produces a list of factors for input
#     #         print(f"Factors of {n} are: ", fact(n))
#     #         break
#     #     except ValueError:
#     #       print(f'Positive integer number in range 2 to 99 is expected, got "{n}" Try again.')
#     #       if __name__ == "__main__":
#     #         tester()




# #             # print("{0}".format(value), end=" ")
# # def factors():
# #     print("hello from factors")
# #     num = int(input("Enter any Number to find its factors: "))
# #     (num)



# # class factors:
# #   def findFactors(number):
# #       print("Factors of a Given Number {0} are:".format(number))
# #       for value in range(1, number + 1):
# #           if number % value == 0:
# #               print("{0}".format(value), end=" ")
# #       print()
# # def factors():
# #     print("hello from factors")
# #     num = int(input("Enter any Number to find its factors: "))
# #     findFactors(num)



# # class factorials:
# #   def __init__(self):
# #     self.factorial1 = [1]
# #   def __call__(self,n):
# #     if n < len(self.factorial1):
# #       return 1
# #     else:
# #       fact_number = n * self(n-1)
# #       self.factorial1.append(fact_number)
# #     return self.factorial1[n]
# # factorial_of_n = factorials()
# # n = int(input("Value for n: "))
# # print(factorial_of_n(n))

  
# #     def do_add(self):

# #       self.sum = sum(self.any_list)

# # create_sum = ChangeList(my_list)

# # create_sum.do_add()

# # print(num)

# # class Factors():
# # def findFactors(number):
# #     print("Factors of a Given Number {0} are:".format(number))
# #     for value in range(1, number + 1):
# #         if number % value == 0:
# #             print("{0}".format(value), end=" ")
# #     print()

# # def factors():
# #     print("hello from factors")
# #     num = int(input("Enter any Number to find its factors: "))
    
# # return findFactors(num)

# # def tester():
# #     num = int(input("Enter a number for factorial: "))
# #     # check if the number is negative
# #     if num < 0:
# #         print("Sorry, factorial does not exist for negative numbers")
# #     else:
# #         print("The factorial of", num, "is", recur_factorial(num))










# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age

# # p1 = Person("John", 36)

# # def myfunc(self):
# #     print("Hello my name is " + self.name)

# # print(p1.name)
# # print(p1.age)

# # this is test driver or code that plays when executed directly, versus import which will not run these statements

# # p1.myfunc()


# # class factorial:
# #     def __init__(self):
# #         self.factorial = [0, 1]
# #     def __call__(self, n):
# #       if n == 1 or n == 0:
# #           return 1
# #       else:
# #           return n * self.factorial(n-1)



# # class ChangeList(object):

# #     def __init__(self, any_list):

# #         self.any_list = any_list

# #     def do_add(self):

# #       self.sum = sum(self.any_list)

# # create_sum = ChangeList(my_list)

# # create_sum.do_add()

# # print(create_sum.sum)




# # #jliang@ucsd.edu


# # # 6195388085
