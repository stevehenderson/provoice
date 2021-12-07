import random
dictionary1 = {'animals':["dog","cat","shark"],
           'things':["desk","chair","pencil"],
           'food':["spaghetti","ice-cream","potatoes"]}

which_list = dictionary1['animals']
print(which_list)
selection = random.choice(which_list)
print(selection)