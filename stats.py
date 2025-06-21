def wordcount(string_to_count):
    words = string_to_count.split()
    return len(words)
def character_count(characters):
    lowercase = characters.lower()
    count = {}
    for char in lowercase:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count
def splitted(character_count):
    character_list = []
    for char, num in character_count.items():
        if char.isalpha():
            char_data = {"char": char, "num": num}
            character_list.append(char_data)
    character_list.sort(reverse=True, key=sorting)
    return character_list
def sorting(numbers):
    return numbers["num"]

