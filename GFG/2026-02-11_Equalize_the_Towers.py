class Solution:
    def minCost(self, heights, cost):
        towers = sorted(zip(heights, cost))
        
        total_weight = sum(cost)
        half = total_weight // 2
        
        cumulative = 0
        target = 0
        
        for h, c in towers:
            cumulative += c
            if cumulative > half:
                target = h
                break
        
        total_cost = 0
        for h, c in zip(heights, cost):
            total_cost += abs(h - target) * c
        
        return total_cost
