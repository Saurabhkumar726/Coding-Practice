from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted([(positions[i], i, healths[i], directions[i]) for i in range(len(positions))])
        stack = []
        alive = [True]*len(positions)
        curr_health = healths[:]

        for pos, idx, h, d in robots:
            if d == 'R':
                stack.append(idx)
            else:
                while stack and curr_health[idx] > 0:
                    top = stack[-1]
                    if not alive[top]:
                        stack.pop()
                        continue
                    if curr_health[top] < curr_health[idx]:
                        alive[top] = False
                        stack.pop()
                        curr_health[idx] -= 1
                    elif curr_health[top] > curr_health[idx]:
                        alive[idx] = False
                        curr_health[top] -= 1
                        break
                    else:
                        alive[top] = False
                        alive[idx] = False
                        stack.pop()
                        break

        res = []
        for i in range(len(positions)):
            if alive[i]:
                res.append(curr_health[i])
        return res
        