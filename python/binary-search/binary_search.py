def find(search_list, value):
    begin = 0
    end = len(search_list)
    done = 0
    while begin != end:
        test_index = (begin + end) >> 1
        if search_list[test_index] == value:
            return test_index
        elif search_list[test_index] > value:
            end = test_index
        else:
            begin = test_index + 1
    raise ValueError("value not in array")
