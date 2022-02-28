# Text from https://gutenberg.ca/ebooks/hemingwaye-oldmanandthesea/hemingwaye-oldmanandthesea-00-h.html
# Copy and pasted into txt placed in the same folder as the .py
file = open('./old_man_and_the_sea.txt', 'r')
data = file.read()

word = input('Vilket ord i The old man and the sea (lite mindre än halva boken) ska räknas (eng)? ')
occurence = data.count(word)
print(f'Ordet förekommer {occurence} gånger.')