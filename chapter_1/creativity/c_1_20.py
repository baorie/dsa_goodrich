from random import randint

def my_shuffle(data):
    # randomly reorder elements using randint(a,b), a & b inclusive
    new_data = []
    pop_data = data
    while len(pop_data) > 0:
        rand = randint(0, len(pop_data)-1)
        new_data.append(pop_data.pop(rand))
    return new_data

