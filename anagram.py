def check_anagram(string_1, string_2):
    string_1 = ''.join(sorted(string_1))
    string_2 = ''.join(sorted(string_2))

    if string_1 == string_2:
        return True
    return False

string_1 = "Mary"
string_2 = "Army"

print(check_anagram(string_1.lower(), string_2.lower()))