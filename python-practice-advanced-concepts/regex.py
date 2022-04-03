import re
import random

# compile the pattern
# good practice to store the pattern in a variable if it is re-used
pattern = re.compile('l[aeiou]ve')
match_result = pattern.search('lqve is live but not lwove however lave yet luve can be leve so lpve is true love')

find_capitol_words = re.search('[A-Z]+', 'CAPITAL is captial letterS')

print(match_result)
print(find_capitol_words)


def clean_sentence(match):
    sentence = match.group(0)
    random_chars = [random.choice('!@#$%^&*') for letter in sentence]
    return '.'.join(random_chars)

class regExp:

    def find_non_word_char(self):
        patn = re.compile(r'\W')
        rt = patn.search('ThomasMJefferson@gmail.com')
        print(rt)

    def check_first_match(self):
        p = re.compile(r'\W')
        rt = p.match('!$isthepassword')
        print(rt)

    def full_match(self):
        p = re.compile(r'[\w\.]+@example.com')
        rt = p.match('JeffreyAdams@example.com')
        print(rt)

    def find_all_match(self):
        p = re.compile(r'\W')
        rt = p.findall('Th!s i5 a str0ng pas5word!@#$')
        print(rt)


    def execute_clean_sentence(self):
        pattern = r'\b[a-z]*(stupid|stinky|darn|shucks|crud|slob)[a-z]*\b'
        p = re.compile(pattern, re.IGNORECASE | re.MULTILINE)
        sentence = """Shucks! What a cruddy day I\'ve had.
        16. I spent the whole darn day with my slobbiest 17. friend darning his STINKY socks."""
        result = p.sub(clean_sentence, sentence)
        print(result)


if __name__ == "__main__":
    regex_obj = regExp()
    regex_obj.find_non_word_char()
    regex_obj.check_first_match()
    regex_obj.full_match()
    regex_obj.find_all_match()
    regex_obj.execute_clean_sentence()