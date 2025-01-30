def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    counter(file_contents)
    print(file_contents[:100])
    

def counter(book):
    words = book.split()
    lines = book.split('\n')
    print("Number of lines:", len(lines))
    print("Total count:", len(words))
    return len(words)


main()