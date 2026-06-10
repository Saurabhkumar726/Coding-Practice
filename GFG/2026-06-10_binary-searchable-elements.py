class Solution:
    def binarySearchable(self, arr):
        n = len(arr)
        ans = 0

        for i in range(n):
            l, r = 0, n - 1
            ok = True

            while l <= r:
                mid = (l + r) // 2

                if mid == i:
                    break

                if mid < i:
                    if arr[mid] < arr[i]:
                        l = mid + 1
                    else:
                        ok = False
                        break
                else:
                    if arr[mid] > arr[i]:
                        r = mid - 1
                    else:
                        ok = False
                        break

            if ok:
                ans += 1

        return ans