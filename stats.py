def get_num_words(text):
    words = text.split()
    count = 0
    for w in words:
        count += 1
    print(f"{count} words found in the document")

