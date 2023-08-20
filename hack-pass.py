import sys
import hashlib

charToNumber = {
    'o': '0', 'i': '1', 'l': '1', 'e': '3'
}


def hashWithSha1(word):
    m = hashlib.sha1(word.encode()).hexdigest()
    return m


def hashWithMd5(word):
    m = hashlib.md5(word.encode()).hexdigest()
    return m


def isSpecialChar(char):
    return char.lower() in ('o', 'i', 'l', 'e')


def isNumber(char):
    return char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


def getPossiblyCases(char):
    amount_cases = 2
    if isSpecialChar(char):
        amount_cases = 3
    if isNumber(char):
        amount_cases = 1
    return amount_cases


def getCharPossiblyCases(char, case):
    if case == 0:
        return char
    elif case == 1:
        return char.upper()
    else:
        return charToNumber[char]


def checkMatchingTarget(word, target):
    hashSha1 = hashWithSha1(word)
    hashMd5 = hashWithMd5(word)
    if (hashSha1 == target or hashMd5 == target):
        return True
    else:
        return False


def generateAllSubstring(word, target, length, current_length, current_word):
    is_correct = False
    if (current_length == length):
        if (checkMatchingTarget(current_word, target)):
            print("Result: " + current_word)
            return True
        return False

    else:
        amount_cases = getPossiblyCases(word[current_length])
        for i in range(amount_cases):
            convert_char = getCharPossiblyCases(word[current_length], i)
            new_current_word = current_word + convert_char
            is_correct = generateAllSubstring(word, target, length,
                                              current_length + 1, new_current_word)
            if is_correct:
                return True
    return is_correct


def setResult(word):
    global result
    result = word


def main():
    print("Hacking Passwords")
    # if len(sys.argv) != 2:
    #     print("Usage: python3 hack-pass.py <inputPath>")
    #     return

    path_in = "data/10k-most-common.txt"
    # path_in = sys.argv[1]
    # path_out = sys.argv[2]
    file_input = open(path_in, "r")
    target_value = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7"
    count = 0

    for line in file_input:
        # if count == 1:
        #     break
        word = line.lower().strip()
        variation = list(word)
        # print(variation)
        is_correct = generateAllSubstring(
            variation, target_value, len(word), 0, "")
        if is_correct:
            break
        # count += 1

    file_input.close()

    # print("Result: " + result)


if __name__ == '__main__':
    main()
