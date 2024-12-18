import locale
locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')





class BankaHesabi():
    def __init__ (self,hesapSahibi):
        self.hesapSahibi = ad
        self.bakiye = 0.0
    
    def get_bakiye(self):
        return self.bakiye

    def paraYatir(self,miktar):
        self.bakiye += miktar
        return self.bakiye

    def paraCek(self,miktar):
        self.bakiye -= miktar
        return self.bakiye
    

ad = input("Hesap adınızı giriniz= ")
bakiye=0.0
print("Bakiyeniz = " + str(bakiye))
yatir = int(input("Yatırmak istediğiniz tutarı giriniz= "))


hesap = BankaHesabi(ad)
print(str(hesap.paraYatir(yatir)) + "TL hesabınıza yatırılmıştır.")


print("Güncel bakiyeniz= " + str(hesap.get_bakiye()))

cek = int(input("Çekmek istediğiniz tutarı giriniz= "))
if(hesap.get_bakiye() > cek):
    print(cek + str("TL hesabınızdan çekilmiştir."))
    print("\n\nGüncel bakiyeniz = " + str(hesap.get_bakiye()))
else:
    print("Hesabınızda o kadar para bulunamadi!")




