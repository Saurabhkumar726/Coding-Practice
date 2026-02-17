class Solution:
    def overlapInt(self, arr):
        events = []
        
        for start, end in arr:
            events.append((start, 1))
            events.append((end + 1, -1))
        
        events.sort()
        
        current = 0
        maximum = 0
        
        for _, value in events:
            current += value
            maximum = max(maximum, current)
        
        return maximum
