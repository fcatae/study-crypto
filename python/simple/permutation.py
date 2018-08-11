def P(text, pbox):
    block_size = len(pbox)
    padding = "." * (block_size-1)  
    padded_text = text + padding

    # store the result
    result = []

    # repeat the operation for each block
    num_blocks = len(padded_text) // block_size  # integer division
    
    for i in range(num_blocks):
        start_positon = i*block_size
        end_positon = start_positon + block_size
        text_block = padded_text[start_positon : end_positon]
        result.append(P_block(text_block))

    result_string = "|".join(result)
    return result_string

def P_block(text):
    shuffle = [ text[p] for p in pbox ]
    return "".join(shuffle)


# receive the user input
text = input("Type a phrase: ")

# permutation box
pbox = [5, 1, 3, 7, 0, 6, 2, 4]

# show encoded text
encoded = P(text, pbox)
print("Encoded:", encoded)
