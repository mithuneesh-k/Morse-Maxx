
morse_to_text = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
    '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',

    '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8',
    '----.': '9','|':' '
}

text_to_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',' ':'  '
}

def mor2txt(aroma):
    morse = aroma
    morse=morse.rstrip(" ")
    morse=morse.lstrip(" ")
    morse=morse.replace(" "," | ")
    morse=morse.replace("  "," ")
    morse=morse.replace("\n","")

    lmorse=[]
    for i in morse:
        if i == " ":
            stx = morse[0:morse.index(i)]
            lmorse.append(stx)
            morse = morse[morse.index(i)+1:]
        else:
            continue
    lmorse.append(morse)

    txt=""
    for aa in range(len(lmorse)):
        listmorse=lmorse[aa]
        txt=txt+str(morse_to_text[listmorse])
        
    text=txt.replace("  ","|")
    text=text.replace(" ","")
    text=text.replace("|"," ")
    text=text.capitalize()

    return text

def txt2mor(aavin):
    text=aavin
    orgtext=text
    text=text.upper()
    text=text.replace("\n","")
    ltext=list(text)
    morse=""

    for aa in range(len(ltext)):
        textletter = ltext[aa]
        morse+=text_to_morse[textletter]
        morse+=" "

    return morse