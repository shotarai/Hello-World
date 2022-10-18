import sys
import random
import numpy as np

def conse(score):
	for i in range(len(score)):
		score[i] = str(random.randint(0,100))
	return score

try:
	print('生徒の人数を入力してください')
	times = int(input())
	score = np.empty(3,'<U3')
	with open('student.txt','w') as f:
		for i in range(times):
			name = []
			name.append('st' + str(i+1))
			name.extend(conse(score))
			f.write(' '.join(name) + '\n')
except:
	print('エラー情報:' + str(sys.exc_info()[1]))