def single_root_words(root_word, *other_words):
    root_word = root_word.lower()
    same_words = []
    for i in other_words:
        i = i.lower()
        if root_word in i or i in root_word:
            same_words.append(i)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('disablement', 'able', 'mable', 'disable', 'bagel')
print(result1)
print(result2)
