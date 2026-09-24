print("------ Task 2.4 ------")
english_freq = {
        'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70,
        'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15,
        'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51,
        'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06,
        'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97,
        'z': 0.07,
    }


def score_text(text):
        counts = {}
        for ch in text:
            if ch.isalpha():
                ch = ch.lower()
                if ch in counts:
                    counts[ch] = counts[ch] + 1
                else:
                    counts[ch] = 1

        total = 0
        for ch in counts:
            total = total + counts[ch]

        if total == 0:
            return 999999

        score = 0
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for ch in alphabet:
            expected = english_freq[ch] / 100 * total #how many times this letter woul appear if it propre english 
            if ch in counts:
                observed = counts[ch] ## how many times this letter appears 
            else:
                observed = 0
            if expected > 0: ## to not divide per 0
                score = score + (observed - expected) ** 2 / expected #chi-squared statistic

        return score


def split_into_piles(ciphertext,key_length):
        letters = []
        for ch in ciphertext:
            if ch.isalpha():
                letters.append(ch.lower())# add an item to the end of a list. so the lower case char 
        piles = []
        for i in range(key_length):
            piles.append("")
        for i in range(len(letters)):
            pile_number=i % key_length
            piles[pile_number] = piles[pile_number] + letters[i]
        return piles

    #  Crack one pile as a Caesar cipher 
def crack_pile(pile):
        best_shift = 0
        best_score = 999999

        for shift in range(26):
            # Build a one-letter key from this shift and decrypt the pile
            key_letter = chr(shift + ord('a'))
            candidate = vigenere(pile, key_letter, decrypt=True)

            s = score_text(candidate)
            if s < best_score:
                best_score = s
                best_shift = shift

        return best_shift

    #  Recover the key 
def recover_key(ciphertext, key_length):
        piles = split_into_piles(ciphertext, key_length) # result alist of strings 

        key = ""
        for pile in piles:
            shift = crack_pile(pile)
            key = key + chr(shift + ord('a'))

        return key


    # 
ciphertext = input("Ciphered text: ")
key_length = int(input("Key length: "))

key = recover_key(ciphertext, key_length)
print("Recovered key:", key)

plaintext = vigenere(ciphertext, key, decrypt=True)
print("Plaintext    :", plaintext)
