class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_num=0
        for index in range(0,len(s)-k+1):
            sub_string=s[index:index+k]
            count_a=sub_string.count('a')
            count_e=sub_string.count('e')
            count_i=sub_string.count('i')
            count_o=sub_string.count('o')
            count_u=sub_string.count('u')
            
            total_count=count_a+count_e+count_i+count_o+count_u
            max_num=max(total_count,max_num)

        return max_num    


        