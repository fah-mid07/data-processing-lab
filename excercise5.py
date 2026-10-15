studentInfo={'Name':'Fahmid', 'Id':'25-63645-3', 'Department':'Data Science', 'CGPA':3.03}
for x, value in studentInfo.items():
    print(f'{x:<15}:{value}')

if studentInfo['CGPA'] >=2.50:
    print('Good Standing')
else:
    print('Academic Warning')