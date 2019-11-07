from WordReplace import separator, finder, is_that_many, swapper, counter

sentence = "It's_dangerous_to_go_alone"
character = "_"
needed_for_maximum = 1
needed_for_minimum = 2
print(sentence)

words = separator.separate(sentence, character)
lengths = counter.count(words)
print(lengths)
#max_value, min_value = finder.max_min_value(length, "max"), finder.max_min_value(length, "min")

max_indeces, min_indeces = finder.max_min_index(lengths, "max"), finder.max_min_index(lengths, "min")
print(max_indeces, min_indeces)
if not (is_that_many.check(needed_for_maximum, len(max_indeces)) and is_that_many.check(needed_for_minimum, len(min_indeces))):
    print("Starting conditions were not satisfied")
    quit()

if needed_for_maximum == 1 and needed_for_minimum == 1:
    words = swapper.swap(words, max_indeces[0], min_indeces[0])
else: swapper.multi_swap(max_indeces, min_indeces, words)

sentence = character.join(words)
print(sentence)
