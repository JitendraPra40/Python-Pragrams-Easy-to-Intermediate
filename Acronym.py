def acronym(phrase):
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

phrase =input('Enter full a organiazation name:\n')
print(acronym(phrase))
