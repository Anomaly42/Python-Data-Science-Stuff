file = open('gunaho_ka_devta.txt', mode='r' , encoding='utf-8')
data = file.read(10000000)
data = data.replace(',', '')
data = data.replace('।', '')
data = data.replace('-', '')
data = data.replace('\'', '')
data = data.replace('\"', '')
data = data.replace('?', '')
data = data.replace('...', '')
data = data.replace('!', '')
word_array = data.split()
file.close()

info = {}
yarray = []
textarray = []
ftarray = []
for word in [ele for ind, ele in enumerate(word_array,1) if ele not in word_array[ind:]]:
    info[word] = word_array.count(word)
    yarray.append(word_array.count(word))
    ftarray.append((word_array.count(word), word))

xarray = []
for i in range(len(info)):
    xarray.append(i)

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

prop = FontProperties()
prop.set_file('Lohit-Devanagari.ttf')

yarray.sort()

ftarray.sort(key=lambda tup: tup[0])
for i in range(len(ftarray)):
    textarray.append(ftarray[i] [1])


print(len(info))

plt.plot(xarray, yarray)

for i, txt in enumerate(textarray):
    if ftarray[i] [0] > 10:
        plt.annotate(txt, (xarray[i], yarray[i]), fontproperties=prop)
    
plt.show()
