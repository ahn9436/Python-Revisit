nor_word = ("be", "because", "see", "the", "okay", "are", "you", "without", "why", "see you", "ate",
           "great", "mate", "wait", "later", "tomorrow", "for", "before", "once", "and", "Your","your",
           "you're", "You're","As far as I know", "As soon as possible", "At the moment", "Be right back",
           "By the way", "For your information", "In my humble opinion", "In my opinion",
           "Laughing out loud", "Oh my god", "Rolling on the floor laughing", "Talk to you later")

ab_word = ("b", "cuz", "c", "da", "ok", "r", "u", "w/o", "y", "cu", "8", "gr8", "m8", "w8", "l8r",
           "2mro", "4", "b4", "1ce", "&", "ur","ur", "ur","ur","afaik", "ASAP", "atm", "brb", "btw",
            "FYI", "imho","imo", "lol", "omg", "rofl", "ttyl")


def textese(s):
    text = s
    for i in range(-1, -len(nor_word)-1, -1):
        if nor_word[i] in text:
            text = text.replace(nor_word[i], ab_word[i])        
        
    return text

def untextese(s):
    text = s.split(" ")
    for i in range(0, len(text)):
        for j in range(0, len(ab_word)):
            if text[i] == ab_word[j]:
                text[i] = nor_word[j]

    text = " ".join(text)
                
    return text

t = textese("Oh my god As soon as possible but because you are here and ate a lot of Salmon")
print(t)

b = untextese(t)
print(b)