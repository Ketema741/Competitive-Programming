class Solution(object):
    def sortSentence(self, s):
        Words = s.split(' ')
        sorted_word = [0] * len(Words)
        sentence = ""
        for i in Words:
            wor_index = int(i[-1])
            sorted_word[wor_index-1] = i[:-1]
        for word in sorted_word:
            sentence += " " +word
        return sentence[1:]
        """
        :type s: str
        :rtype: str
        """
        