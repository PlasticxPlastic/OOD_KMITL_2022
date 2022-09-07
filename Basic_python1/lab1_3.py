def f():
    print(" *** Summation of each digit ***")
    number = (input("Enter a positive number : "))
    s = 0
    if(len(number)<=30):
        for i in range(len(number)):
            s = s+(int(number)%10)
            number = int(number)//10
    print("Summation of each digit = ",s)
    

f()