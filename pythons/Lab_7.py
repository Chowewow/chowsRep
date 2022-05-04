#how to open online shit
'''
import urllib.request
url = "http://www.bom.gov.au/climate/data"
web_page = urllib.request.urlopen(url)
for line in web_page:
    print(line)
    web_page.close()
'''
'''
def main():
    zodiac_signs = [
    ('Capricorn', 0, 1, 19, 1),
    ('Aquarius', 20, 1, 18, 2),
    ('Pisces', 19, 2, 20, 3),
    ('Aries', 21, 3, 19, 4),
    ('Taurus', 20, 4, 20, 5),
    ('Gemini', 21, 5, 20, 6),
    ('Cancer', 21, 6, 22, 7),
    ('Leo', 23, 7, 22, 8),
    ('Virgo', 23, 8, 22, 9),
    ('Libra', 23, 9, 22, 10),
    ('Scorpio', 23, 10, 21, 11),
    ('Sagittarius', 22, 11, 21, 12),
    ('Capricorn', 22, 12, 31, 12)]

    name = input("What is your name? ")
    dob = input("Enter your birthday in the form DD/MM e.g. 3/11: ")
    day_string, month_string = dob.split('/')
    day = int(day_string)
    month = int(month_string)
    for sign, day0, month0, day1, month1 in zodiac_signs:
        if (month0, day0) <= (month, day) <= (month1, day1):
            print("Hi {}, your Zodiac sign is {}.".format(name, sign))
    main()
'''
"""
# *** YOUR CODE *** [Hint: only docstrings and imports can go at the start. 
# *** Only one of those two is relevant here. Which one?]
'''idk what we would import so...'''

def fun_function(n_items, cost_per_item, discount_percent, discount_threshold):
    '''calculates the cost of the items with the given data'''
    # *** YOUR CODE *** The body of fun_function goes here
    cost = n_items * cost_per_item
    if n_items > discount_threshold:
        cost = cost * (1 - discount_percent / 100)
    return cost

def main():
    # *** YOUR CODE ***The body of the main function
    '''initializes the variables'''
    cost_per_item = 27      # Without discount
    discount_percent = 10
    discount_threshold = 20
    n_items = int(input("How many items? "))
    cost = fun_function(n_items, cost_per_item, discount_percent, discount_threshold)   
    print('{} items costing ${:.2f}'.format(n_items, cost))

# Call the main function to run the program
main()
"""
"""
'''a program -_-'''
def read_bound(string):
    '''Reads the upper bound from the standard input (keyboard).
       If the user enters something that is not a positive integer
       the function issues an error message and retries
       repeatedly'''
    upper_bound = None
    while upper_bound is None:
        line = input(string)
        if line.isnumeric():
            upper_bound = int(line)
            return upper_bound
        print("You must enter a positive number.")
    
    
def is_perfect_square(num):
    '''returns true if perfect square'''
    return (num ** 0.5) % 1 == 0

def print_squares(lower_bound, upper_bound, squares):
    '''Print a given list of all the squares up to a given upper bound'''
    print("The perfect squares from {} to {} are: ".format(lower_bound, upper_bound))
    for square in squares:
        print(square, end=' ')
    print()

def main():
    '''Every home should have one'''
    lower_bound = read_bound("Enter the lower bound: ")
    upper_bound = read_bound("Enter the upper bound: ")
    squares = []
    for num in range(lower_bound, upper_bound + 1):
        if is_perfect_square(num):
            squares.append(num)

    print_squares(lower_bound, upper_bound, squares)
main()
"""

'''
"""Test area module"""
import area

def main():
    """Main program calls each method of the area module"""
    print(area.triangle_area(10.0, 7.0))  # Should print 35.0
    print(area.rectangle_area(9.0, 7.0))  # Should print 63.0

main()
'''

"""
def print_game_score(points, maximum_points=200):
    print("Your points: {:.1f}/{:.1f} ({:.1f}%)".format(points,
    maximum_points,(points/maximum_points)*100))
    
def describe(name='unknown', species='unkown', age='unknown'):
    '''describes a species'''
    print("{} is a {}, age: {}".format(name, species, age))
    
def file_size(filename):
    '''counts the number of characters in a file'''
    count = 0
    index = 0
    data = open(filename)
    for line in data:
        while index < len(line):
            print(index)
            if line[index] == " ":
                index += 1
            else:
                count += 1
                index += 1
    return count
"""

'''
def get_stats(filename):
    data = open(filename)
    line = data.readlines(1)[0].split(',')
    count = 0
    total = 0
    maxi = 0
    mini = 1000
    for num in line:
        total += float(num)
        count += 1
        if float(num) > maxi:
            maxi = float(num)
        if float(num) < mini:
            mini = float(num)
    return (mini, maxi, total/count)
'''

"""
def get_stats2(filename):
    '''returns a tuple with the mini, maxi, and average temp'''
    data = open(filename)
    line = data.readlines(1)[0].split(',')
    index = 0
    while index < len(line):
        line[index] = float(line[index])
        index += 1
    return(min(line), max(line), sum(line)/len(line))
"""


def read_data(filename):
    """Read and return the contents of the given file.
       The file is assumed to exist, or an exception will occur.
       It is also assumed that each line of the file consists of a
       student name, a comma, and a floating-point mark.
       Returns: a list of (name, mark) tuples, where name is a string
       and mark is a floating-point number.
    """
    data = open(filename)
    tuples = []
    for line in data:
        tuples.append((line[0:line.index(',')], float(line[line.index(',') + 1:len(line)])))
    return tuples

def statistics(student_data):
    """Given a list of (name, mark) pairs, returns a tuple
       containing statistics extracted from the list. The tuple elements are
       minimum_mark, maximum_mark, average_mark and top_students. The
       first three are just floating point values. The last one is an
       alphabetically ordered list of the names of all students whose
       marks are equal to the maximum_mark.
    """
    top_students = []
    marks_list = []
    for tup in student_data:
        marks_list.append(tup[1])
    index = 0
    while index < len(marks_list):
        if marks_list[index] >= max(marks_list):
            top_students.append(student_data[index][0])
        index += 1
    top_students.sort()
    return (min(marks_list), max(marks_list), sum(marks_list)/len(marks_list), top_students)

def case_converter(filename):
    new_file = ""
    lines = open(filename)
    for line in lines:
        new_file += line.upper()
    file = open(filename, 'w')
    file.write(new_file)
    return filename

def write_reversed_file(input_filename, output_filename):
    '''reverses the text of a file'''
    sorte = []
    new_write = ""
    lines = open(input_filename).readlines()
    index = len(lines) - 1
    while index > -1:
        sorte.append(lines[index])
        index -= 1
    for line in sorte:
        new_write += line
    outfile = open(output_filename, 'w')
    outfile.write(new_write)
    outfile.close()