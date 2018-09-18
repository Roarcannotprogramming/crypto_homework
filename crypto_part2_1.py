from encrypo import text


def clean_text(text):
    text = text.replace('‡', 'a')
    text = text.replace('†', 'b')
    text = text.replace(')', 'c')
    text = text.replace('*', 'd')
    text = text.replace('.', 'e')
    text = text.replace(';', 'f')
    text = text.replace('¶', 'g')
    text = text.replace(']', 'h')
    text = text.replace('(', 'i')
    text = text.replace('?', 'j')
    text = text.replace(':', 'k')
    text = text.replace('-', 'l')
    text = text.replace('0', 'm')
    text = text.replace('1', 'n')
    text = text.replace('2', 'o')
    text = text.replace('3', 'p')
    text = text.replace('4', 'q')
    text = text.replace('5', 'r')
    text = text.replace('6', 's')
    text = text.replace('7', 't')
    text = text.replace('8', 'u')
    text = text.replace('9', 'v')
    return text


def get_plain(text):
    text = text.replace('u', 'E')
    text = text.replace('f', 'T')
    text = text.replace('q', 'H')
    return text


def get_times(text):
    dic = {}
    for letter in range(ord('a'), ord('v')+1):
        letter = chr(letter)
        dic[letter] = text.count(letter)
    return dic


cleand_text = clean_text(text)

plain_text = get_plain(cleand_text)

times_dic = get_times(cleand_text)

print(sorted(times_dic.items(), key=lambda x: x[1]))

print(plain_text)

print(plain_text.split('THE'))

print(cleand_text)

# print(len(text))


# times_dic_zip = zip(times_dic.values, times_dic.keys)

# print(times_dic_zip)

# print(ord('a')+1)

# print(clean_text(text))

print(get_times(clean_text(text)))