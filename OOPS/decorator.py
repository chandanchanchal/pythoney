#decorator_definition
def decorator_function(main_function):
    #inner_decorator
    def inner_decorator():
        print("Decorator Function Called")
        main_function()

    return inner_decorator

#calling_decorator
@decorator_function
#fun_finds_division_of_number
def main_function():
    print("Normal Function Called")

#calling_normal_function
main_function()

#Output
#Decorator Function Called
#Normal Function Called
