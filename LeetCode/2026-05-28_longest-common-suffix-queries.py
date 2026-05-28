from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1
        self.length = float('inf')

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        best_idx = 0
        best_len = len(wordsContainer[0])
        
        for i, w in enumerate(wordsContainer):
            if len(w) < best_len:
                best_len = len(w)
                best_idx = i
        
        root.index = best_idx
        root.length = best_len
        
        for i, word in enumerate(wordsContainer):
            node = root
            rev = word[::-1]
            
            for ch in rev:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                
                node = node.children[ch]
                
                if len(word) < node.length:
                    node.length = len(word)
                    node.index = i
        
        ans = []
        
        for word in wordsQuery:
            node = root
            
            for ch in word[::-1]:
                if ch not in node.children:
                    break
                node = node.children[ch]
            
            ans.append(node.index)
        
        return ans
        