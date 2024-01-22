# make a def function
def half_tree(rows):
    # make a for loop
    for counts in range(rows, 0, -1):
        print('*' * counts)

# run the program
length = 5
print(half_tree(length))