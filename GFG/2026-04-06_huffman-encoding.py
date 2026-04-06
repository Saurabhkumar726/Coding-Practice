import heapq

class Node:
    def __init__(self, freq, char=None, left=None, right=None, min_idx=0):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.min_idx = min_idx

class Solution:
    def huffmanCodes(self, s, f):
        if len(s) == 1:
            return ["0"]
        
        heap = []
        
        for i in range(len(s)):
            heapq.heappush(heap, (f[i], i, Node(f[i], s[i], min_idx=i)))
        
        while len(heap) > 1:
            f1, i1, n1 = heapq.heappop(heap)
            f2, i2, n2 = heapq.heappop(heap)
            
            if f1 < f2 or (f1 == f2 and n1.min_idx < n2.min_idx):
                left, right = n1, n2
            else:
                left, right = n2, n1
            
            merged = Node(f1 + f2, left=left, right=right, min_idx=min(left.min_idx, right.min_idx))
            heapq.heappush(heap, (merged.freq, merged.min_idx, merged))
        
        root = heap[0][2]
        res = []
        
        def preorder(node, path):
            if node.char is not None:
                res.append(path)
                return
            preorder(node.left, path + "0")
            preorder(node.right, path + "1")
        
        preorder(root, "")
        return res