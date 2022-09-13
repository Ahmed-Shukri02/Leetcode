# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
    # return true if t can be formed by s
    if t.length != s.length
        return false
    end
    
    hmap1 = {}
    for char in s.split("")
        if hmap1.key?(char)
            hmap1[char] = hmap1[char] + 1
        else
            hmap1[char] = 1
        end
    end
    
    for char in t.split("")
        if hmap1.key?(char) and hmap1[char] > 0
            hmap1[char] -= 1
        else
            return false
        end
    end
    return true
end