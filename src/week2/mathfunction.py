
# Function to find prime numbers in OOP

#test values
min = 2
max = 200

class primeNumbers:
    def __init__(self):
        pass
    def __call__(self, min, max):
      print("Here are OOP results, listing all prime numbers from 2 to 200: ")
      for Number in range(min, max + 1):
              count = 0
              for i in range(2, (Number // 2 + 1)):
                  if (Number % i == 0):
                      count = count + 1
                      break
              if (count == 0 and Number != 1):
                  print(" %d" % Number, end='  ')

min = 2
max = 200

def primenumbers (min, max):
    for Number in range(min, max + 1):
        count = 0
        for i in range(2, (Number // 2 + 1)):
            if (Number % i == 0):
                count = count + 1
                break
        if (count == 0 and Number != 1):
            print(" %d" % Number, end='  ')
    print()
  
def primes():
  print("Imperative results:") 
  # primenumbers(min, max + 1)

# primes()

def driver():
  primes_of = primeNumbers() # object instantiation and run __init__ method
  print(primes_of(min, max)) # object running __call__ method
  primes()
  primenumbers(min, max + 1)




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
