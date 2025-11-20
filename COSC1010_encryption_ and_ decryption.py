#
# Victor Byrd
# 11-20-25
# File Encryption Program
# COSC 1010
#
# Use comments liberally throughout the program. 

def main():
    # Dictionary mapping each letter to a code symbol
    codes = {
        'A':'%', 'a':'9',
        'B':'@', 'b':'#',
        'C':'&', 'c':'1',
        'D':'$', 'd':'2',
        'E':'!', 'e':'3',
        'F':'^', 'f':'4',
        'G':'*', 'g':'5',
        'H':'(', 'h':'6',
        'I':')', 'i':'7',
        'J':'[', 'j':'8',
        'K':']', 'k':'0',
        'L':'{', 'l':'=',
        'M':'}', 'm':'+',
        'N':'<', 'n':'-',
        'O':'>', 'o':'?',
        'P':'~', 'p':'/',
        'Q':'`', 'q':'|',
        'R':'$', 'r':'¢',
        'S':'€', 's':'£',
        'T':'§', 't':'¶',
        'U':'•', 'u':'°',
        'V':'✓', 'v':'√',
        'W':'∆', 'w':'÷',
        'X':'×', 'x':'Ω',
        'Y':'≈', 'y':'≠',
        'Z':'¥', 'z':'₩'
    }

    try:
        # open file
        infile = open("text.txt", "r", encoding="utf-8")
        contents = infile.read()
        infile.close()
    except Exception as err:
        print("Error opening text.txt:", err)
        return

    encrypted_text = ""

    # encrypt letter by letter
    for ch in contents:
        if ch in codes:
            encrypted_text += codes[ch]
        else:
            encrypted_text += ch   

    # save to encrypted
    outfile = open("encrypted.txt", "w", encoding="utf-8")
    outfile.write(encrypted_text)
    outfile.close()

    print("Encryption complete. Check encrypted.txt.")

main()

def main():
    # same dictionary 
    codes = {
        'A':'%', 'a':'9',
        'B':'@', 'b':'#',
        'C':'&', 'c':'1',
        'D':'$', 'd':'2',
        'E':'!', 'e':'3',
        'F':'^', 'f':'4',
        'G':'*', 'g':'5',
        'H':'(', 'h':'6',
        'I':')', 'i':'7',
        'J':'[', 'j':'8',
        'K':']', 'k':'0',
        'L':'{', 'l':'=',
        'M':'}', 'm':'+',
        'N':'<', 'n':'-',
        'O':'>', 'o':'?',
        'P':'~', 'p':'/',
        'Q':'`', 'q':'|',
        'R':'$', 'r':'¢',
        'S':'€', 's':'£',
        'T':'§', 't':'¶',
        'U':'•', 'u':'°',
        'V':'✓', 'v':'√',
        'W':'∆', 'w':'÷',
        'X':'×', 'x':'Ω',
        'Y':'≈', 'y':'≠',
        'Z':'¥', 'z':'₩'
    }

    # reverse dictionary for decoding
    decode = {value: key for key, value in codes.items()}

    try:
        infile = open("encrypted.txt", "r", encoding="utf-8")
        contents = infile.read()
        infile.close()
    except Exception as err:
        print("Error opening encrypted.txt:", err)
        return

    decrypted_text = ""

    for ch in contents:
        if ch in decode:
            decrypted_text += decode[ch]
        else:
            decrypted_text += ch   

    print("\n--- Decrypted Text ---\n")
    print(decrypted_text)
    print("\n--- End ---")

main()
