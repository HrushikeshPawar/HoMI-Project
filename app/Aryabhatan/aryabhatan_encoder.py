from indic_transliteration import detect, sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate
from random import choice,sample
from itertools import combinations

def Split_Number(number):  
    vowels={'a':1,'A':1,'i':10**2,'I':10**2,'u':10**4,'U':10**4,'f':10**6,'F':10**6,'x':10**8,'X':10**8,'e':10**10,'E':10**12,'o':10**14,'O':10**16}
    consonants={'k':1,'K':2,'g':3,'G':4,'N':5,'c':6,'C':7,'j':8,'J':9,'Y':10,'w':11,'W':12,'q':13,'Q':14,'R':15,'t':16,'T':17,'d':18,'D':19,'n':20,'p':21,'P':22,'b':23,'B':24,'m':25,'y':30,'r':40,'l':50,'v':60,'S':70,'z':80,'s':90,'h':100}
    consonants_keys = list(consonants.keys())
    consonants_values = list(consonants.values())
    digits=[]
    if number<=100:
      digits.append(number)
    else:
      while number>100:
        d=number%100
        digits.append(int(d))
        number=(number-d)/100
        if number <=100:
          digits.append(int(number))
    #print(digits)

    split_digits=[]
    for digit in digits:
      a=[]
      i=1
      while i<digit:
        a.append(i)
        i=i+1
      b=[]
      if digit==0:
        b.append([0])
      if digit in consonants.values():
        b.append([digit])
      if digit>2:  
        comb=combinations(a,2)
        for x in list(comb):
          c=[]
          i=0
          while i<2:
            if i==0:
              if  x[i] in consonants.values():
                c.append(x[i])
            else:
              if (x[i]-x[i-1]) in consonants.values():   
                c.append(x[i]-x[i-1])
              if (digit-x[i]) in consonants.values():  
                c.append(digit-x[i])
            i=i+1 
          if len(c)==3:
            b.append(c)
      if digit>1:  
        comb=combinations(a,1)
        for x in list(comb):
          c=[]
          if x[0] in consonants.values() and digit-x[0] in consonants.values():
            c.append(x[0])
            c.append(digit-x[0])
            b.append(c)
      split_digits.append(b)
    return split_digits

def Aryabhatan_Encoder(number,show):
    vowels={'a':1,'A':1,'i':10**2,'I':10**2,'u':10**4,'U':10**4,'f':10**6,'F':10**6,'x':10**8,'X':10**8,'e':10**10,'E':10**12,'o':10**14,'O':10**16}
    consonants={'k':1,'K':2,'g':3,'G':4,'N':5,'c':6,'C':7,'j':8,'J':9,'Y':10,'w':11,'W':12,'q':13,'Q':14,'R':15,'t':16,'T':17,'d':18,'D':19,'n':20,'p':21,'P':22,'b':23,'B':24,'m':25,'y':30,'r':40,'l':50,'v':60,'S':70,'z':80,'s':90,'h':100}
    consonants_keys = list(consonants.keys())
    consonants_values = list(consonants.values())
    split_digits=Split_Number(number)
    syllable_collection=[]    
    for b in split_digits:
      syllables=[]
      for c in b:
        if c==[0]:
          syllables.append("")   
        else:  
          syllable=""
          for x in c:
            syllable=syllable+consonants_keys[consonants_values.index(x)]   
          syllables.append(syllable)          
      syllable_collection.append(syllables)

    total_words_possible=1
    for syllables in syllable_collection:
      total_words_possible=total_words_possible*len(syllables)

    #print(total_words_possible)
    word_collection=[]
    while len(word_collection)<show and len(word_collection)<total_words_possible:
      word=""
      i=0
      for x in syllable_collection: 
        if x==[""]:
          i=i+2
        else:  
          syllable=choice(x)
          a=[]
          for x,y in vowels.items():
            #print(10**i)
            if y==10**i:
              a.append(x)
          #print(a)
          word=word+syllable+choice(a)
          i=i+2
      if word not in word_collection:
        word_collection.append(word)
    return ( word_collection ,total_words_possible )

def encoder(number, show):
    show=int(show)

    word_collection, total_words_possible=Aryabhatan_Encoder(number,show)
    text = ''
    result = []
    s1 = SchemeMap(SCHEMES[sanscript.SLP1], SCHEMES[sanscript.DEVANAGARI])
    if len(word_collection)==show:
      i=1
      for word in word_collection:
        #print(f"{i}. {transliterate(word,scheme_map=s1)}")
        result.append(transliterate(word,scheme_map=s1))
        i=i+1
    else:
      text = f"\nOnly {total_words_possible} words are available."
      i=1
      for word in word_collection:  
        #print(f"{i}. {transliterate(word,scheme_map=s1)}")
        result.append(transliterate(word,scheme_map=s1))
        i=i+1
    
    return text, result