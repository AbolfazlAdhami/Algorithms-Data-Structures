def is_palindrome(s):
        return True if s == reverse(s) else False



def reverse(data):
        data=list(data)
        
        start_index=0
        end_index=len(data)-1
        
        while end_index > start_index :
                
                data[start_index],data[end_index] = data[end_index],data[start_index]
                start_index+=1
                end_index-=1
                
        return ''.join(data)
                
                
print(is_palindrome('madam'))
print(is_palindrome('kevin'))
print(is_palindrome('bob'))
print(is_palindrome('radar'))
