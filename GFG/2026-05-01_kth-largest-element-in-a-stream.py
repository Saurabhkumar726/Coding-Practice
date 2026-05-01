import heapq

class Solution:
    def kthLargest(self, arr, k):
        heap = []
        res = []
        
        for num in arr:
            heapq.heappush(heap, num)
            
            if len(heap) > k:
                heapq.heappop(heap)
            
            if len(heap) < k:
                res.append(-1)
            else:
                res.append(heap[0])
        
        return res