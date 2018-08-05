def remove_punc(string):
    cap_alpha = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    sm_alpha = [chr(j) for j in range(ord('a'), ord('z')+1)]
    merge_alpha = cap_alpha + sm_alpha
    merge_alpha.append(' ')
    return "".join([char for char in string if char in merge_alpha])
