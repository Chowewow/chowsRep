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
    punc_list = []
    for punc in punctuation:
        punc_list.append(punc)
    new_str = ""

    for word in word_list:
        temp_word = word
        for punc in punc_list:
            while temp_word.startswith(punc):
                temp_word = temp_word.removeprefix(punc)                        
                for punc2 in punc_list:
                    while temp_word.startswith(punc2):
                        temp_word = temp_word.removeprefix(punc2)
                        
            while temp_word.endswith(punc):
                temp_word = temp_word.removesuffix(punc)
                for punc2 in punc_list:
                    while temp_word.endswith(punc2):
                        temp_word = temp_word.removesuffix(punc2)
                
        word_list[word_list.index(word)] = temp_word
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
    index = 0
    count = 0
    doc_list = tokenization(document)
    new_list = []
    print(doc_list)
    for word in doc_list:
        if not word.endswith('.'):
            count += 1
            if count == len(doc_list) - 1:
                for word2 in doc_list[index:count]:
                    print(doc_list[index:count])
                    temp += word2 + " "
                index = count
                new_list.append(temp)                    
        else:
            temp = ""
            for word2 in doc_list[index:count]:
                print(doc_list[index:count])
                temp += word2 + " "
            index = count
            new_list.append(temp)
    return new_list