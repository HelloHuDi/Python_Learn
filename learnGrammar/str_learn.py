# -*- coding:utf-8 -*-
favorite_language = " learn python the more"
print(favorite_language.__len__())
print(favorite_language.title())
print(favorite_language.lower())
print(favorite_language.upper())
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
print(favorite_language.find("th"))
print(favorite_language.find("th", 12))
print(favorite_language[favorite_language.find("th"):14])
print("=======")
favorite_language = favorite_language.strip()
print(favorite_language)


def get_formatted_name(first, last, middle=''):
    print(str("\njie ")+middle)
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()
