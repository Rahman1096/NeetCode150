class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        # finding frequency of each char 
        for char in s:
            freq[char]=freq.get(char,0)+1
        # finding the most frequent char so that we can use it for replacement
        most_freq_char = max(freq, key=freq.get)
        for char in s:
            if k==0:
                break 
            if char!=most_freq_char:
                char=most_freq_char
                k -=1
        #finding most frequent substring
        length_most_freq=0
        left,right=0,0

        for i in range(len(s)):
            while s[left]==s[right]:
                right  +=1
            #getting max length    
            length_most_freq=max(length_most_freq,right-left)
            #again setting left and right for new substring if there is any
            left , right=i,i
        return length_most_freq      