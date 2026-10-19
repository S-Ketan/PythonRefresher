import json

book={}
book['tom']={
    'name':'tom',
    'address':'NY city',
    'number':'649404940'
}
book['bob']={
    'name':'Bob',
    'address':'Mexico',
    'number':'645456145'
    }
book['digga']={
        'name':'digga',
        'address':'Canada',
        'number':'72848416'
    }
# print(type(book))
s=json.dumps(book)
# print(s)
# print(type(s))

# with open("/home/ketan/Desktop/AIML/book.txt","w") as f:
#     f.write(s)
a= open("/home/ketan/Desktop/AIML/book.txt","r")
b=a.read()
print(b)
print(type(b))
bookBack=json.loads(b)
print(bookBack['bob'])
print(type(bookBack))
