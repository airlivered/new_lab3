def swap(words, first, second):
    """

    :param words: string
    :param first: integer
    :param second: integer
    :return: list
    """
    words[first], words[second] = words[second], words[first]
    return words
def multi_swap(max_indeces, min_indeces, words):
    counter = 1
    while counter <= min([len(max_indeces), len(min_indeces)]):
        max_index = int(input("Of maximum indeces, input it's index in a given list:"))
        min_index = int(input("Of minimum indeces, input it's index in a given list:"))
        words = swap(words, max_indeces[max_index], min_indeces[min_index])
        counter += 1
    return words

if __name__ == '__main__':
    nums = [1, 2, 5, 7]
    nums = swap(nums,0, 3)
    print(nums)
    print(multi_swap([0, 3], [1, 2], nums))