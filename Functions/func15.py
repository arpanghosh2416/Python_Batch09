# Recursion  with Lists:

# Sum of all elements in a list using recursion

def sum_list(num):
  if len(num) == 0: #Base case
    return 0 #Breaking condition of recursion
  else:
    # print("Current list:", num)
    # print("Current sum:", num[0])
    # print("Remaining list:", num[1:])
    # print("Testing...",sum_list(num[1:]))
    sum= num[0] + sum_list(num[1:]) #Recursive case
    # print(sum)
    return sum

lst = [1,2,3,4,5]

print(sum_list(lst))


# max value in a list using recursion
def find_max(num):
  if len(num) == 1: #Base case
    return num[0] #Breaking condition of recursion
  else:
    # print("Current list:", num)
    # print("Current max:", num[0])
    # print("Remaining list:", num[1:])
    # print("Testing...",find_max(num[1:]))
    # max_value= max(num[0], find_max(num[1:])) #Recursive case
    max_value = num[0] if num[0] > find_max(num[1:]) else find_max(num[1:])

    # print(max_value)
    return max_value


lst = [1,2,3,4,5]
print(find_max(lst))



