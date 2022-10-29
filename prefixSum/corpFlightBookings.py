class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n + 2)
        for booking in (bookings):
            first, last, seat = booking[0], booking[1], booking[2]
            ans[first] += seat
            ans[last+1] -= seat
        carry, res = 0, []
        for i in range(1, n+1):
            carry += ans[i]
            res.append(carry) 
        return res
