class Solution:
    def canSeatAllPeople(self, k, seats):
        count = 0
        n = len(seats)
        
        for i in range(n):
            if seats[i] == 0:
                left_empty = (i == 0 or seats[i - 1] == 0)
                right_empty = (i == n - 1 or seats[i + 1] == 0)
                
                if left_empty and right_empty:
                    seats[i] = 1
                    count += 1
                    
                    if count >= k:
                        return True
        
        return count >= k