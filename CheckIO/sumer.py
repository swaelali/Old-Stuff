def checkio(nums):
	if nums == []:
		return 0
	else:
		return nums[0] + checkio(nums[1:])
	
	
print checkio([2, 2, 2, 2, 2, 2])
