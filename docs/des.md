
# Criptografia #

Cifra de Cesar
https://en.wikipedia.org/wiki/Caesar_cipher#/media/File:Caesar_cipher_left_shift_of_3.svg

Shannon
http://netlab.cs.ucla.edu/wiki/files/shannon1949.pdf

confusion: relação entre plain text e o codificado.
exemplo: substituição

    exemplo da imagem.

non-linear using Substitution Box (S-BOX)

    exemplo da imagem.


# Permutação #

diffusion: influencia entre os bits do plain text

    r olzur hvxd vreuh d phvd
    X  X  X  X X  X  X X  X X

outra coisa que podemos descobrir sao as vogais.

    r olzur hvxd vreuh d phvd
    o livro esta sobre a mesa

Exemplo de letras seguidas:

    quimico queijo quiabo queimado quebrado querer quintal
    tylplfr tyhlmr tylder tyhlpdgr tyheudgr tyhuhu tylqxdo

Exemplos:

    fabricio
    carofibi

Exemplo:

    A suprema arte da guerra é subjugar o inimigo sem lutar
    r umAespe rda atr uaargebésu j u a ngiro mgeisioa u.mrlt

Note que o segredo é descobrir o "período de repetição". Se
descobrimos que é 8, então podemos agrupar:

    A suprem|a arte d|a guerra| é subju|gar o in|imigo se|m lutar.
    r umAesp|e rda at|r uaarge|bésu j u| a ngiro| mgeisio|a u.mrlt

Podemos descobrir que o Permutation Box é 

    [5, 1, 3, 7, 0, 6, 2, 4]


RNG (Random Number Generator)

Pseudo/True RNG

(XOR)

A suprema arte da guerra é subjugar o inimigo sem lutar.
Encoded: C${vspaeb#cv|f#fe(dvgvzb#ë${vahqobq"k(jmkiadl"wmn#nq|bq,

Visualmente mais dificil que a cifra de Cesar. no entanto nao. sofre do mesmo 
problema, sendo que a grande dificuldade é descobrir o tamanho da chave usada.

password = é uma forma de criar um seed.



Data Encryption Standard
History
* 1974: US Government Standard
* 1977-1998: US Standard
* best studied cipher in the world
* Current status: insecure (key too short) - 3DES is very secure
* block cipher (instead of stream cipher , RC4)

Feistel Network - video do YouTube

DES usa a permutação. Entretanto, o objetivo não é criptografar, mas melhorar
a distribuição dos bits.

57, 49, 41, 33, 25, 17, 9,
1, 58, 50, 42, 34, 26, 18,
10, 2, 59, 51, 43, 35, 27,
19, 11, 3, 60, 52, 44, 36,
63, 55, 47, 39, 31, 23, 15,
7, 62, 54, 46, 38, 30, 22,
14, 6, 61, 53, 45, 37, 29,
21, 13, 5, 28, 20, 12, 4

**************************************

paradox?
size of key = memorized = smaller as possible


***************************************


AES Advanced Encryption Standard

1997 AES by NIST

Usages:
* Encryption
* Stream Cipher
* PRNG
* Hash Function
* MAC


Block Cipher - Modes of Operation

- ECB
- CBC (block cipher)
- OFB (stream cipher)


