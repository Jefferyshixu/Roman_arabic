import subprocess

commands = ["echo '' | python3 roman_arabic.py",
 'echo Please convert 4567 2345 | python3 roman_arabic.py',
 'echo Please convert 123 using | python3 roman_arabic.py',
 "echo 'Please convert 519 minimally using '| python3 roman_arabic.py",
 'echo Please convert 519 using ABCDE minimally | python3 roman_arabic.py',
 'echo Please convert 1045 minimal | python3 roman_arabic.py',
 'echo Please convert 30 THCO THCO | python3 roman_arabic.py',
 'echo Please convert 51 using using ABCDE | python3 roman_arabic.py',
 'echo Please please 51 using DABCDE | python3 roman_arabic.py',
 'echo Please_concert please_convert E using E | python3 roman_arabic.py',
 'echo Please convert 0 | python3 roman_arabic.py',
 'echo Please convert 010 | python3 roman_arabic.py',
 'echo Please convert 4000 | python3 roman_arabic.py',
 'echo Please convert VV | python3 roman_arabic.py',
 'echo Please convert IVI | python3 roman_arabic.py',
 'echo Please convert IVX | python3 roman_arabic.py',
 'echo Please convert 1 | python3 roman_arabic.py',
 'echo Please convert 69 | python3 roman_arabic.py',
 'echo Please convert 307 | python3 roman_arabic.py',
 'echo Please convert 1110 | python3 roman_arabic.py',
 'echo Please convert 2009 | python3 roman_arabic.py',
 'echo Please convert 3060 | python3 roman_arabic.py',
 'echo Please convert 3984 | python3 roman_arabic.py',
 'echo Please convert I | python3 roman_arabic.py',
 'echo Please convert LXIX | python3 roman_arabic.py',
 'echo Please convert CCCVII | python3 roman_arabic.py',
 'echo Please convert MCX | python3 roman_arabic.py',
 'echo Please convert MMIX | python3 roman_arabic.py',
 'echo Please convert MMMLX | python3 roman_arabic.py',
 'echo Please convert MMMCMLXXXIV | python3 roman_arabic.py',
 'echo Please convert aba using ab | python3 roman_arabic.py',
 'echo Please convert LI using IPQL | python3 roman_arabic.py',
 'echo Please convert ABCDEF using XYZBCDEF | python3 roman_arabic.py',
 'echo Please convert ABCDEFGHIJKLMNOPQRST using AbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStT | python3 roman_arabic.py',
 'echo Please convert 098 using zaqws | python3 roman_arabic.py',
 'echo Please convert 4000 using lkjhgfd | python3 roman_arabic.py',
 'echo Please convert 4 using lL | python3 roman_arabic.py',
 'echo Please convert 7 using asdfghjklpoiuyt | python3 roman_arabic.py',
 'echo Please convert 957 using mMnNjJkKtTgGdDqQ | python3 roman_arabic.py',
 'echo Please convert 55555 using plmnbqwert | python3 roman_arabic.py',
 'echo Please convert 936936936936936 using pqowieurytLAKSDJFHGzmxncbvQPWOEIRUTY | python3 roman_arabic.py',
 'echo Please convert 1020304050607080901 using qwertyuioplkjhgfdsaZXCVBNMLKJHGFDSAQWERTYUIOPzxcvbnm | python3 roman_arabic.py',
 'echo Please convert 6000000040000000008 using QWERTYUIOPlkjhgfdsaZXCVBNMmnbvcxzASDFGHJKL | python3 roman_arabic.py',
 'echo Please convert Ll using lL | python3 roman_arabic.py',
 'echo Please convert ytt using asdfghjklpoiuyt | python3 roman_arabic.py',
 'echo Please convert GTdqQQ using mMnNjJkKtTgGdDqQ | python3 roman_arabic.py',
 'echo Please convert pmbwr using plmnbqwert | python3 roman_arabic.py',
 'echo Please convert retttLASAJJJFHzHxxxncvcPPPWOIOUUUTY using pqowieurytLAKSDJFHGzmxncbvQPWOEIRUTY | python3 roman_arabic.py',
 'echo Please convert fZZBBBKLGAQRTTIOOOczm using qwertyuioplkjhgfdsaZXCVBNMLKJHGFDSAQWERTYUIOPzxcvbnm | python3 roman_arabic.py',
 'echo Please convert TYCXKLLL using QWERTYUIOPlkjhgfdsaZXCVBNMmnbvcxzASDFGHJKL | python3 roman_arabic.py',
 'echo Please convert 937 minimally | python3 roman_arabic.py',
 'echo Please convert I0 minimally | python3 roman_arabic.py',
 'echo Please convert MSSM minimally | python3 roman_arabic.py',
 'echo Please convert ABAB minimally | python3 roman_arabic.py',
 'echo Please convert ABCDEFA minimally | python3 roman_arabic.py',
 'echo Please convert ABAAA minimally | python3 roman_arabic.py',
 'echo Please convert ABBACDEFGH minimally | python3 roman_arabic.py',
 'echo Please convert abcdeabcde minimally | python3 roman_arabic.py',
 'echo Please convert aaaYeXbbbcccdddeee minimally | python3 roman_arabic.py',
 'echo Please convert abcdefghijabcdefghij minimally | python3 roman_arabic.py',
 'echo Please convert X minimally | python3 roman_arabic.py',
 'echo Please convert qp minimally | python3 roman_arabic.py',
 'echo Please convert LPPP minimally | python3 roman_arabic.py',
 'echo Please convert hjgrt minimally | python3 roman_arabic.py',
 'echo Please convert TTTEEQ minimally | python3 roman_arabic.py',
 'echo Please convert ERRTYYY minimally | python3 roman_arabic.py',
 'echo Please convert IIUUUtTRRB minimally | python3 roman_arabic.py',
 'echo Please convert lljjggffsswwccbbnn minimally | python3 roman_arabic.py',
 'echo Please convert eteuuiooolllkjjghfds minimally | python3 roman_arabic.py',
 'echo Please convert lllkkkjjhhmxxvvqqqppp minimally | python3 roman_arabic.py',
 'echo Please convert kdjshffyyyMAAADDGDT minimally | python3 roman_arabic.py',
 'echo Please convert brbwwqaaaZZZXCCKBOPL minimally | python3 roman_arabic.py',
 'echo Please convert CEEGGGIikmMoOOqQQQSR minimally | python3 roman_arabic.py',
 'echo Please convert uvcfdrzzzeeaQQCCCHVYRE minimally | python3 roman_arabic.py',
 'echo Please convert iyoppplkkjhgdazxccvbbbmb minimally | python3 roman_arabic.py',
 'echo Please convert KKKJJJHHZZXCVVRRQQQWWW minimally | python3 roman_arabic.py',
 'echo Please convert tgggvnnLAAAKSSFJHDERRTWWW minimally | python3 roman_arabic.py',
 'echo Please convert YUUIIIOoplLkKKjJJJHJGHfFFFdDDsSaZzXXXCCV minimally | python3 roman_arabic.py',
 'echo Please convert IOOPPPLlkjJhHHgGGGFGDFsSSSaAAzZxCcVVVBBN minimally | python3 roman_arabic.py',
 'echo Please convert fhdssszsxcccbcnmmmNmBVVVXVZAAASDGGHJLLPOUUYTEEWQ minimally | python3 roman_arabic.py']


with open("cpu_your_tests_result_ass1.txt", "w") as file:
    file.write(f"TEST FOR 2024 T1 Ass1 ---- Leo CPU\n\n")
    count = 1
    for command in commands:
        file.write(f"TEST {count} BEGIN\n")
        file.write("$ " + command + "\n")
        process = subprocess.run(command, shell=True, capture_output=True, text=True)
        file.write(process.stdout)
        
        if process.stderr:
            file.write(process.stderr)
            
        file.write("\n")
        file.write(f"TEST {count} END\n\n")
        count += 1