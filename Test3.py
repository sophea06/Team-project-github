text="AaBabaCcDdafe"
total =0
for char in text:
    if char.lower()== 'b' or char.lower()== "c" or char.lower() =="d":
        total += 1
print ( "Total:" ,total)