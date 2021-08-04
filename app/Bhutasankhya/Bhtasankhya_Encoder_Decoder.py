from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate
import json
from random import sample
from sanskrit_parser import Parser


def get_scheme_map(scheme):
    
    supported_formats = ["HK", "Devanagari", "IAST", "ITRANS", "Kolkata", "SLP1", "Kannada", "Malayalam", "Telugu"]
    
    if scheme not in supported_formats:
        print("The input text is not in supported format.")
        print(f"List of supported formats : {supported_formats}")
        return "", ""
    
    if scheme == "HK":
        script = sanscript.HK
    
    if scheme == "Devanagari":
        script = sanscript.DEVANAGARI
        
    if scheme == "IAST":
        script = sanscript.IAST
        
    if scheme == "ITRANS":
        script = sanscript.ITRANS

    if scheme == "Kolkata":
        script = sanscript.KOLKATA
    
    if scheme == "SLP1":
        script = sanscript.SLP1
        
    if scheme == "Kannada":
        script = sanscript.KANNADA
        
    if scheme == 'Malayalam':
        script = sanscript.MALAYALAM
    
    if scheme == 'Telugu':
        script = sanscript.TELUGU
        
    
    s1 = SchemeMap(SCHEMES[script], SCHEMES[sanscript.SLP1])
    s2 = SchemeMap(SCHEMES[script], SCHEMES[sanscript.DEVANAGARI])
    
    return s1, s2

def get_transliteration(data, scheme_map):

    return transliterate(data, scheme_map=scheme_map)

def slp2dev(src, convert_numbers=True):
    vowels = {
        'a': ['अ', ''],
        'A': ['आ', 'ा'],
        'i': ['इ', 'ि'],
        'I': ['ई', 'ी'],
        'u': ['उ', 'ु'],
        'U': ['ऊ', 'ू'],
        'f': ['ऋ', 'ृ'],
        'F': ['ॠ', 'ॄ'],
        'x': ['ऌ', 'ॢ'],
        'X': ['ॡ', 'ॣ'],
        'e': ['ए', 'े'],
        'E': ['ऐ', 'ै'],
        'o': ['ओ', 'ो'],
        'O': ['औ', 'ौ']}
    consonants = {
        'k': 'क',
        'K': 'ख',
        'g': 'ग',
        'G': 'घ',
        'N': 'ङ',
        'c': 'च',
        'C': 'छ',
        'j': 'ज',
        'J': 'झ',
        'Y': 'ञ',
        'w': 'ट',
        'W': 'ठ',
        'q': 'ड',
        'Q': 'ढ',
        'R': 'ण',
        't': 'त',
        'T': 'थ',
        'd': 'द',
        'D': 'ध',
        'n': 'न',
        'p': 'प',
        'P': 'फ',
        'b': 'ब',
        'B': 'भ',
        'm': 'म',
        'y': 'य',
        'r': 'र',
        'l': 'ल',
        'v': 'व',
        'S': 'श',
        'z': 'ष',
        's': 'स',
        'h': 'ह'}
    others = {
        'M': 'ं',
        'H': 'ः',
        '~': 'ँ',
        "'": 'ऽ'}
    digits = {
        '0': '०',
        '1': '१',
        '2': '२',
        '3': '३',
        '4': '४',
        '5': '५',
        '6': '६',
        '7': '७',
        '8': '८',
        '9': '९'}

    tgt = ''
    boo = False
    inc = 0
    while inc < len(src):
        pre = src[inc-1] if inc > 1 else ''
        now = src[inc]
        nxt = src[inc+1] if inc < len(src) - 1 else ''
        if now in consonants:
            tgt += consonants[now]
            if nxt == 'a':
                inc += 1
            elif nxt in vowels:
                boo = True
            else:
                tgt += '्'
        elif now in vowels:
            if boo:
                tgt += vowels[now][1]
                boo = False
            else:
                tgt += vowels[now][0]
        elif now == '\'':
            if not pre or not nxt:
                tgt += now
            elif ord(pre) in range(65, 123) and ord(nxt) in range(65, 123):
                tgt += 'ऽ'
            else:
                tgt += now
        elif now in others:
            tgt += others[now]
        elif now in digits:
            if convert_numbers:
                tgt += digits[now]
            else:
                tgt += now
        elif now == '.':
            if nxt == '.':
                tgt += '॥'
                inc += 1
            else:
                tgt += '।'
        else:
            tgt += now
        inc += 1
    return tgt

def bhutasankhya (nume,database):
    try:    
        option = database[nume]
        option= sample(option,k=2)
        i = 1
        choices = []
        for sentem in option:
          sentem = slp2dev(sentem)

          #print(f"\t{i}. {sentem}")
          choices.append(sentem)
          i +=1
        
        return choices, True
        
    except:
        
        return [], False

def bhutasankhya_decoder(word,database, scheme):
    #scheme = detect.detect(word)
    scheme_map = get_scheme_map(scheme)
        
    if scheme_map[0] != "":
        word = get_transliteration(word, scheme_map[0])
    
    
    for i in database:
        if word in database[i]:
            #print("The Bhutasankhya of the word is: ",i)
            return i, [word], True
    parser = Parser()
        
    splits = list(parser.split(word, limit=10))
    llist = []
    breakup = []
    for split in splits:
        llist.append(split.split)
    for i in range(len(llist)):
        string=""
        count =0
        for j in range(len(llist[i])):
            
            for key,value in database.items():
                if str(llist[i][j]) in value:
                    
                    string += str(key)
                    breakup.append((llist[i][j], value, str(key)))
                    count+=1
                    continue
        if count==len(llist[i]):
            #print("The Bhutasankhya of the word is: "+ string)
            return string, breakup, True
    #print("Sorry, the word has no Bhutasankhya according to our database")
    return string, breakup, False

def encoder(num, jsonfile):
    #nume = input("Please Input a number: ")
    database = dict()

    # Reading from json file
    json_object = json.load(jsonfile)

    for number in json_object:

        database[number] = json_object[number]

    return bhutasankhya(num, database)

def decoder(word, jsonfile, scheme):
    #word = input("Input a word: ")
    database = dict()

    # Reading from json file
    json_object = json.load(jsonfile)
    
    for number in json_object:

        database[number] = json_object[number]

    return bhutasankhya_decoder(word,database, scheme)