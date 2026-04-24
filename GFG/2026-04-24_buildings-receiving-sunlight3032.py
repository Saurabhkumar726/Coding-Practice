class Solution:
    def visibleBuildings(self, arr):
        count = 0
        max_height = 0
        
        for h in arr:
            if h >= max_height:
                count += 1
                max_height = h
        
        return count