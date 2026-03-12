from typing import List

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        parent = list(range(n))
        rank = [0]*n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x,y):
            x=find(x)
            y=find(y)
            if x==y:
                return False
            if rank[x]<rank[y]:
                parent[x]=y
            elif rank[x]>rank[y]:
                parent[y]=x
            else:
                parent[y]=x
                rank[x]+=1
            return True

        def can(x):
            parent[:] = list(range(n))
            rank[:] = [0]*n
            upgrades = k
            used = 0

            for u,v,s,m in edges:
                if m==1:
                    if s < x or not union(u,v):
                        return False
                    used += 1

            opts=[]
            for u,v,s,m in edges:
                if m==0:
                    opts.append((u,v,s))

            opts.sort(key=lambda t:max(t[2],t[2]*2), reverse=True)

            for u,v,s in opts:
                if used==n-1:
                    break
                if find(u)==find(v):
                    continue
                if s>=x:
                    union(u,v)
                    used+=1
                elif s*2>=x and upgrades>0:
                    union(u,v)
                    upgrades-=1
                    used+=1

            return used==n-1

        lo,hi=0,2*10**5
        ans=-1
        while lo<=hi:
            mid=(lo+hi)//2
            if can(mid):
                ans=mid
                lo=mid+1
            else:
                hi=mid-1
        return ans