

def bisearch( nums, target):
        size = len(nums)
        if size <= 0:
             return -1
        
        if size == 1:
             if nums[0] == target:
                  return 0
             else:
                  return -1

        mid = int(size/2)
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            out = bisearch(nums[mid:], target)
            if out == -1:
                 return -1
            return mid + out
        else:
            out = bisearch(nums[:mid], target)
            if out == -1:
                 return -1
            return out
        
if __name__ == "__main__":
    nums = [-1,0,3,5,10,12]
    #  nums = [10]
    # nums = [10,15]

    target = 10
    print("out", bisearch(nums, target))