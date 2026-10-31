class Solution:
    def __init__(self):
        self.elements = []

    def isValid(self, s: str) -> bool:
        patterns = {
            ")": "(", 
            "}": "{", 
            "]": "["
        }

        for char in s:
            if char in patterns:
                if not self.elements or self.elements[-1] != patterns[char]:
                    return False
                self.elements.pop()
            else:
                self.elements.append(char)

        return not self.elements
