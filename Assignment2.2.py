var = 0
try:
    var = int(input("Enter the number to print number of stars: "))
except:
    print("Please enter an integer. Exiting now. Please re-run")
for i in range(1,var+1):
    print ('*' * i)
    if (i == var):
        for j in range(var-1,0,-1):
            print ('*' * j)
