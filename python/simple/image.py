from PIL import Image
import numpy as np

# secret
secret = [123,28,5,234,71,230,59]
pbox = [5, 1, 3, 7, 0, 6, 2, 4]

def P(text, pbox):
    block_size = len(pbox)

    # repeat the operation for each block
    num_blocks = len(text) // block_size  # integer division
    
    for i in range(num_blocks):
        start_positon = i*block_size
        P_swap(text, start_positon, block_size)

def P_swap(text, st_pos, block_size):
    shuffle = [ text[st_pos + p] for p in pbox ]
    for i in range(block_size):
        text[st_pos + i] = shuffle[i]

# xor
def XORACC(text, sec_init):    
    secret_size = len(sec_init)

    secret = sec_init.copy()
    acc = 0
    for i in range(len(text)):
        ch = text[i]
        key = secret[i % secret_size]
        xor_result = ch ^ key
        text[i] = xor_result
        # update secret 
        acc = (acc + ch) % 256
        secret[i % secret_size] = secret[i % secret_size] ^ acc

# xor
def XOR(text, secret):    
    secret_size = len(secret)

    for i in range(len(text)):
        ch = text[i]
        key = secret[i % secret_size]
        xor_result = ch ^ key
        text[i] = xor_result

def CAESAR(text):
    for i in range(len(text)):
        text[i] = ( text[i] + 100 ) % 256

# image loader
im = Image.open("img.jpg")
ab = np.asarray(im)
ar = ab.copy()

# gray scale
# for row in ar:
#     for col in row:
#         avg = (int(col[0]) + int(col[1]) + int(col[2])) // 3
#         col[0] = col[1] = col[2] = avg

b = ar.flatten()

# CAESAR(b)
# XOR(b, secret)
XORACC(b, secret)
# P(b, pbox)

size = ar.shape
res = b.reshape(size)

im2 = Image.fromarray(res)
im2.save("bin/out.jpg", "JPEG")


