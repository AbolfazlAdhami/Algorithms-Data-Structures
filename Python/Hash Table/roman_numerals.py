def solve(roman):
        T= { 'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        s=0
        
        for i in range(len(roman)-1):
                if T[roman[i]] < T[roman[i+1]]:
                        s -= T[roman[i]]
                else:
                        s += T[roman[i]]
                        
        s+=T[roman[i+1]]
        
        return s 

N=input()
print(solve(N))
             