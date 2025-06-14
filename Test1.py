isText=False
while not isText:
    text= input('Enter your text:')
    if text.lower() =='a':
        print("found letter A")
        isText=True
    elif text != 'a':
        print("Try agian")
        