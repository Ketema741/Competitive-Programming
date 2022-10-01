class Solution(object):
    def fizzBuzz(self, n):
        fizz = "Fizz"
        buzz = "Buzz"
        fizzBuzz = "FizzBuzz"
        ans = []
        for i in range(1, n+1):
            if i%3==0 and i%5==0:
                ans.append(fizzBuzz)
            elif i%3==0:
                ans.append(fizz)
            elif i%5==0:
                ans.append(buzz)
            else:
                ans.append(str(i))
        print(ans)
        return ans
                
        """
        :type n: int
        :rtype: List[str]
        """
        