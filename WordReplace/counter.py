def count(words):
    """

    :param words: list of strings
    :return: list of integers
    """
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

if __name__ == "__main__":
    print(count(["gh", "tthd"]))