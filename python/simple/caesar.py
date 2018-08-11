def caesar(ch):
    subst = ['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','a','b','c']

    if(ch >= 'a' and ch <= 'z'):
        return subst[ord(ch) - ord('a')]

    return ch

text = input("Type a phrase: ")

encoded = "".join([ caesar(ch) for ch in text ])

print(encoded)