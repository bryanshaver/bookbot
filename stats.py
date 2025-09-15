def get_num_words(text):
    words = text.split()
    count = 0
    for w in words:
        count += 1
    return f"Found {count} total words"

def character_count(text):
    lower_text = text.lower()
    character_dict = {}
    text_split = list(lower_text)
    for c in text_split:
        if c in character_dict:
            character_dict[c] += 1
        else:
            character_dict.update({c: 1})
    
    return character_dict

def sort_on(items):
    return items["num"]

def sort_dict(counts):
    records = []
    for ch, cnt in counts.items():
        if ch.isalpha():
            records.append({"char": ch, "num": cnt})
        else:
            pass
    records.sort(reverse=True, key=sort_on)
    return records
