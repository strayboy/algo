# Implement a trie with insert, search, and startsWith methods.
#
#  Example:
#
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
#
#
#  Note:
#
#
#  You may assume that all inputs are consist of lowercase letters a-z.
#  All inputs are guaranteed to be non-empty strings.
#
#  Related Topics Design Trie
#  👍 4108 👎 64


# leetcode submit region begin(Prohibit modification and deletion)
class TrieNode:
    def __init__(self, data: str):
        self._data = data
        self._children = [None] * 26
        self._is_ending_char = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = TrieNode("/")

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self._root
        for index, char in map(lambda x: (ord(x) - ord("a"), x), word):
            if not node._children[index]:
                node._children[index] = TrieNode(char)
            node = node._children[index]
        node._is_ending_char = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._root
        for index in map(lambda x: ord(x) - ord("a"), word):
            if not node._children[index]:
                return False
            node = node._children[index]
        return node._is_ending_char

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self._root
        for char in prefix:
            index = ord(char) - ord("a")
            if not node._children[index]:
                return False
            node = node._children[index]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("ab")
    print(trie.search("abc"))  # returns true
    print(trie.search("ab"))  # returns false
    print(trie.startsWith("abc"))  # returns true
    print(trie.startsWith("ab"))  # returns true
    trie.insert("ab")
    print(trie.search("abc"))  # returns true
    print(trie.startsWith("abc"))  # returns true
    trie.insert("abc")
    print(trie.search("abc"))  # returns true
    print(trie.startsWith("abc"))  # returns true
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)
