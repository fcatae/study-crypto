from PIL import Image
import numpy as np
import pyDes
import random

des = pyDes.des('secretke')
#des = pyDes.des('secretke', pyDes.CBC, "\31\1\20\7\100\20\45\15")

# secret
secret = [123,28,5,234,71,230,59]
pbox = [5, 1, 3, 7, 0, 6, 2, 4]
sbox = list(range(0, 255))
random.shuffle(sbox)

def SUBST(img):
    print(sbox)

    text = img.copy()
    for i in range(len(text)):
        text[i] = sbox[text[i]-1]

    return text

def DES(img):    
    res = des.encrypt(b.tobytes())
    
    return np.frombuffer(res, dtype=np.uint8)

def P(img, pbox):
    text = img.copy()
    block_size = len(pbox)

    # repeat the operation for each block
    num_blocks = len(text) // block_size  # integer division
    
    for i in range(num_blocks):
        start_positon = i*block_size
        P_swap(text, start_positon, block_size)
    return text

def P_swap(text, st_pos, block_size):
    shuffle = [ text[st_pos + p] for p in pbox ]
    for i in range(block_size):
        text[st_pos + i] = shuffle[i]

# xor
def XORACC(img, sec_init):    
    text = img.copy()
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
    return text

# xor
def XOR(img, secret):    
    text = img.copy()
    secret_size = len(secret)

    for i in range(len(text)):
        ch = text[i]
        key = secret[i % secret_size]
        xor_result = ch ^ key
        text[i] = xor_result
    return text

def CAESAR(img):
    text = img.copy()
    for i in range(len(text)):
        text[i] = ( text[i] + 50 ) % 256
    return text

# image loader
im = Image.open("img.jpg")
ab = np.asarray(im)
b = ab.flatten()

def save(b, name):
    size = ab.shape
    res = b.reshape(size)
    im2 = Image.fromarray(res)
    im2.save(name + ".jpg", "JPEG")


# save(b, "bin/plain")
save(SUBST(b), "bin/subst")
# save(DES(b), "bin/des")
# save(CAESAR(b), "bin/caesar")
# save(XOR(b, secret), "bin/xor")
# save(XORACC(b, secret), "bin/xoracc")
# save(P(b, pbox), "bin/perm")
