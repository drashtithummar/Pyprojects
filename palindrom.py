def is_pal(str):
    new_str=""
    reverse_str=""
    for x in str:
        if x!=" ":
            new_str+=x
            reverse_str=x+reverse_str
    if new_str.lower()==reverse_str.lower():
            return True
    return False
print(is_pal("161"))