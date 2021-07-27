from indic_transliteration import detect, sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate
import indicsyllabifier

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
        script = sanscript.KOLKATA_v2
    
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

# A function for actual transliteration
def get_transliteration(data, scheme_map):

    return transliterate(data, scheme_map=scheme_map)

# A function for breaking down a word into syllables
def get_syllable(word):

    syllablizer_handle = indicsyllabifier.getInstance()   # Get the Syllabifier class
    syllables = syllablizer_handle.syllabify_hi(word)     # Initiate the Syllabifier for Hindi 
  
    return syllables

def Aryabhatan(syllables):
    vowels={'a':1,'A':1,'i':10**2,'I':10**2,'u':10**4,'U':10**4,'f':10**6,'F':10**6,'x':10**8,'X':10**8,'e':10**10,'E':10**12,'o':10**14,'O':10**16}
    consonants={'k':1,'K':2,'g':3,'G':4,'N':5,'c':6,'C':7,'j':8,'J':9,'Y':10,'w':11,'W':12,'q':13,'Q':14,'R':15,'t':16,'T':17,'d':18,'D':19,'n':20,'p':21,'P':22,'b':23,'B':24,'m':25,'y':30,'r':40,'l':50,'v':60,'S':70,'z':80,'s':90,'h':100}
    Number=0
    i=0
    value=0
    while i<len(syllables):
      if i==0:
        if syllables[i] in vowels.keys():
          value = value + vowels[syllables[i]]
          Number=Number+value
          value=0
        if syllables[i] in consonants.keys():
          value = value + consonants[syllables[i]]
      else:
        if syllables[i] in vowels.keys():
          if syllables[i-1] in vowels.keys():
            value = value + vowels[syllables[i]]
            Number=Number+value
            value=0
          else:
            value = value * vowels[syllables[i]] 
            Number=Number+value
            value=0
        if syllables[i] in consonants.keys():
          value = value + consonants[syllables[i]]
      i=i+1         
    return Number

def decoder(data, scheme, verbose=True):
   
    scheme_map = get_scheme_map(scheme)
    
    data_slp1 = get_transliteration(data, scheme_map[0])
    data_dev = get_transliteration(data, scheme_map[1])

    Data = dict()
    if verbose:
      Data['Converted in SLP1 : '] = data_slp1
      Data['Converted in Devnagri : '] = data_dev
    
    syllables = []
    
    scheme_map = SchemeMap(SCHEMES[sanscript.DEVANAGARI], SCHEMES[sanscript.SLP1])
    syllables=[]
    for word in data_dev.split():
      word=transliterate(word, scheme_map=scheme_map)
      syllables += get_syllable(word)
    
    aryabhatan = Aryabhatan(syllables)

    Syllables_Data = [[],[]]
    if verbose:
      """
      scheme_map2 = SchemeMap(SCHEMES[sanscript.SLP1], SCHEMES[sanscript.DEVANAGARI])
      for i in range(len(syllables)):
        syllable = syllables[i]#get_transliteration(syllables[i], scheme_map2)
        a =  Aryabhatan([syllable])#transliterate(syllable, scheme_map=scheme_map)])
        if a != '':
          Syllables_Data[0].append(syllable)
          Syllables_Data[1].append(a)
      """

    return (aryabhatan, Data)


"""#Run
##Examples :
  1. bhadrāmbudhisiddhajanmagaṇitaśraddhā sma yad bhūpagīḥ 
  2. āyurārogyasaukhyam
  3. gopIBAgyamaDuvrAta-SfNgiSodaDisanDiga..  KalajIvitaKAtAva galahAlArasaMDara.. (Reverse)
  4. jYAnam paramam Dyeyam
  5. गौण्य वन्ध्यां क्षौम स्फुं
  6. शिवालय त्वां सान्त्वना
"""
