class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people)-1
        people = sorted(people, reverse=True)
        count = 0
        while l <= r :
            if people[l] > limit:
                count += 1
                l += 1
            elif people[l] +people[r] <= limit:
                count +=1
                r -= 1
                l += 1 
            else:
                count += 1
                l += 1
        return count
                        
                        
                        
                    