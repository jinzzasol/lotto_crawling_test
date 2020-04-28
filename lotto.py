import numpy as np
from os import listdir
import pandas as pd
import random
import matplotlib.pyplot as plt
from collections import Counter

cnt_list = []
for i in range(0, 46):
    cnt_list.append(0)

with open('D:/90_Python/lotto.csv') as fp:
    data = fp.readlines()

for i in range(0, len(data)):
    temp_lotto = ''.join(data[i])
    temp_lotto = temp_lotto.replace('\n', '')
    cur_lotto_list = list(temp_lotto.split(','))

    for i in range(2, len(cur_lotto_list)) :
        cnt_index = cur_lotto_list[i]
        cnt_list[int(cnt_index)] += 1

num = np.arange(0,46,1)
#print(num)
hit = np.array(cnt_list)
#print(hit)

matrix = np.array([num] + [hit])
matrix = matrix.T
#print(matrix)

for k in range (1, len(matrix)) :
    print('%5d 번공: %3d 회' %(matrix[k,0], matrix[k,1]))

y = []
y = sorted(matrix, key=lambda matrix: matrix[1])
y = np.array(y)
#print(y)
#y에서 당첨회수 오름차순으로 배열됨
#Plot을 그리기 위해, 번호랑 횟수를 xs, ys 로 분리
xs = matrix[:,0];
ys = matrix[:,1];
plt.bar(xs, ys)
plt.axis([0, 47, 80, 160])
plt.show()

#y 배열에서 횟수가 적은 순에서 많은 순으로 배열되었으므로,
#하위 20개의 행, 즉, 회수가 많은 상위 20개의 숫자를 y2 에 저장
y2 = y[26:, :]
x2 = y2[:,0]
y3 = y2[:,1]
#그 다음 상위 10개의 숫자를 yy2 에 저정
yy2 = y[15:25, :]
xx2 = yy2[:,0]
yy3 = yy2[:,1]
print("Top 1-20 number =", x2)
print("Top 21-30 number =", xx2)
x2 = x2.tolist()
xx2 = xx2.tolist()

number =[];
number2 =[];
for i in range(0, 6):
     out = random.sample(x2, 4)
     out2 = random.sample(xx2, 2)
     number = out + out2
     number2.append(number)
#print("Recommended_number_set =", number2)

print("Recommended_number_1=",number2[0])
print("Recommended_number_2=",number2[1])
print("Recommended_number_3=",number2[2])
print("Recommended_number_4=",number2[3])
print("Recommended_number_5=",number2[4])
