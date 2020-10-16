def initials(phrase):
    words=phrase.split()
    result=""
    for word in words:
        result+=word[0].upper()
    return result
print(initials("University Santa Barbara"))