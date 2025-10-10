# Задача: Напишите функцию, которая объединяет два отсортированных списка в один отсортированный.
# Пример: merge([1, 3, 5], [2, 4, 6]) → [1, 2, 3, 4, 5, 6]
def merge_sorted_lists(list1, list2):
    result=[]
    list1_index=0
    list2_index=0
    while list1_index<len(list1) and list2_index<len(list2):
        if list1[list1_index]<list2[list2_index]:
            result.append(list1[list1_index])
            list1_index+=1
        else
            result.append(list2[list2_index])
            list2_index+=1
    if list1_index=len(list1) and list2_index<len(list2):
        while list2_index<len(list2):
            result.append(list2[list2_index])
            list2_index+=1
    elif list2_index=len(list2) and list1_index<len(list1):
        while list1_index<len(list1):
            result.append(list1[list1_index])
            list1_index+=1
    return result