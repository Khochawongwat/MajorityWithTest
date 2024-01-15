def majority(L: list):
    
    #O(1)
    if len(L) == 0:
        return None
    count_dict = {}

    #O(n)
    for element in L:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1

    #O(n)
    majority_element = max(count_dict, key=count_dict.get)
    
    if count_dict[majority_element] > len(L) // 2:
        return majority_element
    else:
        return None