def XOR(text, secret):    
    # store the result
    result = []
    secret_size = len(secret)

    for i in range(len(text)):
        ch = text[i]
        key = secret[i % secret_size]
        xor_result = chr( ord(ch) ^ key )
        result.append(xor_result)

    result_string = "".join(result)
    return result_string

# receive the user input
text = input("Type a phrase: ")

# secret
secret = [2,4,8,3,3]

# show encoded text
encoded = XOR(text, secret)
print("Encoded:", encoded)
