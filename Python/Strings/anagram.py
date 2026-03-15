def is_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    return True


if __name__ == "__main__":
    s1 = ['f', 'l', 'u', 's', 't', 'e', 'r']
    s2 = ['u', 'l', 'e', 's', 't',  'r', 'f']
    print(is_anagram(s1, s2))
