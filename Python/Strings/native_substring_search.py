def native_search(pattern,text):
        m=len(pattern)
        n=len(text)
        
        for i in range(n-m+1):
                j = 0
                
                while j <m:
                        if text[i+j] != pattern[j]:
                                break
                        
                        j += 1
                        
                        if j == m :
                                
                                print('Found a match at index %s' % i)
                                
if __name__ == '__main__':
        native_search('abcd','abcdeefababcd')
                                