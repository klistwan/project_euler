"""By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file."""

f = open('words.txt', 'r')
words = map(lambda k: k[1:-1], f.readlines()[0].split(','))

def words_to_dict(words):
  dict = {}
  for word in words:
    if len(word) < 4 or not is_unique_word(word):
      continue
    sorted_word = "".join(sorted(list(word)))
    if sorted_word in dict:
      dict[sorted_word] = [dict[sorted_word], word]
    else:
      dict[sorted_word] = word
  return dict

# is_unique_word('ABILITY') => False
def is_unique_word(word):
  if len(set(word)) > len(word):
    return False
  return True

# remove_single_words({'abc': 'def', 'dac': ['cad', 'acd']}) => {'dac': ['cad, 'acd']}
def remove_single_words(dict):
  for k in dict.keys():
    if type(dict[k]) == type(''):
      dict.pop(k)
  return dict

# generate_squares(1) => [1,4,9]
def generate_squares(length):
  from math import sqrt, ceil, floor
  starting_number = int(ceil(sqrt(pow(10, length - 1))))
  ending_number = int(floor(sqrt(pow(10, length))))
  squares = []
  for num in xrange(starting_number, ending_number + 1):
    square = pow(num, 2)
    # Remove the numbers with duplicate integers.
    if not unique_ints(square):
      continue
    squares += [square]
  return squares

# unique_ints(635997961) => False
def unique_ints(square):
  square = list(str(square))
  if len(square) > len(set(square)):
    return False
  return True

# create_mapping('INTRODUCE', 635997961) => {'I': 6, 'N': 3, 'T': 5, ... }
def create_mapping(word, number):
  dict = {}
  for i in xrange(len(word)):
    dict[word[i]] = int(str(number)[i])
  return dict

# http://stackoverflow.com/questions/2489435/how-could-i-check-if-a-number-is-a-perfect-square
def is_square(n):
  x = n // 2
  seen = set([x])
  while x * x != n:
    x = (x + (n // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def get_other_square(word, mapping):
  number = ""
  for i in word:
    number += str(mapping[i])
  return int(number)

if __name__ == '__main__':
  pairs = remove_single_words(words_to_dict(words)).values()
  starting_length, solution_found = 9, False
  while not solution_found:
    starting_length -= 1
    squares = generate_squares(starting_length)
    for square in squares:
      for pair in pairs:
        if len(pair[0]) != starting_length:
          continue
        mapping = create_mapping(pair[0], square)
        potential_square = get_other_square(pair[1], mapping)
        if len(str(potential_square)) != starting_length or not is_square(potential_square):
          continue
        if potential_square in squares:
          print max(square, potential_square), "is the largest square formed."
          solution_found = True
          
