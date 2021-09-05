import requests
from textstat.textstat import textstat
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

test_data = ("this is a sentence with difficult words like Oregon")

test_data2 = test_data.split(" ")

highest_word = []
new_word = ""
hi_score = 0

for word in test_data2:
    new_word = word.lower()
    wordscore = textstat.difficult_words(new_word)
    if wordscore >= hi_score:
        hi_score = wordscore
        highest_word = new_word


print("Chosen word is {}".format(highest_word))
print()
print("-" * 40)

#url = 'https://en.wikipedia.org/w/api.php?action=opensearch&search=oregon&limit=20&namespace=0&format=json'
url = 'https://en.wikipedia.org/w/api.php'

params = dict(
    action='opensearch',
    search=highest_word,
    limit='20',
    namespace='0',
    format = 'json'
)

resp = requests.get(url=url, params=params)
data = resp.json()
# print(data)
# print(type(data))

# for item in data:
# print(item)

list1 = data[1]

wiki_hi_score = 0
i = 0
wiki_search_index = None
for item in list1:
    # print(item)
    item_score = textstat.coleman_liau_index(item)
    print("item name is {}, item score is {}".format(item, item_score))
    if item_score > wiki_hi_score:
        wiki_hi_score = item_score
        winning_wiki_search = item
        wiki_search_index = i
    i = i + 1
print("Winning wiki search term is {}".format(winning_wiki_search))

list3 = data[3]
winning_url = list3[wiki_search_index]

print("Heading to get {}".format(winning_url))

resp = requests.get(url=winning_url)

# print(resp.text)
# TODO fix this so that url is not hard coded...
source = urlopen('https://en.wikipedia.org/wiki/Oregon_Shakespeare_Festival').read()

soup = BeautifulSoup(source)


# Extract the plain text content from paragraphs
paras = []
for paragraph in soup.find_all('p'):
    paras.append(str(paragraph.text))
# for paraE in paras:
#     print(paraE)
heads = []
for head in soup.find_all('span', attrs={'mw-headline'}):
    heads.append(str(head.text))
# for heading in heads:
#     print(heading)

# Interleave paragraphs & headers
text = [val for pair in zip(paras, heads) for val in pair]
text = ' '.join(text)

# Drop footnote superscripts in brackets
text = re.sub(r"\[.*?\]+", '', text)

# Replace '\n' (a new line) with '' and end the string at $1000.
text = text.replace('\n', '')[:-11]
print(text)
para_list = text.split(".")
highest_word_sentence = []
new_word_sentence = ""
hi_score_sentence = 0

for sentence in para_list:
    # print(sentence)
    new_word_sentence = sentence.lower()
    wordscore_sentence = textstat.difficult_words(sentence)
    if wordscore_sentence > hi_score_sentence:
        hi_score_sentence = wordscore_sentence
        highest_word_sentence = new_word_sentence
print()
print("Have you heard of the {}...{}".format(winning_wiki_search, highest_word_sentence))




# testing -------
# for s in soup.find_all(text=True):
#     # Check out the parent name
#     print(f'Parent name: {s.parent.name}')
#     # Check the text
#     print(s)