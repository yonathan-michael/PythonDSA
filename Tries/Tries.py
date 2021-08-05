class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26
        self.is_end_word = False
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, t):
        return ord(t) - ord('a')

    def insert(self, key):
        # If there is nothing to insert, return false
        if key is None:
            return False

        # Here are we standardizing the input, all lowercase
        key = key.lower()
        # Start at root of the trie
        current = self.root

        # Iterate over each character in the key
        for letter in key:

            # Get the index for the character
            index = self.get_index(letter)

            # If this index is empty, meaning this node does not have this character as a child
            if current.children[index] is None:
                # Create a TrieNode with that character and put it inside this
                # node's list of children in the appropriate index
                current.children[index] = TrieNode(letter)
                print(letter, "inserted")

            # After you have placed the child in the node, you go down a level into the new node
            current = current.children[index]

            # After you completed the word and you are at the last letter/level
            # Mark the end of the word

        current.is_end_word = True
        print("'" + key + "'inserted")

    def search(self, key):
        # if there is no key
        if key is None:
            return False

        # standardize input and start at the root
        key = key.lower()
        current = self.root

        # Get index for each character
        for letter in key:
            index = self.get_index(letter)

            # if this character is not in children list , return false
            if current.children[index] is None:
                return False

            # Go down one level
            current = current.children[index]

        # If the end of the word is marked and there is a node, return True
        if current is not None and current.is_end_word:
            return True

        # If we get to a node and its not the end word, return false
        return False

    def delete(self, key):
        if self.root is None or key is None:
            print("None key or empty trie error")
            return
        print("\nDeleting:", key)

        # Start delete function from root, with length of key, and level 0
        self.delete_helper(key, self.root, len(key), 0)

    def delete_helper(self, key, current, length, level):

        # Initialize this marker
        deleted_self = False

        # If the current node does not exist
        if current is None:
            print("Key does not exist")
            return deleted_self

        # Base Case
        # When you get to the end of the word, the last level
        if level is length:

            print("Level is length, we are at the end")

            # No nodes ahead, this is the last node, delete the node and return True
            if current.children.count(None) == len(current.children):
                print("- Node", current.char, ": has no children, delete it")
                current = None
                deleted_self = True

            # Don't delete node and just unmark as end of word, return False
            else:
                print("- Node", current.char, ": has children, don't delete \it")
                current.is_end_word = False
                deleted_self = False

        else:
            # Get index of next character of string
            index = self.get_index(key[level])
            print("traverse to", key[level])
            # Get the child node
            child_node = current.children[index]
            # [RECURSION LINE] Recursively go down the trie, and get whether the child was deleted or not (True or False)
            child_deleted = self.delete_helper(key, child_node, length, level + 1)

            # If the child was deleted, you must delete the pointer in its parent to that child
            if child_deleted:
                print("- Delete link from", current.char, "to", key[level])
                current.children[index] = None

                # This node has had its child deleted, but we will not delete this current node
                # because it is marked as the end of another word (it is a prefix)
                if current.is_end_word:
                    print("-- Don't delete node", current.char, ": word end")
                    # For this node we will pass False for (Child deleted)
                    deleted_self = False

                # This is basically checking condition of whether there are 26 Nones
                # If this is not true, that means there are children which are not None and part of another key
                # Don't delete, pass deleted_self as false
                elif current.children.count(None) != len(current.children):
                    print("- - Don't delete node", current.char, ": has \ children")
                    deleted_self = False

                # Last case, we can just delete this node as well
                else:
                    print("- - Delete node", current.char, ": has no children")
                    current = None
                    deleted_self = True

            # If child was not deleted, then this current node cannot be deleted
            else:
                deleted_self = False

        return deleted_self


keys = ["the", "a", "there", "answer"]

t = Trie()

for word in keys:
    t.insert(word)

print(t.search("the"))

t.delete("the")

print(t.search("the"))