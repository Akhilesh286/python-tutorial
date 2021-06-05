def great_user1 ():
    print ('hai')
    print ('hello')


print ('hello hai')
#great_user()
"with argument"
def great_user (name):
    print ('hai')
    print (f'hello  {name}')

great_user('akhilesh')

"key word argument"


def great_user (first_name,last_name):
    print ('hai')
    print (f'hello  {  first_name} {last_name}')

great_user('esh','akhil')
great_user(last_name='esh',first_name="akhil")

"retorn"
def squar (number):
    return number * number


result=squar(3)
print (result)
print (squar(4))


















