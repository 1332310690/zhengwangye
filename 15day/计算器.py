def jisuanqi(z,x,c):
	q = 0
	if c == 1:
		q = z+x
		print('和是%0.2f'%q)
	elif c == 2:
		q = z-x
		print('差是%0.2f'%q)
	elif c == 3:
		q = z*x
		print('积是%0.2f'%q)
	elif c == 4:
		if x !=0:
			q =z/x
			print('商是%0.2f'%q)
		else:
			print('输入输入错误')

	else:
		print('输入错误')
while True:
	q =float(input('请输入数字'))
	w =float(input('请再输入一个数字'))
	e = float(input('请选择符号　１+ 2- 3* 4/'))
	jisuanqi(q,w,e)
		
