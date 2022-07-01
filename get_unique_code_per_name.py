def get_code(first_name, last_name):
    def count_vw_cs(tgt_str):
        vowels = 'AEIOUY'
        consonants = 'BCDFGJKLMNPQSTVXZHRW'
        c, v, = 0, 0
        c_list, v_list = [], []
        for char in tgt_str.upper():
            if char in vowels:
                v += 1
                v_list.append(char)
            elif char in consonants:
                c += 1
                c_list.append(char)
            else:
                pass
        return [c, v, c_list, v_list]

    cv_last_name = count_vw_cs(last_name.upper())
    code = ''

    if cv_last_name[0] >= 3 and len(last_name) >= 3:
        code += ''.join(cv_last_name[2][0:3])
    elif cv_last_name[0] < 3 and len(last_name) >= 3:
        code += ''.join(cv_last_name[2][0:] + cv_last_name[3][0:3-len(cv_last_name[2])])
    elif len(last_name) < 3:
        code += ''.join(cv_last_name[2][0:] + cv_last_name[3][0:]) + 'X' * (3 - len(last_name))
    else:
        return False

    cv_first_name = count_vw_cs(first_name.upper())

    if cv_first_name[0] == 3 and len(first_name) >= 3:
        code += ''.join(cv_first_name[2][0:])
    elif cv_first_name[0] > 3 and len(first_name) >= 3:
        code += ''.join(cv_first_name[2][0]).join(cv_first_name[2][2]).join(cv_first_name[2][3])
    elif cv_first_name[0] < 3 and len(first_name) >= 3:
        code += ''.join(cv_first_name[2][0:]).join(cv_first_name[3][0:3-len(cv_first_name[2])])
    elif len(first_name) < 3:
        code += ''.join(cv_first_name[2][0:]).join(cv_first_name[3][0:]) + 'X' * (3 - len(first_name))
    else:
        return False

    return code


print(get_code('Mickey', 'Mouse'))

