# removing unicode characters
# https://www.pythonpool.com/remove-unicode-characters-python/

s = 'nachiket\u00a9'
print(s)
s2 = s.encode('ascii','ignore').decode('ascii')
print(s2)

# curved quotes is a unicode character
s = '“'.encode('unicode_escape')
print(s)
print('\u201c')
