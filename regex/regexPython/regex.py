import re
def print_match(pattern,text_to_search):
    matches = pattern.finditer(text_to_search)

    for match in matches:
        print(match)
    
text_to_search = '''
abcdefghijklmnopqrtuvwxyz
1234567890

Ha HaHa

MetaChars:
. ^ $ * + ? { } [ ] \ | ( )

teste.com
2222-003-123
1234-003-123
9913-003-123
9913*003*123
9913.003.123
192.168.1.192

Mr. falcatrua
Ms Falcatrua
Ms. falcatrua
Mrs. falcatruas
Mrs. F
aaaaHa
bat
cat
mat
pat
'''

sentence = 'Start a sentence and then brig it to and end'


#use r before string to interpret the string in raw format

pattern = re.compile(r'abc')
print_match(pattern,text_to_search)
#-> return is <_sre.SRE_Match object; span=(1, 4), match='abc'>, so text_to_search[1:4] = abc

pattern = re.compile(r'teste\.com')
print_match(pattern,text_to_search)
#-> return is <_sre.SRE_Match object; span=(88, 97), match='teste.com'>, to search for those metaChars '\' is needed

pattern = re.compile(r'\d')
print_match(pattern,text_to_search)
#-> return all digits

pattern = re.compile(r'\D')
print_match(pattern,text_to_search)
#-> return everything but digits

pattern = re.compile(r'\w')
print_match(pattern,text_to_search)
#-> return all word characters

pattern = re.compile(r'\W')
print_match(pattern,text_to_search)
#-> return all not word characters (\n, whitestapce , .,[ , ], { })

pattern = re.compile(r'\s')
print_match(pattern,text_to_search)
#-> return all space chars (\n, whitestapce , .,...)

pattern = re.compile(r'\S')
print_match(pattern,text_to_search)
#-> return all not space chars (\n, whitestapce , .,)

pattern = re.compile(r'\bHa')
print_match(pattern,text_to_search)
#-> return all that start with Ha (\b =  word boundary)

pattern = re.compile(r'\BHa')
print_match(pattern,text_to_search)
#-> return all that has Ha but not start with Ha (\B =  not word boundary)

pattern = re.compile(r'^Start')
print_match(pattern,sentence)
#-> return all that has 'Start' on the start of the sentence ( ^ for start)

pattern = re.compile(r'end$')
print_match(pattern,sentence)
#-> return that has 'end' on the end of the sentence ( $ for start)

#%%practical tests
#find phone numbers
pattern = re.compile(r'\d\d\d\d[.-]\d\d\d[.-]\d\d\d') # or pattern = re.compile(r'\d\d\d\d.\d\d\d.\d\d\d')
print_match(pattern,text_to_search)

#find phone numbers 8000~9000
pattern = re.compile(r'[89]\d\d\d[.-]\d\d\d[.-]\d\d\d') # or pattern = re.compile(r'\d\d\d\d.\d\d\d.\d\d\d')
print_match(pattern,text_to_search)
#^ inside a character ser ex: [^a-zA-Z] will negate the expression inside and only return digits and space characters in thi case

#everything that ends with at but its not bat
pattern = re.compile(r'[^b]at')
print_match(pattern,text_to_search)

#qunatifiers
pattern = re.compile(r'\d{4}.\d{3}.\d{3}') #-> find \d{number of charactes}
print_match(pattern,text_to_search) 

pattern = re.compile(r'M(r|s|rs)[.]\W\w*') #-> 
print_match(pattern,text_to_search) 

emails = '''
m.coltroscz@gmail.com
marscz@alunos.utfpr.edu.br
macanudo@gmail.com
teste@gmail.com
'''
#emails
pattern = re.compile(r'[a-zA-Z.]+@[^\n]+') #-> 
print_match(pattern,emails) 

urls = '''
https://www.google.com
http://google.com
https://google.com
https://www.brasil.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
print_match(pattern,urls) 

matches = pattern.finditer(urls)
for match in matches:
    print(match)
subbed_url = pattern.sub(r'\2\3',urls)#substitute the url with group 1 and 2












