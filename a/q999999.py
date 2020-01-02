# sequence of (string type) numbers into list (string type)
num1 = input('Enter bunch of numbers:')
num1_list = num1.split()

print(num1_list)

try_list = [1, 2, 3, 4]
print(try_list)

'''sequence of (string type) numbers into list (int type)'''
# Logic: using for
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
for i in range(0, n):
    lst_ele = int(input(i))
    lst.append(lst_ele)

print(lst)

'''sequence of (string type) numbers into list (int type)'''

# try block to handle the exception
try:
    my_list = []

    while True:
        my_list.append(int(input()))

    # if input is not-integer, just print the list
except:
    print(my_list)
