#enlarge function
def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n *100

# if in global scope, this will mess up our
# ability to import other functions from 
# this file so we need to next it under the main conditional

# x = int(input("Please Choose a number(like 5): "))
# result = enlarge(x)
# print(result)

if __name__ == "__main__":
    # only invoke code below if running module
    # from another file
    x = int(input("Please Choose a number(like 5): "))
    result = enlarge(x)
    print(result) 