def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    # if len(first_string) == 0 or len(second_string) == 0:
    #     return False

    string1_list = list(first_string.lower())
    string2_list = list(second_string.lower())

    # print(string1_list)
    # print(string2_list)

    merge_sort(string1_list)
    merge_sort(string2_list)

    string1_ordenada = "".join(string1_list)
    string2_ordenada = "".join(string2_list)

    # print("entrei")

    sao_anagramas = string1_ordenada == string2_ordenada

    return tuple([string1_ordenada, string2_ordenada, sao_anagramas])


# print(is_anagram("", "alergia"))
# def is_anagram(first_string, second_string):
#     if len(first_string) != len(second_string):
#         return tuple([None, None, False])

#     string1_ordenada = sorted(first_string)
#     string2_ordenada = sorted(second_string)

#     sao_anagramas = string1_ordenada == string2_ordenada

#     return tuple([string1_ordenada, string2_ordenada, sao_anagramas])
