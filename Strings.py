name = 'jagRoop'
middle = '''Singh'''
surname = "v i r k"
line = """Sometimes\tthis\tis\nuseful 123"""
yob = '1986'
multiline = '''\
I am trying
to learn
Python'''
para = ('this isn\'t bad. '
        "that'll also work")

print(name)
print(name[0])
print(name[0:2])
print(name[3:-2])
print(name[:-4])
print(name[-4:])
print('V' + surname[1:])
print(multiline)
print(para)
print(name+surname)
print(name + " " + middle + ' ' + surname)

print(len(multiline))
print("<"*4 + "-"*3 + ">"*5)
print(name.capitalize())
print(name.casefold()) # similar to lowercase but changes characters to ACSII
print(name.center(11, "-"))
print(name.count('o', 0, len(name)))
print(name.endswith('j', 0, len(name)))
print(name.endswith('p'))
print(line.expandtabs())
print(name.find('o')) # can be given specific length
print('j' in name)
print(name.index('p'))
print(name.isalnum(), name.isalpha(), line.isalnum(), yob.isdigit())
print(name.join('      '))
print(name.partition('R'))
print('1,2,3,,4'.split(','))
print('1,2,3,,4'.split(',', maxsplit=2))
print(surname.split())

s = 'This is {}, {}, {}'
print(s.format('one', 2, 3))

s1 = 'This is {1:10d}, {3:.2f}, {0}, {2}'
print(s1.format('one', 2, 'three', 4.12345))

s2 = 'This is {1:10d}, {3:.2f}, {0}, {2}'
print(s2.format('one', 120, 'three', 4.12345))