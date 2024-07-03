num = [i for i in range(1, 1001) if i % 2 != 0]
#print(num)

num = [1, 2, 3, 4]
cout = ['uk', 'us', 'germ']
count = [1, 'us', 2, 'uk']
cells = [['A1','A2','A3'], ['B1','B2','B3']]
for x in cells:
    for y in x:
         print('Element: ', y)

#print(cells[1][1])


grades = {}
grades['john'] = 'A'
grades['alondra'] = 'C'
grades['andrew'] = 'B'
grades['daniel'] = 'A'
grades['Maria'] = 'A'



if 'john' in grades:
    print('John Got:', grades['john'])

for person, score in grades.items():
        if score == 'A':
            print(person, 'Congrats on passing with a score of:', score)
        else:
         print(person, 'Sorry you have failed the test with a score of:', score)