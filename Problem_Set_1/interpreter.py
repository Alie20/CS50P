equation = input('enter your equation')
parameter = equation.split(' ')
if (parameter[1] =='+'):
    print(float(parameter[0])+float(parameter[2]))
elif (parameter[1] =='-'):
    print(float(parameter[0])-float(parameter[2]))
elif (parameter[1] =='*'):
    print(float(parameter[0])*float(parameter[2]))
elif (parameter[1] =='/'):
    print(float(parameter[0])/float(parameter[2]))
