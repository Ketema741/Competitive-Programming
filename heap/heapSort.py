#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,lst, i, upper):
        while True:
            left, right =  i*2 + 1, i*2 + 2
            if max(left, right) < upper:
                if lst[i] >= max(lst[left], lst[right]): break
                elif lst[left] > lst[right]:
                    self.swap(lst, i, left)
                    i = left
                else:
                    self.swap(lst, i, right)
                    i = right
            elif left < upper:
                if lst[left] > lst[i]:
                    self.swap(lst, i, left)
                    i = left
                else: break
            elif right < upper:
                if lst[right] > lst[i]:
                    self.swap(lst, i, right)
                    i = right
                else: break
            else: break
    
    #Function to build a Heap from array.
    def buildHeap(self,lst,n):
        for j in range((len(lst)-2)//2, -1, -1):
            self.heapify(lst, j, len(lst))
        
    def swap(self, lst, i, j):
        lst[i], lst[j] = lst[j], lst[i]
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, lst, n):
        self.buildHeap(lst, n)
        for end in range(len(lst)-1, 0, -1):
           self.swap(lst, 0, end)
           self.heapify(lst, 0, end)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends