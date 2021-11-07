def color(slicetxt, array):
    for paint in range(0, len(slicetxt)):
        if slicetxt[paint] in array:
            print(f'\033[31m{slicetxt[paint]}\033[m', end='')
            array.remove(slicetxt[paint])
        else:
            print(f'{slicetxt[paint]}', end='')


def catch(txt, wanted):
    select = list(wanted)
    got = []
    result = []
    for x in range(0, len(select)):
        for y in range(0, len(txt)):
            if txt.find(select[x], y, y + 1) not in got:
                if txt.find(select[x], y, y + 1) > -1:
                    try:
                        got.append(txt.find(select[x], y, y + 1))
                        result.append(txt[got[x]])
                        break
                    except IndexError:
                        break

    if len(select) == len(result):
        txtFinal = ''.join(result)
        print(f'{txtFinal}')
        color(txt, result)
    else:
        print('Cannot use these letters')


catch('text', 'xet')
