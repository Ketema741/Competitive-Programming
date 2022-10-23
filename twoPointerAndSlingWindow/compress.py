def compress(chars):
    slow = fast = 0  
    while fast < len(chars):
        while fast < len(chars) and chars[slow] == chars[fast]:
            fast += 1
            
        if (fast-slow) == 1:
            slow = fast
        else:
            chars[slow+1:fast] =str(fast-slow)
            slow = fast
    
    return chars

print(compress(["a","a","a","b","b","a","a"]))