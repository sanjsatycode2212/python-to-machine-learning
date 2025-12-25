def pallindrom(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]

    if rev == st :
        print(f"st is pallindrom :- {st}")
    else:
        print(f"st is not pallindromic :- {st}")
pallindrom("satyam")


def hello():
    return " i hope you understand if no then visit."
    # print(" i hope you understand if no then visit.") # step 1>>
# hello() # yaha function ko call krne per kuch nhi aa rha he kyuki uper jo return he ushe print karana hi dega 2 type se print ho skta he.
print(hello()) # step 2>>>