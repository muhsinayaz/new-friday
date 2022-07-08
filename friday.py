print("Have a nice Friday")
def cikartma(x,y):
    return max(int(x),int(y)) - min(int(x),int(y))
def giris():
    a = input("1. Sayıyı giriniz: ") 
    b = input("2. Sayıyı giriniz: ")
    return cikartma(a,b) if a != b and a.isdigit() and b.isdigit() else giris()
print(giris())
print("Have a nice Friday")
