import re


class NgramComp:
    def __init__(self):
        pass

    def tokeniseCode(self, code):
        # Split the code into tokens
        return code.split()

    def generateNgrams(self, tokens, n):
        # Generate n-grams from the tokens
        return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]

    def jaccardDistance(self, set1, set2):
        # Calculate Jaccard distance between two sets
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return 1 - (intersection / union) if union > 0 else 0

    def getNgramsFromFile(self, fileName, n):
        with open(fileName, "r") as file:
            code = file.read()

        tokens = self.tokeniseCode(code)
        return set(self.generateNgrams(tokens, n))

    def jaccardSimilarity(self, fileName1, fileName2, n):
        ngramsCode1 = self.getNgramsFromFile(fileName1, n)
        ngramsCode2 = self.getNgramsFromFile(fileName2, n)
        return 1 - self.jaccardDistance(ngramsCode1, ngramsCode2)
