def all_variants(text):
    length_text = len(text)
    for i in range(length_text):
        start = 0
        for j in range(i+1, length_text+1):
            yield text[start:j]
            start += 1


a = all_variants("abc")
for i in a:
    print(i)