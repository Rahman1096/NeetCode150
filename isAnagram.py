class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s,freq_t={},{}
        for each_char in s:
            freq_s[each_char]=freq_s.get(each_char,0)+1 
        for each_char in t:
            freq_t[each_char]=freq_t.get(each_char,0)+1
        #if lengths of  maps are different string can not be anagram  
        if len(freq_s)!=len(freq_t):
            return False
        else:
            #lengths of maps are equal so we will now check individual entries
            for entry in freq_s.keys():
                if freq_s.get(entry)!=freq_t.get(entry):
                    return False
            #otherwie return True coz all edge cases handled 
        return True