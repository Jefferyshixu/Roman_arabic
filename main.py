# COMP9021 24T1
# Assignment 1 *** Due Monday 25 March (Week 7) @ 9.00am

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
def please_convert():
    user_input = input('How can I help you? ')
    words = user_input.split()
    if len(words) == 3 and words[0] == "Please" and words[1] == "convert":
        answer = convert1(words[2])
        if answer != None:
            print("Sure! It is " + str(answer))
        else:
            print("Hey, ask me something that's not impossible to do!")
    elif len(words) == 4 and words[0] == "Please" and words[1] == "convert" and words[3] == "minimally":
        answer = convert3(words[2])
        if answer != None:
            pattern, value = answer
            print("Sure! It is " + str(value) + " using " + pattern)
        else:
            print("Hey, ask me something that's not impossible to do!")
    elif len(words) == 5 and words[0] == "Please" and words[1] == "convert" and words[3] == "using":
        answer = convert2(words[2], words[4])
        if answer != None:
            print("Sure! It is " + str(answer))
        else:
            print("Hey, ask me something that's not impossible to do!")
    else:
        print("I don't get what you want, sorry mate!")

def convert1(word):
    if word.isdigit() and 0 < int(word) < 4000 and word[0]!=0:
        return a_to_r(word)
    elif word.isalpha():  # valid Roman Number
        return r_to_a(word)
    else:
        return None

def convert2(word,rules):
    if word.isdigit() and word[0] != "0":
        return a_to_r(word, rules)
    elif word.isalpha():
        return r_to_a(word, rules)
    else:
        return None


def get_pair(rules):
    char_to_number = {}
    number_to_char = {}
    count = 0
    value = 1
    for char in rules[::-1]:
        char_to_number[char] = value
        number_to_char[value] = char
        if count % 2 == 0:
            value *= 5
        else:
            value *= 2
        count += 1
    return char_to_number, number_to_char

def r_to_a(word,rules="MDCLXVI"):
    if not (set(word) <= set(rules)):
        return None
    char_to_number, number_to_char = get_pair(rules)
    value = 0
    for index in range(len(word) - 1):
        if char_to_number[word[index]] < char_to_number[word[index + 1]]:
            value -= char_to_number[word[index]]
        else:
            value += char_to_number[word[index]]
    value += char_to_number[word[-1]]

    if a_to_r(value,rules) == word:
        return value



def a_to_r(word, rules="MDCLXVI"):
    char_to_number, number_to_char = get_pair(rules)
    result = ""
    number = int(word)
    for char in rules:
        result += char * (number // char_to_number[char])
        number = number % char_to_number[char]
    new_result = ""
    index = 0
    while index < (len(result) - 3):

        if len(set(result[index: index + 4])) == 1:
            value = char_to_number[result[index]]
            if index == 0 or char_to_number[result[index - 1]] // value != 5:
                bigger_value = number_to_char.get(value * 5)
            else:
                bigger_value = number_to_char.get(value * 10)
                new_result = new_result[:-1]
            if bigger_value is None:
                return None
            new_result += result[index] + bigger_value
            index += 4
        else:
            new_result += result[index]
            index += 1
    new_result += result[index:]
    return new_result



def convert3(word):
    if not word.isalpha():
        return None
    next_rep = 1
    next_non_rep = 5

    result = {}
    index = len(word) - 1
    value = 0

    while index >= 0:
        char = word[index]
        left_index = word.find(char)

        if char in result:
            if result[char] != next_rep / 10:
                return None
            else:
                value += result[char]
                index -= 1
                continue

        if left_index == index:  # 从左边数第一个
            if index != len(word) - 1:  # 若是最后一个字符
                previous = word[index + 1]
                if word.count(previous) == 1:  # 若前一个字符只出现一次
                    if next_non_rep > next_rep:
                        result[char] = next_rep
                        next_rep *= 10
                        value += result[char]
                    else:
                        result[char] = next_non_rep
                        next_non_rep *= 10
                        result[previous], result[char] = result[char], result[previous]
                        value += 3*result[char]
                    index -= 1
                    continue



            if next_rep > next_non_rep:
                result[char] = next_non_rep
                value += next_non_rep
                next_non_rep *= 10
            else:
                result[char] = next_rep
                value += next_rep
                next_rep *= 10

        else:
            char_number = len(set(word[left_index: index + 1]))
            if char_number == 1 and index - left_index <= 2:  # AAA
                result[char] = next_rep
                value += result[char]*(index - left_index + 1)
                if next_rep > next_non_rep:
                    next_non_rep *= 10
                next_rep *= 10
            elif char_number == 2 and index - left_index <= 4 and word.count(word[index - 1]) == 1:
                result[word[index - 1]] = next_rep
                result[word[index]] = next_rep * 10
                value += result[word[index]] * (index - left_index) - result[word[index - 1]]

                next_rep *= 100
                next_non_rep = next_rep // 2
            elif char_number == 3 and index - left_index == 3:
                result[word[index - 1]] = next_rep
                result[word[index]] = next_rep * 10
                if word.count(word[index - 2]) == 1:
                    result[word[index - 2]] = result[word[index]] * 5
                    next_rep *= 100  # 10000, 5000, 1000, 100
                    next_non_rep = next_rep * 5
                else:
                    result[word[index - 2]] = result[word[index - 1]] * 10
                    next_non_rep = result[word[index - 2]] * 5
                    next_rep *= 1000
                value += result[word[index - 2]] - result[word[index - 1]]

            else:
                return None


        index = left_index - 1

    pairs = sorted(result.items(), key=lambda x: x[1], reverse=True)
    pattern = pairs[0][0]
    for index in range(1, len(pairs)):
        if pairs[index - 1][1] / pairs[index][1] == 10:
            pattern += "_" + pairs[index][0]
        else:
            pattern += pairs[index][0]

    return pattern, value

please_convert()