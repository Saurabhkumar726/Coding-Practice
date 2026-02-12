class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)

        def canAchieve(target):
            diff = [0] * (n + 1)
            curr_add = 0
            operations = 0

            for i in range(n):
                curr_add += diff[i]
                height = arr[i] + curr_add

                if height < target:
                    need = target - height
                    operations += need
                    if operations > k:
                        return False
                    curr_add += need
                    if i + w < n:
                        diff[i + w] -= need

            return True

        left = min(arr)
        right = min(arr) + k
        ans = left

        while left <= right:
            mid = (left + right) // 2
            if canAchieve(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
