def compress(chars):
    slow = fast = 0  
    while fast < len(chars):
        while fast < len(chars) and chars[slow] == chars[fast]:
            fast += 1   
        if (fast - slow) == 1:
            slow = fast
        else:
            chars[slow + 1 : fast] =str(fast - slow)
            slow = fast
    
    return charsclass Solution:
    def compress(self, chars: List[str]) -> int:
        walker = runner = 0
        while runner < len(chars):
            chars[walker] = chars[runner]
            count = 1
            while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
                runner += 1
                count += 1
            if count > 1:
                for c in str(count):
                    chars[walker+1] = c
                    walker += 1
            runner += 1
            walker += 1
        return walker

print(compress(["a","a","a","b","b","a","a"]))