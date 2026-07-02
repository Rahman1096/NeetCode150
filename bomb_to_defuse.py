class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        result=[0]*n
        #when k=0
        if k==0:
            return result
        #other cases
        total=sum(code[1:k+1])
        result[0]=total
        if k>0:

            for i in range(1,n):
                total =total -code[i]+code[(i+k) % n]
                result[i]=total
        if k<0:
            total = sum(code[n+k:n])
            result[0]=total
            for i in range(1,n):
                total = total - code[(i+k-1) % n] + code[(i-1) % n]                
                result[i]=total
        return result        

