from collections import deque
import string
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        q = deque([[beginWord]])
        used_on_level = [beginWord]
        level = 0
        ans = []


        while q:
            path = q.popleft()

            if len(path)>level:
                level+=1
                for word in used_on_level:
                    word_set.discard(word)
            word = path[-1]

            if word==endWord:
                if not ans:
                    ans.append(path[:])
                elif len(ans[0])==len(path):
                    ans.append(path[:])

            for i in range(len(word)):
                for ch in string.ascii_lowercase:
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in word_set:
                        path.append(new_word)
                        q.append(path[:])
                        used_on_level.append(new_word)
                        path.pop()
            
        return ans

