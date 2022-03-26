
# # # Write a python program to print a 3x3 formatted matrix as shown below, using lists and nested loops.
# # # Make note of 2d array, loop/iteration and zero based counting.
# # # matrix = [ [1,2,3],[4,5,6],[7,8,9] ] #write a function to output the formatted matrix :
# # # 1 2 3
# # # 4 5 6
# # # 7 8 9

# # matrix = [ [1,2,3],[4,5,6],[7,8,9] ]

# # print each sublist in new row
# # for row in matrix:
# #   print (row, sep=',')
# # a = matrix[0
# # print(a)

# a = matrix[0][0], matrix[0][1], matrix[0][2]
# b = matrix[1][0], matrix[1][1], matrix[1][2]
# c = matrix[2][0], matrix[2][1], matrix[2][2]
# print(*a, sep=" ")
# print(*b, sep=" ")
# print(*c, sep=" ")



# swaps numbers regardless of value
def swap1(age1,age2):
  temp = age1
  age1 = age2
  age2 = temp
  print("Swap 1 Result:")
  return age1,age2
  
#returns numbers lowest to highest  
def swap2(a, b):
  if a > b:
    b, a = a, b
  print("Swap 2 Result:")
  return a, b

# returns numbers lowest to highest
def swap3(age1, age2):
  if age1 > age2:
    print ("Swap 3 Result:")
    return(age2, age1)
  else:
    print ("Swap 3 Result:")
    return(age1, age2)

# tests
print(16,20)
print(9.134,4)
print(swap1(16, 20))
print(swap1(9.134, 4))
print(swap2(16,20))
print(swap2(9.134, 4))
print(swap3(16,20))
print(swap3(9.134, 4))