import urllib.request 
from bs4 import BeautifulSoup 
import nltk 
nltk.download('stopwords')
from nltk.corpus import stopwords
url = 'https://en.wikipedia.org/wiki/Artificial_intelligence'
# Create a request with a User-Agent header
req = urllib.request.Request(
    url,
    headers={'User-Agent': 'Mozilla/5.0'}
)

response=urllib.request.urlopen(req)
html=response.read()
print(html)
soup=BeautifulSoup(html,'html5lib')
text=soup.get_text(strip=True)
print(text)
tokens=[t for t in text.split()]
print(tokens)
sr=stopwords.words('english')
clean_token=tokens[:]
for tok in tokens:
    if tok in sr:
        clean_token.remove(tok)
print(clean_token)

import matplotlib.pyplot as plt
freq=nltk.FreqDist(clean_token)
for key,val in freq.items():
    print(str(key)+":"+str(val))
freq.plot(20,cumulative=False)
plt.show()