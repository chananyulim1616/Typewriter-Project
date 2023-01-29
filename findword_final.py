import bs4
import requests
import pandas as pd
from pandas import ExcelWriter

'''data'''
lskeyword = []
data = requests.get('https://sentence.yourdictionary.com/index/a')
soup = bs4.BeautifulSoup(data.text, 'html.parser')
text = soup.find_all('a',{"class":"examples-link inline-block w-full max-w-200 truncate text-black text-base my-2 hover:underline hover:text-blue-900 active:text-blue-900 visited:text-purple"})
for i in text:
    k = str(i).replace('<a class="examples-link inline-block w-full max-w-200 truncate text-black text-base my-2 hover:underline hover:text-blue-900 active:text-blue-900 visited:text-purple" data-v-0f8b352a="" ','')
    k=k.replace(" ","").replace('</a>','').replace('">','').replace('\n',',')
    ls1 = k[8:].split(',')
    lskeyword.append(ls1[1])
print(lskeyword)

'''data'''
lsword = []
for i in range(1250):
    data = requests.get('https://sentence.yourdictionary.com/'+lskeyword[i])
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    text = soup.find_all('p',{"class":"sentence-item__text"})
    for x in text:
        x= str(x).replace('<p class="sentence-item__text" data-v-ea7db9ee="">',"").replace('<strong>','').replace('</strong>','').replace('</p>','')
        lsword.append(x)
    print(lskeyword[i],'success')

'''convert'''
df = pd.DataFrame(lsword)

'''write'''
writer = ExcelWriter("testword.xlsx")
df.to_excel(writer, "Sheet1")
writer.save()