while True:
	a1 = int(input("请输入一个数字"))
	b2 = int(input("请输入一个数字"))
	sum = 0
	if a1 < b2:
		for i in range(a1,b2+1):
			sum=sum+i
		print(sum)
		break
	
	else:
		print("输入有误")

