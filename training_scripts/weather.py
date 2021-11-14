temp = int(input("what is the degree of the weather?"))
rain = input("is it raining or not (yes/no)")
if temp >=28 or rain == "yes":
    if not rain == "yes": 
        print ('it is too hot and stay at home')
    else:
        print ('It is raining and stay at home')
else:
    print ('enjoy your day')