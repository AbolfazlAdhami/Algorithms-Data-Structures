"""_
Complete the solution so that the function will break up camel casing, using a space between words.

        "camelCasing"  =>  "camel Casing"
        "identifier"   =>  "identifier"
        ""             =>  ""
        "breakCamelCase" => "break Camel Case"
Link:https://www.codewars.com/kata/5208f99aee097e6552000148/train/python        
"""
import re


def solution(s):
    return ' '.join(re.findall(r'[A-Z][a-z]*|[a-z]+', s))


print(solution("camelCasing"))
print(solution("identifier"))
print(solution("breakCamelCase"))
