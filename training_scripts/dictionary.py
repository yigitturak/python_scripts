# key assign to value structure = Key:Value

def getAcronym(dict, acr):
    defination = dict.get(acr)
    if defination:
        return acr+"="+defination
    else:
        return "Key doesn't exist"

def setAcronym(dict,acr,defi):
    dict[acr]=defi
    return dict

acronyms={
    'LOL':'laugh out load',
    'IDK':'I don\'t know',
    'TBH':'to be honest',
    'BTW':'by the way'
}
print(acronyms.get('laugh out load')[0])
print(getAcronym(acronyms,'AFAIK'))
print(getAcronym(acronyms,'BTW'))
print(setAcronym(acronyms,'AFAIK','As far as I know'))
print(setAcronym(acronyms,'TBH','honestly'))
print(getAcronym(acronyms,'AFAIK'))

