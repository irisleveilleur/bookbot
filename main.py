def count_characters(input):
    characters = {}
    string = input.lower()
    
    for char in string:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def count_words(input):
    split_book = input.split()
    return len(split_book)

def sort_function(input):
    return input["count"]

def sort_characters(input):
    list_of_characters = []
    for char in input:
        list_of_characters.append({
            "name": char, 
            "count": input[char]
        })
    list_of_characters.sort(key=sort_function, reverse=True)
    return list_of_characters

def main():
    with open('books/frankenstein.txt', 'r') as f:
        book = f.read()
        print("-- Book Statistics --")
        print(f"Book contains {count_words(book)} words\n")

        sorted_chars = sort_characters(count_characters(book))

        for dict in sorted_chars:
            print(f"Character: '{dict['name']}' appears {dict['count']} times")
        
        print("\n-- Book End --")

main()

