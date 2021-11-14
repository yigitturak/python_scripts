# key assign to value structure = Key:Value
acronyms={
    'LOL':'laugh out load',
    'IDK':'I don\'t know',
    'TBH':'to be honest',
    'BTW':'by the way'
}
print(acronyms)

acronyms['AFAIK'] = 'As far as I know'

print(acronyms)

acronyms['TBH']='honestly'
print(acronyms)

defination1=acronyms.get('BTW')
if defination1:
    print(defination1)
else:
    print("Key doesn't exist")

defination2=acronyms.get('ASL')
if defination2:
    print(defination2)
else:
    print("Key doesn't exist")