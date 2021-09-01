print('*** Reading E-Book ***')
text,hl = input('Text , Highlight : ').split(',')
print(text.replace(hl,'['+hl+']'))