from collections import deque
import string
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        
        q = deque([beginWord])
        distance = {beginWord:0}
        found = False

        while q and not found:
            level_size = len(q)
            for _ in range(level_size):
                word = q.popleft()
                curr_dist = distance[word]
                if word == endWord:
                    found=True
                    break

                for i in range(len(word)):
                    for ch in string.ascii_lowercase:
                        new_word = word[:i] + ch + word[i+1:]
                        if new_word in word_set:
                            if new_word not in distance:
                                distance[new_word] = curr_dist + 1
                                q.append(new_word) 

        if endWord not in distance:
            return []
        
        ans = []

        def dfs(curr_word, path):
            if curr_word == beginWord:
                ans.append(path[::-1])
                return
            
            for i in range(len(curr_word)):
                for ch in string.ascii_lowercase:
                    prev_word = curr_word[:i] + ch + curr_word[i+1:]

                    if prev_word in distance and distance[prev_word]==distance[curr_word]-1:
                        path.append(prev_word)
                        dfs(prev_word, path)
                        path.pop()
        
        dfs(endWord, [endWord])
        return ans



            



        