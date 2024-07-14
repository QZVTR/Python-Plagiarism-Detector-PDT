import math


class CosineSim:
    def __init__(self):
        pass

    def tokenizeCode(self, code):
        # Split the code into tokens
        return code.split()

    def computeTF(self, tokenizedCode):
        # Compute term frequency (TF) for each token in the code snippet
        tf = {}
        totalTokens = len(tokenizedCode)
        for token in tokenizedCode:
            tf[token] = tf.get(token, 0) + 1
        for token, freq in tf.items():
            tf[token] = freq / totalTokens
        return tf

    def computeIDF(self, codeSnippets):
        # Compute inverse document frequency (IDF) for each unique token in the collection of code snippets
        idf = {}
        totalSnippets = len(codeSnippets)
        for snippet in codeSnippets:
            uniqueTokens = set(self.tokenizeCode(snippet))
            for token in uniqueTokens:
                idf[token] = idf.get(token, 0) + 1
        for token, freq in idf.items():
            idf[token] = math.log(totalSnippets / (freq + 1))
        return idf

    def computeCosineSimilarity(self, fileName1, fileName2):
        codeSnippets = [self.readFile(fileName1), self.readFile(fileName2)]
        tokenizedSnippets = [self.tokenizeCode(snippet) for snippet in codeSnippets]

        # Compute TF-IDF matrix
        tfidfMatrix = []
        idf = self.computeIDF(codeSnippets)
        for tokenizedSnippet in tokenizedSnippets:
            tf = self.computeTF(tokenizedSnippet)
            tfidfVector = [tf.get(token, 0) * idf[token] for token in tokenizedSnippet]
            tfidfMatrix.append(tfidfVector)

        # Compute cosine similarity
        cosineSim = 0
        if len(tfidfMatrix) == 2:
            dotProduct = sum(
                tfidfMatrix[0][i] * tfidfMatrix[1][i]
                for i in range(min(len(tfidfMatrix[0]), len(tfidfMatrix[1])))
            )
            norm1 = sum(val**2 for val in tfidfMatrix[0])
            norm2 = sum(val**2 for val in tfidfMatrix[1])
            if norm1 != 0 and norm2 != 0:
                cosineSim = dotProduct / (math.sqrt(norm1) * math.sqrt(norm2))

        return cosineSim

    def readFile(self, file_name):
        with open(file_name, "r") as file:
            code = file.read()

        return code
