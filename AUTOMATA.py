class DFA:
    def __init__(self):
        self.alfabe = {'0', '1'}
        self.durumlar = {'q0', 'q1', 'q2'}
        self.baslangıc_durum = 'q0'
        self.final_durum = {'q2'}
        self.gecisler = {
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q2', '1': 'q0'},
            'q2': {'0': 'q2', '1': 'q0'}
        }
        self.mevcut_durum = self.baslangıc_durum
        self.gecis_tarihi = []

    def cizim_dfa(self):
        """ASCII karakterleri kullanarak DFA'yı çiz"""
        print("\nDFA Görsel Temsili:")
        print("--------------------")
        print("        0           0           0    ")
        print("  -->  q0 -----> q1 -----> q2((")
        print("       ↺    ↖    ↓           ↺")
        print("       1     \\   1           0")
        print("              \\  ↓          ")
        print("               \\ q0         1")
        print("                \\            |")
        print("                 \\___________|")
        print("\nNotlar:")
        print("- -->  : Başlangıç durumu")
        print("- ((   : Kabul durumu")
        print("- q0   : Başlangıç durumu")
        print("- q1   : Ara durum")
        print("- q2   : Kabul durumu")
        print("- ↺    : Kendine döngü")
        print("- →    : Durum geçişi")
        print("- \\ ve | kullanımı : 1 ile q0'a dönüş")
        print("--------------------")
        print("\nGeçiş açıklamaları:")
        print("1. q0'dan:")
        print("   - 0 ile q1'e geçer")
        print("   - 1 ile kendine döner (q0)")
        print("2. q1'den:")
        print("   - 0 ile q2'ye geçer")
        print("   - 1 ile q0'a döner")
        print("3. q2'den:")
        print("   - 0 ile kendine döner (q2)")
        print("   - 1 ile q0'a döner")

    def gecis_islemi(self, input_symbol):
        if input_symbol not in self.alfabe:
            raise ValueError(f"Geçersiz input sembolü: {input_symbol}")

        old_state = self.mevcut_durum
        self.mevcut_durum = self.gecisler[self.mevcut_durum][input_symbol]

        gecis_infosu = {
            'from_state': old_state,
            'input': input_symbol,
            'to_state': self.mevcut_durum
        }
        self.gecis_tarihi.append(gecis_infosu)

    def yenileme(self):
        self.mevcut_durum = self.baslangıc_durum
        self.gecis_tarihi = []

    def kabul_etme(self, input_string):
        self.yenileme()

        try:
            # Önce string'in geçerli olup olmadığını kontrol et
            gecersiz_karakterler = [char for char in input_string if char not in self.alfabe]
            if gecersiz_karakterler:
                print("\nHATA: Geçersiz karakter(ler) tespit edildi!")
                print(f"Geçersiz karakter(ler): {', '.join(gecersiz_karakterler)}")
                print("Lütfen sadece 0 ve 1 karakterlerini kullanın!")
                return "REJECTED (Geçersiz Input)"

            print("\nGeçiş adımları:")
            print(f"Başlangıç durumu: {self.mevcut_durum}")

            if not input_string:
                print("HATA: Boş string girildi!")
                print("Lütfen en az bir karakter içeren bir string girin!")
                return "REJECTED (Boş Input)"

            for symbol in input_string:
                old_state = self.mevcut_durum
                self.gecis_islemi(symbol)
                print(f"{old_state} --({symbol})--> {self.mevcut_durum}")

            result = "ACCEPTED" if self.mevcut_durum in self.final_durum else "REJECTED"
            print(f"\nSon durum: {self.mevcut_durum}")
            print(f"Sonuç: {result}")
            return result

        except Exception as e:
            print(f"\nHATA: Beklenmeyen bir hata oluştu!")
            print(f"Hata detayı: {str(e)}")
            return "REJECTED (Hata)"

    def print_formal_definition(self):
        print("\nDFA Formal Tanımı:")
        print("------------------")
        print(f"Alfabe (Σ) = {self.alfabe}")
        print(f"Durumlar (Q) = {self.durumlar}")
        print(f"Başlangıç durumu = {self.baslangıc_durum}")
        print(f"Kabul durumları (F) = {self.final_durum}")
        print("Geçiş fonksiyonu (δ):")
        for state in self.gecisler:
            for symbol in self.gecisler[state]:
                print(f"  δ({state}, {symbol}) = {self.gecisler[state][symbol]}")
        print("------------------")


def main():
    dfa = DFA()

    while True:
        print("\nDFA Test Menüsü")
        print("---------------")
        print("1. DFA'yı görüntüle")
        print("2. String test et")
        print("3. Formal tanımı göster")
        print("4. Çıkış")
        print("---------------")

        seciminiz = input("\nSeçiminiz (1-4): ")

        if seciminiz == '1':
            dfa.cizim_dfa()

        elif seciminiz == '2':
            print("\nTest edilecek stringi girin:")
            user_input = input().strip().lower()
            dfa.kabul_etme(user_input)

        elif seciminiz == '3':
            dfa.print_formal_definition()

        elif seciminiz == '4':
            print("\nProgram sonlandırılıyor... :)")
            break

        else:
            print("\nGeçersiz seçim! Lütfen 1-4 arası bir sayı girin.")


if __name__ == "__main__":
    main()