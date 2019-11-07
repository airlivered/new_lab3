def separate(sentence, character):
    """

    :param sentence: string
    :param character: string char
    :return:
    """
    words = sentence.split(character)
    return words

if __name__ == "__main__":
    print(separate("Oh my"," "))