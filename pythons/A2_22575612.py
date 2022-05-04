def proper_capitalization(sentence):
    '''returns sentence in lower case'''
    return sentence.lower()

def tokenization(sentence):
    '''returns strings in sentence as a list'''
    return sentence.split()

def stop_word_removal(sentence, stop_words):
    '''return a sentence without the stop words'''
    word_list = tokenization(sentence)
    stops = tokenization(stop_words)
    new_str = ""
    index = 0
    while index < len(word_list):
        for stop in stops:
            if word_list[index] == stop:
                word_list.remove(word_list[index])
        index += 1
    for word in word_list:
        new_str += word + " "
    return new_str

def remove_punc(sentence, punctuation):
    '''returns the sentence without the punctuation'''
    word_list = tokenization(sentence)
    new_str = ""
    count = 0
    while count < len(word_list):
        word_list[count] = word_list[count].strip(punctuation)
        count += 1
    for word in word_list:
        new_str += word + " "
    return new_str

def remove_duplicate_words(sentence):
    '''returns sentence without duplicate words'''
    word_list = tokenization(sentence)
    new_str = ""
    for word in word_list:
        index = word_list.index(word) + 1
        length = len(word_list)
        while index < length:
            if word_list[index] == word:
                word_list.pop(index)
                length -= 1
            else: 
                index += 1
        
    word_list.sort()
    for word in word_list:
        new_str += word + " "
    return  new_str

def sentence_segmentation(document):
    '''returns a list of sentences'''
    new_list = []
    new_word = ""
    index = 0
    while index < len(document):
        if index + 1 == len(document):
            new_word += document[index]
            new_list.append(new_word.strip())
            break
        if not (document[index] == '.' and document[index + 1] == " "):
            new_word += document[index]
        else:
            new_word += document[index]
            new_list.append(new_word.strip())
            new_word = ""  
        index += 1
    return new_list
                
    
def vowel_consonant_ratio(sentence):
    '''returns the ratio of vowels to consonants in a sentence'''
    new_sentence = proper_capitalization(sentence)
    vowels = 0
    consonants = 0
    for char in new_sentence:
        if char.isalpha() and char in ("aeiou"):
            vowels += 1
        elif char.isalpha() and char not in ("aeiou"):
            consonants += 1
    if consonants == 0 or vowels == 0:
        return 0.0
    ratio = vowels/consonants

    print("Number of vowels: {} \nNumber of consonants: {}".format(vowels, consonants))
    return round(ratio, 4)

def valid_words_mask(sentence):
    '''returns the number of valid words'''
    words = tokenization(sentence)
    count = 0
    bool_list = []
    for word in words:
        dashcount = 0
        next_bool = True
         
        if not word[-1].isascii() or word[-1].isdigit():
            bool_list.append(False)
            continue
        
        if word[-1] == '-' or word[0] == '-':
            bool_list.append(False)
            continue
        
        for lett in word[0:-1]:
            if not lett.isalpha():
                if lett == '-' and dashcount == 0:
                    dashcount += 1
                    continue
                next_bool = False
                break      
            
        if next_bool is False:
            bool_list.append(next_bool)
            continue        
        count += 1
        bool_list.append(next_bool)
    return (count, bool_list)

def cleaning_noise(sentence):
    '''removes all noise from sentence'''
    word_list = tokenization(sentence)
    index = 0
    atcount = 0
    new_str = ""
    while index < len(word_list):
        
        if word_list[index].find('http') != -1:
            word_list[index] = ''
            
        if word_list[index].find('\n') != -1:
            word_list[index] = word_list[index].replace('\n', '', word_list[index].count('\n'))
            
        if word_list[index].find('#') != -1:
            word_list[index] = ''
            
        if word_list[index].find('&amp') != -1:
            word_list[index] = word_list[index].replace('&amp', '&', word_list[index].count('&amp'))
        
        if word_list[index].find('@') != -1:
            if atcount % 2 == 0:
                atcount += 1
                word_list[index] = ''
            else:
                atcount += 1
                
        index += 1
    for word in word_list:
        if word != "":
            new_str += word + " "
    return new_str.strip()

def construct_ngrams(sentence, n):
    '''returns an n-gram generated from sentence'''
    index = 0
    new_list = tokenization(sentence)
    length = len(new_list) - n
    outerlist = []
    
    
    while index <= length:
        index2 = 0
        element = []
        while index2 < n:
            element.append(new_list[index + index2])
            index2 += 1
        outerlist.append(element)
        index += 1
    return outerlist

    
def load_data(filename):
    '''returns the lines of filename stripped and encoded with UTF-8'''
    text = open(filename, mode='r', encoding='utf-8')
    lines = []
    for line in text:
        lines.append(line.strip())
    return lines

def tweet_analysis():
    '''processes file and returns lines'''
    filename = input("Enter the name of the file to read: ")
    filew = input("Enter the name of the file to write: ")
    stop_words = input("Enter your stopwords: ")
    puncs = input("Enter your punctuations to remove: ")
    text = open(filename)
    lines = []
    for line in text:
        new_line = line
        new_line = proper_capitalization(new_line)
        new_line = stop_word_removal(new_line, stop_words)
        new_line = remove_punc(new_line, puncs)
        new_line = remove_duplicate_words(new_line)
        new_line = cleaning_noise(new_line)
        new_line = pos(new_line)
        file = open(filew, mode='w', encoding='utf-8')
        file.write(new_line)
        file.close()
        lines.append(new_line)
    return lines

def pos(sentence):
    '''stems every word in sentence and returns sentence'''
    new_sentence = tokenization(sentence)
    index = -1
    new_str = ""
    for word in new_sentence:
        index += 1
        if word.endswith("'s") or word.endswith("s'"):
            word = word[0:-2]
        if word.endswith('sses'):
            word = word.removesuffix('es')
        if word.endswith('ies'):
            if len(word.removesuffix('es')) < 3:
                word = word.removesuffix('s')   
            else:
                word = word.removesuffix('es')                
        if word.endswith('ves'):
            if len(word.removesuffix('ves')) < 3:
                word = word.removesuffix('ves') + "fe"
            else:
                word = word.removesuffix('ves') + "f"        
        
        if word.endswith('s') and word[-2] not in "aeiousy":
            for lett in word:
                if lett in "aeiou":
                    word = word.removesuffix('s')
                    break
                

        if word.endswith('ly') or (word.endswith('lying') and 
            len(word.removesuffix('lying')) > 0):
            word = word.removesuffix('lying')
            word = word.removesuffix('ly')    
        if word.endswith('ed'):
            if word.endswith('ied') and len(word.removesuffix('ed')) < 3:
                word = word.removesuffix('d')
            word = word.removesuffix('ed')            
        if word.endswith('er'):
            word = word.removesuffix('er')
        if word.endswith('ing') and len(word.removesuffix('ing')) > 2:
            word = word.removesuffix('ing')        
        new_sentence[index] = word
        
    for word in new_sentence:
        new_str += word + " "
    return new_str

def word_ranking(corpus, n, sort_index):
    '''returns a list of sorted tuples'''
    words = ""
    tuple_list = []
    for sentence in corpus:
        words += sentence + " "
    tokenized = tokenization(words)
    while len(tokenized) > 0:
        tuple_list.append((tokenized[0], tokenized.count(tokenized[0])))
        words = words.replace(tokenized[0], "").strip()
        tokenized = tokenization(words)  
    if sort_index == 0:
        tuple_list.sort()
    elif sort_index == 1:
        tuple_list.sort(key=take_second, reverse=True)
    else:
        return []
    return tuple_list[0:n]

def take_second(elem):
    '''returns second element'''
    return elem[1]  