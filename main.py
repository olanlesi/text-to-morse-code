
# creating a dictionary which contain uppercase alphabet, numbers 0-9, symbols as key and their morse code as the value


morse_dict = {
    "A": ".-",  "B": "-...", "C": "-.-.",  "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..",  "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--",
    "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": "....", "6": "-...", "7": "--...", "8": "---..", "9": "----.", "0": "-----", "?": "..--..",
    "!": "-.-.--", ".": ".-.-.-", ",": "--..--", ";": "-.-.-.", ":": "---...", "+": ".-.-.", "-": "-....-",
    "/": "-..-.", "=": "-...-", " ": "|"
    }


def text_2_morse(words=input("what is your message? ")):

    """this function take words as string and return it as morse code """

    global morse_dict

    texts = [letter.upper() for letter in words]
    code = [morse_dict[text] for text in texts]
    return "/".join(code)


message = text_2_morse()
print(message)