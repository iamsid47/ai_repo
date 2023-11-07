

unsorted_list = [5, 6 , 7 , 5, 6, 3]
sorted_list = []

def SelectionSort(unsorted_list: list, sorted_list: list) -> list:
    min_val = unsorted_list[0]
    for num in unsorted_list:
        if num < min_val:
            min_val = num
    
    sorted_list.append(min_val)
    unsorted_list.remove(min_val)
    if len(unsorted_list) == 0:
        return sorted_list
    SelectionSort(unsorted_list, sorted_list)
    return sorted_list

print(SelectionSort(unsorted_list, sorted_list))

