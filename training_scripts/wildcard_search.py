s=input("input string: ")
p=input("pattern: ")

def matchingQue(s,p):
    result=""
    for i in range(0,len(s)):
        if s[i] == p[i] or p[i] == "?":
            result="TRUE"
        else:
            result="FALSE"
    return result

def matchingStar(s,p,index):
    result=""
    new_s=""
    start_p=p.split('*')[0]
    end_p=p.split('*')[1]
    for i in range(0,len(start_p)):
        if s[i] == p[i]:
            result="TRUE"
        else:
            result="FALSE"
    for j in range(len(s)-len(end_p),len(s)):
        new_s=new_s+s[j]
    if new_s==end_p:
        result="TRUE"
    else:
        result="FALSE"
    return result

if not "?" in p and not "*" in p:
    if s == p:
        print("TRUE")
    else:
        print ("FALSE")
elif p == "*":
    print("TRUE")
elif p == "?":
    if len(s) == 1:
        print("TRUE")
    else:
        print("FALSE")
elif "?" in p and not "*" in p:
    if not len(s) == len(p):
        print("FALSE")
    else:
        print(matchingQue(s,p))
elif "*" in p and not "?" in p:
    if p[0] == "*":
        new_p=p.replace('*','')
        if new_p in s:
            print("TRUE")
        else:
            print("FALSE")
    else:
        print(matchingStar(s,p,p.index('*')))
