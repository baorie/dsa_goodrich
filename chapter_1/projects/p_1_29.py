def all_orders():
    # outputs all possible strings formed by characters in 'catdog' exactly once
    # 720 possible strings
    all_words = []
    chars = ["c", "a", "t", "d", "o", "g"]
    for i in range(len(chars)):
        # choose starting letter and pop into a new string
        first_chars = list(chars)
        pos_0 = chars[i]
        first_chars.remove(chars[i])
        for j in range(len(first_chars)):
           second_chars = list(first_chars)
           pos_1 = first_chars[j]
           second_chars.remove(first_chars[j])
           for k in range(len(second_chars)):
               third_chars = list(second_chars)
               pos_2 = second_chars[k]
               third_chars.remove(second_chars[k])
               for l in range(len(third_chars)):
                   fourth_chars = list(third_chars)
                   pos_3 = third_chars[l]
                   fourth_chars.remove(third_chars[l])
                   for m in range(len(fourth_chars)):
                       fifth_chars = list(fourth_chars)
                       pos_4 = fourth_chars[m]
                       fifth_chars.remove(fourth_chars[m])
                       for n in range(len(fifth_chars)):
                           sixth_chars = list(fifth_chars)
                           pos_5 = fifth_chars[n]
                           new_word = "".join([pos_0, pos_1, pos_2, pos_3, pos_4, pos_5])
                           all_words.append(new_word)                        
    print(len(all_words))
    print(all_words)
