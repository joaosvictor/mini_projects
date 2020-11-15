#!/usr/bin/python3
# hash table will call the dictionary
voted = {} # here are the hash table = "{}"
def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")

check_voter("Victor")
check_voter("Ana")
check_voter("Thiago")
