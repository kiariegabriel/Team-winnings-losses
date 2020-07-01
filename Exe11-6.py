d=dict()
score=100
for i in range(5):
	l=list()
	team=input('Enter team: ')
	l.append(eval(input('Enter score: ')))
	l.append(score-l[0])
	d[team]=l
print(d)