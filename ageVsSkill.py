import csv
import matplotlib.pyplot as plt
import numpy as np

file = open('data.csv','r')
csv_reader =csv.DictReader(file)        # To read dictionary type csv
players = [ ]
listUmur = [ ]
listOverall = [ ]

for i in csv_reader:
    players.append(dict(i))

# print(players)
# print(len(players))
# print(type(players[0]['Overall']))
# print(listUmur)
# print(type(listUmur))

for player in players:
    listUmur.append(int(player['Age']))
    listOverall.append(int(player['Overall']))

x = np.array(listUmur)
y = np.array(listOverall)

# print(listUmur)
# print(type(listOverall))


x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x5 = []
y5 = []
x6 = []
y6 = []
'''
============================================================
Based on Age and Skill
============================================================
'''
# color = []

# for i in range(len(x)):           # Beware of the total number of data
#     if x[i]>=25 and y[i]>80:
#         color.append('g')
#     elif x[i]>25 and y[i]<70:
#         color.append('b')
#     elif x[i]<25 and y[i]>70:
#         color.append('y')
#     else:
#         color.append('r')

# for i in range(len(x)):
#         if x[i]>=30 and y[i]>=80:
#                 x1.append(x[i])
#                 y1.append(y[i])
#         elif x[i]>=30 and y[i]<80:
#                 x2.append(x[i])
#                 y2.append(y[i])
#         elif x[i]<30 and y[i]>80:
#                 x3.append(x[i])
#                 y3.append(y[i])
#         else:
#                 x4.append(x[i])
#                 y4.append(y[i])

for i in range(len(x)):
        if x[i]>=30 and y[i]>=80:
                x1.append(x[i])
                y1.append(y[i])
        elif x[i]>=30 and y[i]<80:
                x2.append(x[i])
                y2.append(y[i])
        elif x[i]<30 and x[i]>20 and y[i]>=80:
                x3.append(x[i])
                y3.append(y[i])
        elif x[i]<30 and x[i]>20 and y[i]<80:
                x4.append(x[i])
                y4.append(y[i])
        elif x[i]<=20 and y[i]>80:
                x5.append(x[i])
                y5.append(y[i])
        else:
                x6.append(x[i])
                y6.append(y[i])

'''
============================================================
Based on Skill Level
============================================================
'''

# for i in range(len(x)):             # Beware of the total number of data
#     if x[i]>=16 and y[i]>=70:
#         color.append('g')
#     elif x[i]>=16 and y[i]<70:
#         color.append('r')

plt.figure('Plot', figsize=(10,7))
plt.subplot(1,1,1)
plt.title('Plot Age vs Overall')
plt.grid(True)
plt.xlabel('Players Age')
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.ylabel('Players Overall Score')
plt.yticks(np.arange(min(y),max(y), 5.0))

plt.scatter(x1,y1, color='b', marker="o")
plt.scatter(x2,y2, color='g', marker="o")
plt.scatter(x3,y3, color='r', marker="o")
plt.scatter(x4,y4, color='c', marker="o")
plt.scatter(x5,y5, color='m', marker="o")
plt.scatter(x6,y6, color='y', marker="o")



plt.legend(['Old but good','Old and normal','Mature but good','Mature and bad','Young and good','Young and raw'],loc='upper right')

plt.annotate('This is Messi', xy=(31,94), xytext=(26,95), arrowprops=dict(facecolor='black', shrink=1))

plt.show()
