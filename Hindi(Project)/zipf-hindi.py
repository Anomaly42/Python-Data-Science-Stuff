import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from collections import Counter

prop = FontProperties()
prop.set_file('Lohit-Devanagari.ttf')

file = open('karmabhoomi.txt', mode='r' , encoding='utf-8')
data = file.read()

redundant = ',।\'\"?.!<>=1234567890'
for r in redundant:
    data = data.replace( r, '')
data = data.replace('-', ' ')
word_list = data.split()
file.close()

xlist = []
ylist = []
ftlist = []

info = Counter(word_list)
ftlist = [ (y, x) for x, y in info.items() ]
ftlist.sort(key=lambda tup: tup[0])

for i in range(len(ftlist)):
    xlist.append(i)
    ylist.append(ftlist[i][0])
    
print("Total Words: {}, Unique Words: {}".format(len(word_list), len(xlist)) )
plt.plot(xlist, ylist)

for i, unit in enumerate(ftlist):
    if unit[0] > 10:
        plt.annotate(unit[1] + " -" + str(ylist[i]), (i, ylist[i]), fontproperties=prop)
    
plt.show()
