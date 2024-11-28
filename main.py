"""Main python """
def get_book_contents(book_path):
    """Function to get the contents of a book in the books directory."""
    with open (book_path, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def get_book_text_count(text):
    """Function to get the text count of a book."""
    text_words_count = len(text.split())
    return text_words_count

def get_charecter_count(text):
    """Function to get the count of each char in a book."""
    charecters_dict = {}
    for char in text:
        char = char.lower()
        if(char not in charecters_dict):
            charecters_dict[char] = 1
        else:
            charecters_dict[char] += 1
    return charecters_dict

def sort_charecter_counts(charecter_counts):
    def sort_on(dict):
        return dict["count"]
    
    list_of_dict = []
    for item in charecter_counts:
        list_of_dict.append({"name":item,"count":charecter_counts[item]})
    list_of_dict.sort(reverse=True, key=sort_on)
    return(list_of_dict)
    

def main():
    """Main function."""
    #book_path = f"books/{input("which book?: ")}"
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_contents(book_path)
    text_word_count = get_book_text_count(text)
    charecter_counts = get_charecter_count(text)
    sorted_charecter_counts = sort_charecter_counts(charecter_counts)
    sort_charecter_counts(charecter_counts)
    print(f"{text_word_count} words were found in this document")
    for charecter in sorted_charecter_counts:
        if charecter["name"].isalpha():
            print(f"the '{charecter["name"]}' character was found {charecter["count"]} times")
    print ("--- End report ---")
main()
