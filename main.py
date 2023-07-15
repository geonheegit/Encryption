mode = int(input("암호화는 '1'을, 복호화는 '2'를 타이핑 해주세요. : "))

code = []
decode = []
small_index = 0
big_index = 0

alphabet_list_small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

alphabet_list_big = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                     "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                     "W", "X", "Y", "Z"]
if mode == 1:

    given_words = list(input("암호화할 문자열 (영어)를 입력하세요: "))

    for i in given_words:
        if i.islower():

            if alphabet_list_small.index(i) + 6 >= 26:
                small_index = alphabet_list_small.index(i) - 20
                code.append(alphabet_list_small[small_index])
            else:
                small_index = alphabet_list_small.index(i) + 6
                code.append(alphabet_list_small[small_index])

        elif i.isupper():
            if alphabet_list_big.index(i) + 6 >= 26:
                big_index = alphabet_list_big.index(i) - 20
                code.append(alphabet_list_big[big_index])
            else:
                big_index = alphabet_list_big.index(i) + 6
                code.append(alphabet_list_big[big_index])

        elif i == " ":
            i = '='
            code.append(i)

    print("암호화된 문자열: " + ''.join(code))

elif mode == 2:
    given_encryp = list(input("복호화할 문자열을 입력하세요: "))

    for i in given_encryp:
        if i.islower():

            if alphabet_list_small.index(i) - 6 < 0:
                small_index = alphabet_list_small.index(i) + 20
                decode.append(alphabet_list_small[small_index])
            else:
                small_index = alphabet_list_small.index(i) - 6
                decode.append(alphabet_list_small[small_index])

        elif i.isupper():
            if alphabet_list_big.index(i) - 6 < 0:
                big_index = alphabet_list_big.index(i) + 20
                decode.append(alphabet_list_big[big_index])
            else:
                big_index = alphabet_list_big.index(i) - 6
                decode.append(alphabet_list_big[big_index])

        elif i == "=":
            i = ' '
            decode.append(i)
    print("복호화된 문자열: " + ''.join(decode))