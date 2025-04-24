import random
Dict = {'A': '00000', 'B': '00001', 'C': '00010',
        'D': '00011', 'E': '00100', 'F': '00101',
        'G': '00110', 'H': '00111', 'I': '01000',
        'J': '01001', 'K': '01010', 'L': '01011',
        'M': '01100', 'N': '01101', 'O': '01110',
        'P': '01111', 'Q': '10000', 'R': '10001',
        'S': '10010', 'T': '10011', 'U': '10100',
        'V': '10101', 'W': '10110', 'X': '10111',
        'Y': '11000', 'Z': '11001', '.': '11010',
        '?': '11100', '!': '11011', '(': '11101',
        ')': '11110', '-': '11111'}

#'Eλενχος εισόδου χαρακτήρων
allowed_chars = set('.?,!()-ABCDEFGHIJKLMNOPQRSTUVWXYZ')

Word = input('Εκφραση: ')
while not set(Word).issubset(allowed_chars):
    print('Μη αποδεκτοί χαρακτήρες.')
    Word = input('Εκφραση: ')
print(Word)

#Μετατροπή της έκφρασης σε BINARY
Binary = ''
for i in range(len(Word)):
  if (Word[i] in ['.', ',', '?', '!', '(', ')', '-']) or Word[i] >= 'A' and Word[i] <= 'Z':
    Binary += Dict[Word[i]]
  else:
    print("Mη αποδεκτοί χαρακτήρες")


#Δημιουργεία ψευδότυχαίου αριθμού ίσο με το μέγεθος της έκφρασης, με την βοήθεια της έτοιμης συνάρτησης random
Key = ''
for i in range(len(Binary)):
  random_number = random.randint(0, 1)
  Key += str(random_number)

#Κάνω την πράξη XOR μεταξύ του Binary αριθμού και του κλειδιού, αλλά δεν χρησιμοποιώ την έτοιμη συνάρτηση, γιατί  η μορφή
#των χαρακτήρων ειναι σαν STR και οχι σαν INTEGER
Coded_Binary = ''
for i in range(len(Binary)):
 if Binary[i] == Key[i]:
  Coded_Binary += '0'
 else:
  Coded_Binary += '1'

#Αντιστοίχηση των Binary αριθμών στον χαρακτήρα και εμφάνιση του κωδικοποιημένου μηνύματος
temp  = ''
Coded = ''
j     = 0
for i in range(len(Binary)):
    temp += Coded_Binary[i]
    j    += 1
    if j%5==0:
        for key in Dict.keys():
            if Dict[key] == temp:
                Coded += key
        temp = ''
print(Coded)

#Μετατρέπω σε BINARY το κρυπτογραφημένο κείμενο
Crypto_message_Binary = ''
for i in range(len(Coded)):
    Crypto_message_Binary += Dict[Coded[i]]

#XOR του κλειδιού με το κρυπτογραφημένο μήνυμα, για τον ίδιο λόγο με πριν δεν χρισημοποιώ την έτοιμη συνάρτηση XOR
Decoded_Binary = ''
for i in range(len(Binary)):
 if Crypto_message_Binary[i] == Key[i]:
  Decoded_Binary += '0'
 else:
  Decoded_Binary += '1'

#Αντιστοίχηση των Binary αριθμών στον χαρακτήρα και εμφάνιση του αποκωδικοποιημένου μηνύματος
temp    = ''
Decoded = ''
j       = 0
for i in range(len(Binary)):
    temp += Decoded_Binary[i]
    j    += 1
    if j%5==0:
        for key in Dict.keys():
            if Dict[key] == temp:
                Decoded += key
        temp = ''
print(Decoded)
