t = input("Введите температуру: ")
t = t.upper().strip() #все заглавные и без пробелов 
last = t[-1]
t = float(t[:-1])
print(last)
print(t)

if last == "C":
    f = (t*1.8)+32 
    print(f)
else:
    c = (t - 32)/1.8
    print(c)