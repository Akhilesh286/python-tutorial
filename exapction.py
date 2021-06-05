try :
    age = int(input('age'))
    incom = 2000
    risk = incom / age
    print (age)
except ValueError:
    print ('value error')
except ZeroDivisionError:
    print ('zero no find')
