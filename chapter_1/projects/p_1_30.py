def stuff():
    #takes a positive integer greater than 2 as input
    #Writes out the number of times one must repeatedly divide this number by 2 before
    #getting a value less than 2
    num = int(input('Please input a value greater than 2: '))
    divcount = 0;
    if num > 2:
        while num > 2:
            num = num / 2
            divcount += 1
    print('It takes ' + str(divcount) + ' divisions to get to below 2.')
