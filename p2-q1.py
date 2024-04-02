# محمدرضا محمدی درویشانی
f = open ("mysterious.txt" , "r")
text = f.read()
f.close()

def decrypt_clue(text): 

    key_words = ['False','await','else','import','pass','None','break','except','in','raise','True','class','finally','is','return','and','continue','for','lambda','try','as','def','from','nonlocal','while','assert','del','global','not','with','async','elif','if','or','yield']
    new_list = []

    for word in key_words :
        if word in text:
            new_list.append(word)
    return new_list

print(decrypt_clue(text))
