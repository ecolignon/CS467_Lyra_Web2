"""
********************************************************************************
* Description: print_arguments function
********************************************************************************
"""

def print_arguments(arguments):
    print("{} arguments provided on command line".format(len(arguments)))
    for x in range(len(arguments)):
        print("Argument {}: {}".format(x, arguments[x]))

"""
********************************************************************************
* Description: check_argument_total function
********************************************************************************
"""

def confirm_total(arguments):
    if len(arguments) < 3:
        print("Too few arguments")
        exit(1)
    elif len(arguments) > 3:
        print("Too many arguments")
        exit(1)
    else:
        print("Correct number of arguments")

"""
********************************************************************************
* Description: confirm_search_type function
********************************************************************************
"""

def confirm_search_type(search_type):
    if search_type != "breadth" and search_type != "depth":
        print("Search type is not valid")
        print("Search type must be breadth-first or depth-first")
        exit(1)
    else:
        if search_type == 'breadth':
            search = "Breadth-First"
        else:
            search = "Depth-First"
        print("Using {} Search Method".format(search))

"""
********************************************************************************
* Description: confirm_limit function
********************************************************************************
"""

def confirm_limit(number):
    print(number)
    try:
        limit = int(number)
    except ValueError:
        print("Search Limit needs to be a numeric value")
        exit(1)
    if int(number) <= 0:
        print("Search Limit needs to be a positive numeric value")
        exit(1)

"""
********************************************************************************
* Description: confirm_keyword function
********************************************************************************
"""

def confirm_keyword(keyword):
    print("Need to implement keyword confirmation")
