# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
    hmap = {}
    for num in nums
        if !hmap.key?(num)
            hmap[num] = 1
        else
            return true
        end
    end
    
    return false
end