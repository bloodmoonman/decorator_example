def decorated(this_will_get_passed):
    def wrapper():
        print('Painter: ')  #this is the step where decorator adds another functionality to passed function. In this case it is adding a text, with print statement.
        this_will_get_passed() #We are taking a function as a parameter in decorated function then calling that function on this line
    return wrapper
    

def name():
    print('Aykan')


print("---------------")
print(type(name))
lets_try_it = decorated(name) #passing name function into decorated function here and assigning this object to a lets_try_it variable
lets_try_it() # this is also function
print("---------------")
print(type(lets_try_it))


