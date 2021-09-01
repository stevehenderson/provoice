from textstat.textstat import textstat
# if __name__ == '__main__':
#     test_data = """Playing games has always been thought to be etc.."""
#
# print(textstat.flesch_reading_ease(test_data))
# print(textstat.smog_index(test_data))



test_data = (
    "Playing games has always been thought to be important to "
    "the development of well-balanced and creative children; "
    "however, what part, if any, they should play in the lives "
    "of adults has never been researched that deeply. I believe "
    "that playing games is every bit as important for adults "
    "as for children. Not only is taking time out to play games "
    "with our children and other adults valuable to building "
    "interpersonal relationships but is also a wonderful way "
    "to release built up tension."
)

# print(textstat.flesch_reading_ease(test_data))
#
# print(textstat.flesch_kincaid_grade(test_data))
# >>> textstat.smog_index(test_data)
# >>> textstat.coleman_liau_index(test_data)
# >>> textstat.automated_readability_index(test_data)
# >>> textstat.dale_chall_readability_score(test_data)
# print(textstat.difficult_words(test_data))
# >>> textstat.linsear_write_formula(test_data)
# >>> textstat.gunning_fog(test_data)
# >>> textstat.text_standard(test_data)
# >>> textstat.fernandez_huerta(test_data)
# >>> textstat.szigriszt_pazos(test_data)
# >>> textstat.gutierrez_polini(test_data)
# >>> textstat.crawford(test_data)
# >>> textstat.gulpease_index(test_data)
# >>> textstat.osman(test_data)


# --------- attempt 1 using flesch_reading_ease -------#
# flesch_reading_ease notes: works but returns same value for a lot of words,
# need something a little more 'picky' for individual words
"""test_data2 = test_data.split(" ")

highest_word = []
new_word = ""
hi_score = 0

for word in test_data2:
    new_word = word
    wordscore = textstat.flesch_reading_ease(new_word)
    print("temp wordscore is {}".format(wordscore))
    if wordscore >= hi_score:
        hi_score = wordscore
        highest_word = []
        highest_word.append(word)
    new_word = ""
    print("hi score is {}".format(hi_score))
    # input()

print(new_word)
print(hi_score)
print(highest_word)"""

test_data2 = test_data.split(" ")

highest_word = []
new_word = ""
hi_score = 0

for word in test_data2:
    new_word = word
    wordscore = textstat.difficult_words(new_word)
    print("temp wordscore is {}".format(wordscore))
    if wordscore >= hi_score:
        hi_score = wordscore
        highest_word = []
        highest_word.append(word)
    new_word = ""
    print("hi score is {}".format(hi_score))
    # input()

print(new_word)
print(hi_score)
print(highest_word)

print(textstat.difficult_words_list(test_data))