class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {0,1,2,5,6,8,9}
        diff = {2,5,6,9}
        
        count = 0
        
        for num in range(1, n + 1):
            x = num
            changed = False
            ok = True
            
            while x > 0:
                d = x % 10
                if d not in valid:
                    ok = False
                    break
                if d in diff:
                    changed = True
                x //= 10
            
            if ok and changed:
                count += 1
        
        return count