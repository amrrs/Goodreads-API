#Extracting Author Information with Author id

import requests
from xml.etree import ElementTree
import shutil

author_id = '1439'

key = 'xxx' #replace it with your developer key

response = requests.get('https://www.goodreads.com/author/show.xml?'+'key='+key+'&id='+author_id)

tree = ElementTree.fromstring(response.content)

#print(response.content)
#print(tree)

print('Retrieving Author Info...\n')
for leaves in tree[1]:
    print(leaves.tag +' : '+str(leaves.text))

#print('Author Name: ' + tree[1][1].text)

if(raw_input('Would you like to download the author image? y/n')=='y'):
    
    print('Downloading Author Image...\n')
    img = requests.get(tree[1][5].text, stream=True)
    with open(tree[1][0].text+'.jpg', 'wb') as out_file:
        shutil.copyfileobj(img.raw, out_file)
    del img
    print(tree[1][0].text+'.jpg'+' Image Downloaded Successfully')
else:
    print('Thank you')
        
