import random
nicaicai = random.randint(2.4)
i = 1
j = int(input('请输入次数:'))
while i<=j:
	diannao = int(input("请输入2:石头  3:布 4:剪刀"))
	if diannao <= 4 and nicaicai > 1:
		if（nicaicai==2 and diannao ==3) or (nicaicai ==3 and diannao ==4) or (nicaicai ==4 and diannao==2):
			print("you wen")
		elif nicaicai  == diannao:
			print("平局")
		else:
			print("你输了")
	i+=1
