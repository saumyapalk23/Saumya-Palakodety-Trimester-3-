Family = []
# List with dictionary records placed in a list
Family.append({
               "Mom": "Kalpana",  
               "Dad": "Ravi",  
               "Children": ["Saumya","Shreya"],
               "Residence": "San Diego" , 
               "Population":"4" 
              })
# Family.append({
#               "Pets": "None",  
#               "Near_Parks": "Trent",  
#               "DOBs": ["August 26", "September 28", "April 5", "November 21"],
#               "Cousins": ["Siva","Harini", "Pranav", "Nithya"],  
#               "Emails":["saumyp3@gmail.com", "ravips1@gmail.com", "k_palakodety@yahoo.com","shreya.palakodety@gmail.com"]  
#               })

# print (Family)

def print_data(n):
    print(Family[n]["Mom"], Family[n]["Dad"]) 
    print(Family[n]["Children"])
    print(Family[n]["Residence"])
    print(Family[n]["Population"])
    # print(Family[n]["Pets"])  
    # print(Family[n]["Near_Parks"])
    # print(Family[n]["DOBs"])
    # print(Family[n]["Cousins"])
    # print(Family[n]["Emails"])
    print()

 
def for_loop():
  for data in Family:
    print(data)
  return
# for_loop(a,b)

def while_loop(n):
  while n < len(Family):
        print_data(n)
        n += 1
  return
# while_loop(a,b)

def recursive_loop(n):
  if n < len(Family):
        print_data(n)
        recursive_loop(n + 1)
  return
# recursive_loop(0,a,b)

def driver():
  #a = input("Enter key: " )
  #b = input("Enter value: " )
  for_loop()
  while_loop(0)
  recursive_loop(0)

