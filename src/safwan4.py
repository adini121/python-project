
from collections import Counter
dictionary =Counter({('findElement', 'id'): 6, ('findElement', 'cssselector'): 4, ('findElement', 'partiallinktext'): 1, ('findChildElements', 'xpath'): 1})
for key, value in dictionary.items():
    print key[0], ":", key[1], ">>", value