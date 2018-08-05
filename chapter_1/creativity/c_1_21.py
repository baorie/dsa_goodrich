import sys

def reverse_lines():
    #reads lines from stdio until an EOFError is raised and then outputs those lines in reverse order
    fp = open('text_c_1_21.txt', 'w')
    try:
        data = input("Write some lines to be reversed:")
        fp.write(data)
    except EOFError:
        # populate a list line by line
        line_list = fp.readlines()
        fp.close()
        rev_list = line_list[::-1]
        print("Here is the reversed input: \n")
        print(rev_list)
        raise
