
#custom print function
def custom_print(*n, sep, end):
    #puts the non-declared arg in a list
    items = [*n]

    #printing them in a for loop
    for i, j in enumerate(items):
        print(*n, sep=sep, end=end)
        break

#function called
custom_print("first", "word", sep = " ", end = ".")
