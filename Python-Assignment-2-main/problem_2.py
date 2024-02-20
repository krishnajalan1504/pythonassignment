#2.	Convert all the numbers in the file2.txt to text. 
#Ex: This file has numbers 1,2
#Convert it to : This file has numbers one,two

def numtoword(num):
    if num == 0:
        return " zero "
    
    arr = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = ""
    while num != 0:
        small_ans = arr[num % 10]
        result = small_ans + result
        num = int(num / 10)
    return result


def convert_numbers_to_words(input_text):
    result = ""
    is_inside_number = False

    for char in input_text:
        if char.isdigit():
            if not is_inside_number:
                result += numtoword(int(char))
                is_inside_number = True
            else:
                result += numtoword(int(char)).rstrip()
        else:
            result += char
            is_inside_number = False

    return result

with open("f2.txt", "r") as f:
    content = f.read()

converted_content = convert_numbers_to_words(content)

with open("new_f2.txt", "w") as of:
    of.write(converted_content)

print("Conversion complete. Check 'new_f2.txt' for the result.")
