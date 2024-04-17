
book_path = "brianmina/bookbot/books/franksnstein.txt"

def read_book():
   
    with open(book_path) as f:
        file_content = f.read().lower()
        chars_dict = {}
        for c in file_content:
            if c in chars_dict:
                chars_dict[c] += 1
            else:
                chars_dict[c] = 1
        for i in chars_dict:
            print(f"The '{i}' character was found {chars_dict[i]} times ")        
        words = file_content.split()
        print(f"{len(words)} were found in this book")

read_book()