def coloring(original, used):
    arrow_array, arrow_array2, letters_array = [], [], []
    cont = 1
    word = "".join(used)
    last_cont = 0
    for index in range(0, len(original)):

        if original[index] in used:
            if str(word.find(original[index]) + 1) in arrow_array:
                arrow_array.insert(index, str(last_cont + 1))

                last_cont += 1
            else:
                arrow_array.insert(index, str(word.find(original[index]) + 1))

                last_cont = word.find(original[index]) + 1
            used.remove(original[index])

            cont += 1
            arrow_array2.insert(index + 1, "↓")

            letters_array.append(f"\033[31m{original[index]}\033[m")
        else:

            arrow_array.insert(index, " ")
            arrow_array2.insert(index, " ")
            letters_array.append(original[index])

    arrow = " ".join(arrow_array)
    arrow2 = " ".join(arrow_array2)
    letters = " ".join(letters_array)
    result_done = f"{arrow}\n{arrow2}\n{letters}"
    return result_done


def catch(input_objetive, input_raw):
    input_array_raw, input_array_objetive = list(input_raw), list(input_objetive)

    current_array, not_used_letter = [], []
    for letter_raw in input_array_raw:
        if letter_raw in input_objetive:
            if not current_array.count(letter_raw) + 1 > input_objetive.count(letter_raw):
                current_array.append(letter_raw)
        else:
            not_used_letter.append(letter_raw)
    if len(input_array_objetive) == len(current_array):
        return coloring(
            input_array_raw,
            input_array_objetive)

    else:

        return "Cannot use these letters"
    # print(current_array, not_used_letter)


raw_word = input('Input your word or phrase: ')
objective = input('Input the wanted word(s): ')
print('\n'*2, 'The result is:', '\n')
end_result = catch(objective, raw_word)
print(end_result)
