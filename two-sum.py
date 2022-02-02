def twoSum(self, nums, target):
        seen = {}
        i = 0
        for n in nums:
            if (target - n) in seen:
                if(seen[target-n] == i): continue
                return [seen[target-n], i]
            seen[n] = i
            i = i + 1
