
letter = '''Dear <|name|>
how are you! Hope you are fine.
<|date|>
<|city|>'''
print(letter.replace("<|name|>","Farhan Khan").replace("<|date|>","7 July,2024").replace("<|city|>","Delhi"))
