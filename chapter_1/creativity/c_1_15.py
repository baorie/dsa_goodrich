def unique_sequence(data):
    sort_data = sorted(data)
    unique_set = sorted(set(data))
    if sort_data == unique_set:
        print('Integers are distinct')
    else: 
        print('Integers aren\'t distinct')
