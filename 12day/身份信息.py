list = []
name_list=[]
count = 0
while True:
	if count == 3:
		break
	dict = {}
	name = input('请输入你的名字')
	age = input('请输入你的年龄')
	sex = input('请输入你的性别')
	qq = int(input('请输入你的qq号'))
	weight = float(input('请输入你的体重'))
	if name not in name_list:
		dict['name'] = name
		dict['age'] = age
		dict['sex'] = sex
		dict['qq'] = qq
		dict['weight'] = weight
		list.append(dict)
		name_list.append(name)
		count+=1
	else:
		print('名字重了')
age_sum =0
for i in list:
	age_sum = age_sum+i.get('age')
	print(i)

