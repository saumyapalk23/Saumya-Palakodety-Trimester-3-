# class factors:
#     def __init__(self):
#         self.allfactors = []

#     def __call__(self,num):
#         for value in range(1, num + 1):
#             if num % value == 0:
#                 self.allfactors.append(value)
#         return self.allfactors

# def driver():
#     # Make a factors object
#     while True:
#         fact = factors()
#         n = input("Enter the number to find factors: ")
#         try:
#             n = int(n)
#             # Validate the value of n
#             if n < 2 or n > 99:
#                 raise ValueError
#             # Produces a list of factors for input
#             print(f"Factors of {n} are: ", fact(n))
#             break
#         except ValueError:
#             print(f'Positive integer number in range 2 to 99 is expected, got "{n}" Try again.')
            
            
# if __name__ == "__main__":
#     driver()
