from collections import deque
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        st = set(wordList)
        if beginWord in st:
            st.remove(beginWord)
        q.append((beginWord, 1))

        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            
            for i in range(len(word)):
                for ch in string.ascii_lowercase:
                    word_list = list(word)
                    word_list[i] = ch
                    new_word = "".join(word_list)
                    if new_word in st:
                        st.remove(new_word)
                        q.append((new_word, step+1))
        
        return 0

        