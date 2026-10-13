class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maximum = 0

        for sentence in sentences:
            words = sentence.split()

            if len(words)> maximum:
                maximum = len(words)

        return maximum