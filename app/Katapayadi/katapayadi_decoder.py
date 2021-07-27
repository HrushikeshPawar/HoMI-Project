from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate
import indicsyllabifier

"""#Supporting Functions"""
# A Function to get a scheme_map used in conversion of a script of any of the mentioned languages or schemes into SLP1 and Devanagari
def get_scheme_map(scheme):
     
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
        
    print(script)
    s1 = SchemeMap(SCHEMES[script], SCHEMES[sanscript.SLP1])
    s2 = SchemeMap(SCHEMES[script], SCHEMES[sanscript.DEVANAGARI])
    
    return s1, s2

# A function for breaking down a word into syllables
def get_syllable(word):

    syllablizer_handle = indicsyllabifier.getInstance()   # Get the Syllabifier class
    return syllablizer_handle.syllabify_hi(word)

# Main code for decoding
def katapayadi(data, reverse=False):
    Vowels = ['a', 'A', 'i', 'I', 'u', 'U', 'e', 'E', 'o', 'O', 'f', 'F', 'x', 'X']
    End_Syllable = ['M', 'H']

    # List of "first letters" of the SLP1 enoding of all the consonants
    Consonants = ['k', 'K', 'g', 'G', 'N', 'c', 'C', 'j', 'J', 'Y', 'w', 'W', 'q', 'Q', 'R', 't', 'T', 'd', 'D', 'n', 'p', 'P', 'b', 'B', 'm', 'y', 'r', 'l', 'v', 'S', 'z', 's', 'h', 'L']
    
    # Each numeric value is matched to the consonant above (We can replace these both list by a dictionary)
    NumereicalValue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    number = ""
    for syllable in data:

        # This is used to ignore some exceptions that arises in Malayalam 
        if syllable[0] not in Consonants + Vowels:
            continue

        if len(syllable) == 1 and syllable not in Vowels:
            continue
        
        elif syllable in Vowels:
            new_digit = "0"
        
        elif len(syllable) == 2 and  syllable[-1] in End_Syllable:  # IM  or AH
            new_digit = "0"

        elif len(syllable) == 3 and syllable[1] in Vowels:
            new_digit = str(NumereicalValue[Consonants.index(syllable[0])]) #"kAe" ka u deva

        elif len(syllable) > 2 and syllable[-1] in Vowels:
          new_digit = str(NumereicalValue[Consonants.index(syllable[-2])])

        elif len(syllable) > 2 and syllable[-1] in End_Syllable and syllable[-3] in Vowels:  #reMM
          new_digit = str(NumereicalValue[Consonants.index(syllable[-4])])

        elif len(syllable) > 2 and syllable[-1] in End_Syllable:
          new_digit = str(NumereicalValue[Consonants.index(syllable[-3])])
        
        else:
            new_digit = str(NumereicalValue[Consonants.index(syllable[0])])
        
        if reverse == False:
            number = new_digit + number      
        else:
            number += new_digit
    
    return number


def decoder(data, scheme, verbose=False):
    
    scheme_map = get_scheme_map(scheme)

    data_slp1 = transliterate(data, scheme_map=scheme_map[0])
    data_dev = transliterate(data, scheme_map=scheme_map[1])

    Data = dict()
    if verbose:
        Data['Converted in SLP1 : '] = data_slp1
        Data['Converted in Devnagri : '] = data_dev
        
    syllables = []
    for word in data_dev.split():
        syllables += get_syllable(word)
    

    scheme_map = SchemeMap(SCHEMES[sanscript.DEVANAGARI], SCHEMES[sanscript.SLP1])
    
    data = []
    for syllable in syllables:
        data.append(transliterate(syllable, scheme_map=scheme_map))

    katapayadi_normal = katapayadi(data, False)
    katapayadi_reverse = katapayadi(data, True)

    Syllables_Data = dict()
    if verbose:
            for i in range(len(syllables)):
                syllable = syllables[i]
                katapa =  katapayadi([transliterate(syllable, scheme_map=scheme_map)])
                if katapa != '':
                    Syllables_Data[syllable] = katapa

    return ((katapayadi_normal, katapayadi_reverse), (Data, Syllables_Data))
