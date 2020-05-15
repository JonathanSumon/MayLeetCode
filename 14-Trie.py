#Implement a trie with insert, search, and startsWith methods.

#Solution

class Trie:
    def __init__(self):
        self.trie={}

    def insert(self, word: str) -> None:
        node=self.trie
        for i in word:
            node=node.setdefault(i,{})
        node['end']=1

    def search(self, word: str) -> bool:
        node=self.trie
        for i in word:
            if i not in node : return 0
            node=node[i]
        return 'end' in node

    def startsWith(self, prefix: str) -> bool:
        node=self.trie
        for i in prefix:
            if i not in node : return 0
            node=node[i]
        return 1