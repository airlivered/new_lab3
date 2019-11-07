def max_min_index(lengths, max_or_min):
    """
    
    :param lengths: list
    :param max_or_min: str
    :return: list
    """""
    if max_or_min == "max":
        max_indeces = []
        for index in range(len(lengths)):
            if lengths[index] == max(lengths):
                max_indeces.append(index)
        return max_indeces
    if max_or_min == "min":
        min_indeces = []
        for index in range(len(lengths)):
            if lengths[index] == min(lengths):
                min_indeces.append(index)
        return min_indeces
def max_min_value(lengths, max_or_min):
    """
    
    :param lengths: list
    :param max_or_min: str
    :return: integer
    """""
    if max_or_min == "max":
        return max(lengths)
    if max_or_min == "min":
        return min(lengths)
if __name__ == "__main__":
    test = [4, 1, 12, 12, 1, 1, 1, 1]
    print(max_min_index(test, "min"))