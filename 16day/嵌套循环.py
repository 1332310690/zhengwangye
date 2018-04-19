import time
def playgame():
	for i in range(10):
		print('性感沙滩')
		time.sleep(1)
	print('你全家都来了')
	result = kill()
	if result == "你被五马分尸了":
		print('你被碎尸了')
	else:
		print('接着玩')
def kill():
	print('毁尸灭迹')
	return '你被五马分尸了'
playgame()
	

