def ortalama_hesapla(sayilar):
    if not sayilar:  # Eğer liste boşsa
        return 0
    return sum(sayilar) / len(sayilar)

def main():
    sayilar = []
    while True:
        giris = input("Bir tam sayı girin (çıkmak için 'q' yazın): ")
        if giris.lower() == 'q':
            break
        try:
            sayi = int(giris)
            sayilar.append(sayi)
        except ValueError:
            print("Lütfen geçerli bir tam sayı girin.")

    if sayilar:
        ortalama = ortalama_hesapla(sayilar)
        print(f"Girdiğiniz sayıların ortalaması: {ortalama}")
    else:
        print("Hiç sayı girilmedi.")

if __name__ == "__main__":
    main()