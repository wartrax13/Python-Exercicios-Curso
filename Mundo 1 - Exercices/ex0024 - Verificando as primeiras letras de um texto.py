#A cidade contem ou não santo no nome?
a = str(input('Diga o nome de uma cidade: ')).strip()
print(a[:5].upper() == 'SANTO')
