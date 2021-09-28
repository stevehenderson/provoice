import requests


#http://en.wikipedia.org//w/api.php?action=query&format=json&prop=revisions&titles=Cat&formatversion=2&rvprop=content&rvslots=*

#url = 'https://en.wikipedia.org/w/api.php?action=opensearch&search=oregon&limit=20&namespace=0&format=json&prop=revisions&titles=Cat&formatversion=2&rvprop=content&rvslots=*'
url = 'https://en.wikipedia.org/w/api.php'

params = dict(
    action='opensearch',
    search='heading to oregon',
    limit='20',
    namespace='0',
    format = 'json'
)

resp = requests.get(url=url, params=params)
data = resp.json() 
print(data)


#print(type(data))

#for item in data:
#    print(item)

list1 = data[1]    
#print(list1)

# item == "oregon trail"
# i =3
# longest_index =1
# longest_length =25

longest_length = 0
longest_index = None
i=0
for item in list1:
    next_length = len(item)
    if next_length > longest_length:
        longest_length = next_length
        longest_index = i
    i=i+1

print("Winner is: {} with legth of {}".format(list1[longest_index], longest_length))

list3 = data[3]
winning_url = list3[longest_index]

print("Heading to get {}".format(winning_url))

resp = requests.get(url=winning_url)

print(resp.text)
