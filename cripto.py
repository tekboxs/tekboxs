def atbash(txt):
    result = ''
    txt = list(txt)
    for passer in range(len(txt)):
        cur_var = str(txt[passer])
        if cur_var.isalpha():
            if cur_var.islower():
                i = abs(ord('a') - ord(txt[passer]))
                result += chr(((25 * i + 25) % 26) + ord('a'))
            elif cur_var.isupper():
                i = abs(ord('A') - ord(txt[passer]))
                result += chr(((25 * i + 25) % 26) + ord('A'))
        else:
            result += txt[passer]
    return result


text = input('Digite o texto: ')
print('Resultado =', atbash(text))
