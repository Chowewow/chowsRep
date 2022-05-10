import re

def find_programming_engineers(ensc2003_students, cits2401_students):
    '''returns students doing both'''
    return ensc2003_students & cits2401_students

def character_set_counts(string_1, string_2, string_3):
    '''returns the characters not in string_3 but in 1 and 2'''
    return len((set(string_1) & set(string_2)) - set(string_3))

def distinct_character_count(string_1, string_2, string_3, string_4):
    '''returns the characters not in string 3 and 4 but in 1 and 2'''
    new_set = (set(string_1) & set(string_2)) - (set(string_3) | set(string_4))
    new_list = list(new_set)
    new_list.sort()
    return new_list

def fourth_min(myset):
    '''return fourth lowest'''
    return sorted(myset)[3]

def two_minset(myset):
    '''returns two lowest values'''
    new_list = list(sorted(myset)[0:2])
    return new_list

def print_common_words(filename_1, filename_2):
    '''return common words of filename_1 and filename_2 in alphabetical order'''
    first_words = set(word_set_from_file(filename_1))
    second_words = set(word_set_from_file(filename_2))
    common_words = sorted(first_words & second_words)
    for word in common_words:
        print(word)
def word_set_from_file(filename):
    '''returns a list of words from a file'''
    input_file = open(filename)
    source_string = input_file.read().lower()
    input_file.close()
    words = re.findall('[a-zA-Z]+', source_string)
    return words

def get_name(name_dict, id_num):
    '''returns the name associated with the id'''
    if id_num in name_dict:
        return name_dict[id_num]
    return None

def word_counter(input_str):
    '''returns a list of occurrences of words'''
    new_str = input_str.lower().split()
    new_dict = {}
    for word in new_str:
        if word in new_dict:
            new_dict[word] += 1
        else:
            new_dict[word] = 1
    return new_dict

def find_key(input_dict, value):
    '''return the key, given a value'''
    for val in input_dict:
        if input_dict[val] == value:
            return val
    return None

def make_index(words_on_page):
    '''logs the page number of the words in a "book"'''
    our_dict = {}
    for index in words_on_page:
        for word in words_on_page[index]:
            if word not in our_dict:
                our_dict[word] = [index]
            else:
                our_dict[word].append(index)
    return our_dict

def make_dictionary(filename):
    '''returns the number of occurences of each idea'''
    objects = open(filename).read().split('\n')
    our_dict = {}
    for thing in objects:
        thing = thing.strip()
        if thing not in our_dict and len(thing) != 0:
            our_dict[thing] = 1
        elif thing in our_dict:
            our_dict[thing] += 1
    return our_dict

def print_word_counts(filename):
    '''prints an abc ordered list of all words in the doc'''
    input_file = open(filename, 'r')
    source_string = input_file.read().lower()
    input_file.close()
    words = re.findall('[a-zA-Z]+', source_string)
    our_dict = {}
    for word in words:
        our_dict[word] = our_dict.get(word, 0) + 1
    for word in sorted(our_dict):
        print(word + ":", our_dict[word])
        
def print_word_counts2(filename):
    input_file = open(filename,'r')
    source_string = input_file.read().lower()
    input_file.close()
    words = re.findall('[a-zA-Z]+', source_string)
    our_dict = {}
    for word in words:
        our_dict[word] = our_dict.get(word, 0) + 1
    for word in sorted(our_dict, key=our_dict.get, reverse=True):
        print(word + ":", our_dict[word])
        
    

def take_second(elem):
    return elem[0]