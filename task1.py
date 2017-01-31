def high_and_low (nStr):
    nums = nStr.split(' ')
    for n in nums:
        n = int(n)
    nums.sort()
    print(str(nums[len(nums) - 1]) + ' ' + str(nums[0]))

high_and_low ("1 2 3 4 5") # возвращение "5 1"
high_and_low ("1 2 -3 4 5") # возвращение "5 -3"
high_and_low ("1 9 3 4 -5") # возвращение "9 -5"
