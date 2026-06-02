from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:
        
        ans = float('inf')
        
        for i in range(len(landStartTime)):
            land_finish = landStartTime[i] + landDuration[i]
            
            for j in range(len(waterStartTime)):
                finish_time = max(waterStartTime[j], land_finish) + waterDuration[j]
                ans = min(ans, finish_time)
        
        for j in range(len(waterStartTime)):
            water_finish = waterStartTime[j] + waterDuration[j]
            
            for i in range(len(landStartTime)):
                finish_time = max(landStartTime[i], water_finish) + landDuration[i]
                ans = min(ans, finish_time)
        
        return ans
        