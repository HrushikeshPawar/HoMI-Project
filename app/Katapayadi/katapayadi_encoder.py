from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate
from random import sample, choice
from itertools import combinations

def Encoder(Number):

  options = get_options(Number)

  Normal = []
  Reversed = []

  for option in options:

    if option[2] == 0:
      Normal.append(option[1])
    else:
      Reversed.append(option[1])
  
  return   Normal, Reversed

def Split_Number(Number,Number_of_sentences):
  scheme_map = SchemeMap(SCHEMES[sanscript.SLP1], SCHEMES[sanscript.DEVANAGARI]) 
  l=len(Number)
  Split_pos=[]   ## for storing the places where the number can be split
  Sentence_collection=[]
  i=0
  while i<len(Number)-1:   ## creates a list of the number of places where the input number can be split for eg if i=2 then the number can be split in 2 places
    Split_pos.append(i)
    i=i+1     
  b=[]   ## for storing the split pieces of number 
  n=1 ## the initial number of places at which the number is split
  while len(Sentence_collection)<Number_of_sentences and n<len(Number):   ##  If the number has l digits it can be split in l-1 places
    comb=combinations(Split_pos,n)
    for j in list(comb):
      b.append(Number[0:j[0]+1])
      k=0
      while k<n-1:
        b.append(Number[j[k]+1:j[k+1]+1])
        k=k+1
      b.append(Number[j[n-1]+1:l]) 
      minimum=4    
      c=[]
      Total_number_of_sentences=1
      for part in b:
        Normal,Reversed=Encoder(part)
        Total_number_of_sentences=Total_number_of_sentences*len(Normal)
        c.append(Normal)        
      if Total_number_of_sentences>0:
        i=0
        ls=len(Sentence_collection)
        while (len(Sentence_collection)-ls)<=(Number_of_sentences/(len(Number)-1)) and ((len(Sentence_collection)-ls)<Total_number_of_sentences):
          sentence=[]
          for x in c:
            select=choice(x)
            sentence.append(transliterate(select, scheme_map=scheme_map))
          if sentence not in Sentence_collection:
            Sentence_collection.append((sentence, "-".join(b)))
      b=[]
    n=n+1
  return Sentence_collection   

def get_options(Number):
    cursor.execute("select Katapayadi, Word, Is_Reverse from Encodings where Katapayadi = ?", (Number,))
    return cursor.fetchall()

def print_Normal(Number,Number_of_words,Number_of_sentences):
  
  Words = []
  scheme_map = SchemeMap(SCHEMES[sanscript.SLP1], SCHEMES[sanscript.DEVANAGARI])
  Normal,Reversed=Encoder(Number)
  if Number_of_words <= len(Normal):
    Normal = sample(Normal, k=Number_of_words)
    
    i=0
    while i<len(Normal):  
      Words.append(transliterate(Normal[i], scheme_map=scheme_map))
      i=i+1
  else: 
    
    i=0
    while i<len(Normal):
      
      Words.append(transliterate(Normal[i], scheme_map=scheme_map))
      i=i+1
  if Number_of_sentences>0:
    if len(Number)>1:   
      Sentences = []
      Sentence_collection=Split_Number(Number,Number_of_sentences)
      
      New_Sentence_collection=[]
      for Sentence in Sentence_collection:
        Split = Sentence[1]
        Sentence = Sentence[0][::-1]
        New_Sentence_collection.append((Sentence, Split)) 
      if len(New_Sentence_collection)>=Number_of_sentences:
        
        i=0
        for Sentence in sample(New_Sentence_collection,k=Number_of_sentences): 
          Print_Sentence=""
          for Word in Sentence[0]:
            Print_Sentence=Print_Sentence+" "+ Word  
          
          Sentences.append((Print_Sentence.strip(), Sentence[1]))
          i=i+1
      else:
        
        i=0
        for Sentence in New_Sentence_collection: 
          Print_Sentence=""
          for Word in Sentence[0]:
            Print_Sentence=Print_Sentence+" "+ Word  
          
          Sentences.append((Print_Sentence.strip(), Sentence[1]))
          i=i+1
      return (Words, Sentences)
    else:
      return (Words, [])

def print_Reversed(Number,Number_of_words,Number_of_sentences):
  Number=Number[::-1]
  scheme_map = SchemeMap(SCHEMES[sanscript.SLP1], SCHEMES[sanscript.DEVANAGARI])
  Words = []
  Normal,Reversed=Encoder(Number)
  if Number_of_words <= len(Normal):
    Normal = sample(Normal, k=Number_of_words)
    
    i=0
    while i<len(Normal):
      
      Words.append(transliterate(Normal[i], scheme_map=scheme_map))
      i=i+1
  else: 
    
    i=0
    while i<len(Normal):
      
      Words.append(transliterate(Normal[i], scheme_map=scheme_map))
      i=i+1
  if Number_of_sentences>0:
    Sentences = []
    if len(Number)>1:
      Sentence_collection=Split_Number(Number,Number_of_sentences)
      
      New_Sentence_collection=[]
      for Sentence in Sentence_collection:
        Split = Sentence[1]
        Sentence = Sentence[0][::-1]
        New_Sentence_collection.append((Sentence, Split)) 
      if len(New_Sentence_collection)>=Number_of_sentences:
        
        i=0
        for Sentence in sample(New_Sentence_collection,k=Number_of_sentences): 
          Print_Sentence=""
          for Word in Sentence[0]:
            Print_Sentence=Print_Sentence+" "+ Word  
          
          Sentences.append((Print_Sentence.strip(), Sentence[1][::-1]))
          i=i+1
      else:
        
        i=0
        for Sentence in New_Sentence_collection: 
          Print_Sentence=""
          for Word in Sentence[0]:
            Print_Sentence=Print_Sentence+" "+ Word  
          
          Sentences.append((Print_Sentence.strip(), Sentence[1][::-1]))
          i=i+1
      
      return (Words, Sentences)
    else:
      #print("\n No sentences were generated") 
      return (Words, [])

def Create_Table_Sentences(Text, Part):
    
    table = "\n"
    
    # Create the table's column headers
    table += "|No.|Word Cluster|Partition|\n|-----|-----|-----|\n"
    
    # Create the table's row data
    for i in range(len(Text)):
        table += f"|{i+1}|{Text[i]}|{Part[i]}|\n"
    
    return table

def Create_Table_Words(Text):
    
    table = "\n"
    
    # Create the table's column headers
    table += "|No.|Words|\n|-----|-----|\n"
    
    # Create the table's row data
    for i in range(len(Text)):
        table += f"|{i+1}.|{Text[i]}|\n"
    
    return table

def printAll(Number, options, N_Words, R_Words, N_Sentences, R_Sentences):
    
    result = ""
    
    if len(N_Words) == 0:
        result += f"<p>The database does not yet have any standard encoding for {Number}</p>"
        N_Words_lable = f'The database does not yet have any standard encoding for {Number}'
    elif len(N_Words) < options:
        result += f"<p>The database only has {len(N_Words)} standard encodings for {Number}</p>"
        result += Create_Table_Words(N_Words)
        N_Words_lable = f'The database only has {len(N_Words)} standard encodings for {Number}'
    else:
        result += f"""<p>The database has more than {len(N_Words)} standard encodings for {Number}</p>.
        <p>Displaying randomly selected {options} standard encodings.</p>"""
        result += Create_Table_Words(N_Words)
        N_Words_lable = f'''The database has more than {len(N_Words)} standard encodings for {Number}.
        Displaying randomly selected {options} standard encodings.'''
    
    if len(N_Sentences) != 0:
        result += f"<p>The database is able to generate the following word clusters for standard encoding of {Number}</p>"
        Text = []
        Part = []
        N_Sentences_Dict = dict()
        for row in N_Sentences:
            T, P = row
            Text.append(T)
            Part.append(P)
            N_Sentences_Dict[T] = P
        result += Create_Table_Sentences(Text, Part)

    if len(R_Words) == 0:
        result += f"<p>The database does not yet have any reverse encoding for {Number}</p>"
        R_Words_lable = f'The database does not yet have any reverse encoding for {Number}'
    elif len(R_Words) < options:
        result += f"<p>The database only has {len(R_Words)} reverse encodings for {Number}</p>"
        result += Create_Table_Words(R_Words)
        R_Words_lable = f'The database only has {len(R_Words)} reverse encodings for {Number}'
    else:
        result += f"""<p>The database has more than {len(R_Words)} reverse encodings for {Number}</p>.
        <p>Displaying randomly selected {options} reverse encodings.</p>"""
        result += Create_Table_Words(R_Words)
        R_Words_lable = f'''The database has more than {len(R_Words)} reverse encodings for {Number}.
        Displaying randomly selected {options} reverse encodings.'''
    
    if len(R_Sentences) != 0:
        result += f"<p>The database is able to generate the following word clusters for reverse encoding of {Number}</p>"
        Text = []
        Part = []
        R_Sentences_Dict = dict()
        for row in R_Sentences:
            T, P = row
            Text.append(T)
            Part.append(P)
            R_Sentences_Dict[T] = P
        result +=  Create_Table_Sentences(Text, Part)

    return (N_Words_lable, N_Words, R_Words_lable, R_Words, N_Sentences_Dict, R_Sentences_Dict) #result

def Single_Digit_Encoder(Number, Options):
    Words = []
    scheme_map = SchemeMap(SCHEMES[sanscript.SLP1], SCHEMES[sanscript.DEVANAGARI])

    for i in range(7):
      n = '0'*i + str(Number)
      options = get_options(n)

      for option in options:
        Words.append(transliterate(option[1], scheme_map=scheme_map))
      
    if len(Words) > Options:
      label = (f'''The Database has a total of {len(Words)} word encodings for {Number}.''', 
      f'''Showing {Options} random selected words.''')
      Words = sample(Words, k=Options)
    else:
      label = (f'''<p>The Database has only {len(Words)} word encodings for {Number}.''', 
      f'''Showing all available words.</p>''')
    
    return label, Words

def Katapayadi_Encoder(Number, options, Database):
    if options == "":
        options = 5
        
    global cursor
    cursor = Database.cursor()
    options = int(options)
    Number_of_words = options
    Number_of_sentences = options

    if len(str(int(Number))) == 1:
      return Single_Digit_Encoder(Number, options)

    N_Words, N_Sentences = print_Normal(Number,Number_of_words,Number_of_sentences)
    R_Words, R_Sentences = print_Reversed(Number,Number_of_words,Number_of_sentences)
    
    return printAll(Number, options, N_Words, R_Words, N_Sentences, R_Sentences)