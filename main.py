import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
from stats import wordcount
from stats import character_count
from stats import splitted
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    wordbook = get_book_text(book_path)
    the_count = wordcount(wordbook)
    print("----------- Word Count ----------")
    print(f"Found {the_count} total words")
    count1 = character_count(wordbook)
    count2 = splitted(count1)
    print("--------- Character Count -------")
    for outcome in count2:
        print(f"{outcome['char']}: {outcome['num']}")
    print("============= END ===============")
main()
