from stats import count, count_characters, sort_characters_by_count
import sys

def get_book_text(filepath):            
    with open(filepath) as f:       
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")  # <-- python3 here
        sys.exit(1)

    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)

    print(f"""
============ BOOKBOT ============
Analyzing book found at {path_to_file}...
----------- Word Count ----------
Found {count(book_text)} total words
--------- Character Count -------
""")

    for item in sort_characters_by_count(count_characters(book_text)):
        print(f"{item['char']}: {item['num']}")

    print("""
============= END ===============
""")

if __name__ == "__main__":
    main()
