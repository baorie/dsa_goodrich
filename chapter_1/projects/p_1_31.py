def make_change():
    #should take two numbers as input: amount charged & amount given
    #return the number of each kind of bill and coin to give back
    #use as few bills and coins as possible
    num_100 = 0
    num_50 = 0
    num_20 = 0
    num_10 = 0
    num_5 = 0
    num_1 = 0
    num_q = 0 #quarters
    num_d = 0 #dimes
    num_n = 0 #nickels
    num_p = 0 #pennies
    charged = float(input("How much was the purchase?: "))
    given = float(input("How much did you give?: "))
    diff = given - charged
    if diff == 0:
        print("You gave exact change!")
    elif diff < 0:
        print("You didnt give enough!")
    else:
        print("Your change is " + str(diff))
        temp = diff
        while(temp > 0):
            if (temp // 100 != 0):
                num_100 = temp // 100
                temp = temp - num_100*100
            elif (temp // 50 != 0):
                num_50 = temp // 50
                temp = temp - num_50*50
            elif (temp // 20 != 0):
                num_20 = temp // 20
                temp = temp - num_20*20
            elif (temp // 10 != 0):
                num_10 = temp // 10
                temp = temp - num_10*10
            elif (temp // 5 != 0):
                num_5 = temp // 5
                temp = temp - num_5*5
            elif (temp // 1 != 0):
                num_1 = temp // 1
                temp = temp - num_1*1
        print("Your change is $" + str(diff) + ". That's :")
        print(str(num_100) + " $100 bills")
        print(str(num_50) + " $50 bills")
        print(str(num_20) + " $20 bills")
        print(str(num_10) + " $10 bills")
        print(str(num_5) + " $5 bills")
        print(str(num_1) + " $1 bills")
        print(str(num_q) + " quarters")
        print(str(num_d) + " dimes")
        print(str(num_n) + " nickels")
        print(str(num_p) + "pennies")
if __name__ == '__main__':
    make_change()
