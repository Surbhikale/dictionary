##three number are maximam find out##

#print("Enter any three numbers: ");
#num1 = input();
#if num1 == 'x':
#    exit();
#else:
#    num2 = input();
#    num3 = input();
#    number1 = int(num1);
#    number2 = int(num2);
#    maximam = number1;
#    count = 1;
#    if maximam < number2:
#        if number2 > number3:
#        else:
#            maximam = number3;
#    elif maximam < number3:
#        if number3 > number2:
#            maximam = number3;
#        else:
#            maximam = number2;
#    else:
#        maximam = number1;
#    if number1 == number2:
#        if number1 == number3:
#            count = 0;
#        print("All numbers are equal .");
#    else:
#        print("Largest of the given three numbers is",maximam);
####################################two number of largest###########################################
#print("Enter any two numbers: ");
#num1 = input();
#if num1 == 'x':
#    exit();
#else:
#    num2 = input();

#    number1 = int(num1);
#    number2 = int(num2);

#    largest = number1;
#    count = 1;
    #if largest < number2:

    #        largest = number2;

    #elif largest < number1:

    #        largest = number2;

    #else:
    #    largest = number1;
    #if number1 == number2:

    #        count = 0;
    #if count == 0:
    #    print("All numbers are equal to each other.",equal);
    #else:
    #    print("Largest of the given two numbers is",largest);
        #####################################fibonicce serice ################
import math    

def is_perfact(n):
    s = math.sqrt(n)
    s = int (s)
    return s*s ==n
def is_fibo(n):
    if  is_perfact(5*n*n+4)or is_perfact(5*n*n-4):
        print('%d is in fibonacci'%n)
    else:
        print('%d is not in fibonacci'%n)


a = int (input('enter the number:/n'))
is_fibo(a)
