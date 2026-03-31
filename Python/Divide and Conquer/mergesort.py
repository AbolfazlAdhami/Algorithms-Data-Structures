def merge(n,m,a,b):
        merge.cnt+=1
        
        c= [0] *(n+m)
        i = j = k = 0
        while i< n and j < m:
                if a[i] < b[j]:
                        c[k] = a[i]; i+=1;k+=1
                else:
                        c[k] = b[j]; j+=1;k+=1
        while i < n: c[k] = a[i]; i+=1;k+=1
        while j < m: c[k] = b[j]; j+=1;k+=1
        return c 


def mergesort(n,s):
        if n <=1:
                return s
        else: 
                m = n//2
                a = s[:m]; b =s[m:]
                a = mergesort(len(a),a)
                b = mergesort(len(b),b)
                return merge(len(a),len(b),a,b)
        
        
if __name__ == "__main__":
        merge.cnt = 0
        n = int(input())
        s = list(map(int,input().split()))
        s = mergesort(n,s)
        print(merge.cnt)
        print(*s)