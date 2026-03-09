class Solution:
    def largestSwap(self, s):
        arr = list(s)
        last = {c:i for i,c in enumerate(arr)}
        n = len(arr)
        
        for i in range(n):
            for d in range(9, int(arr[i]) , -1):
                c = str(d)
                if c in last and last[c] > i:
                    j = last[c]
                    arr[i], arr[j] = arr[j], arr[i]
                    return "".join(arr)
        
        return s
        