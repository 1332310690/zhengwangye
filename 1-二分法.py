list = [1,2,3,4,5,6,7,8,9]
key = 9
center = int(len(list)/2)
if key in list:
	while True:
		if list[center] > key:
			center = center-1
		elif list[center] < key:
			center = center+1
		elif list[center] == key:
			print('%d在列表里索引为%d'%(key,center))
			break
