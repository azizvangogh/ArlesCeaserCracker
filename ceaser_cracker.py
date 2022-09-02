message = input("Şifreli Mesajınızı giriniz: ")
harfler = ["a" , "b" , "c" ,"ç" ,"d" , "e" , "f" , "g" , "h" , "ı" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "ö" , "p" , "q" , "r" , "s" , "ş" , "t" , "u" , "ü" , "v" , "w" , "x" , "y" , "z"]

for key in range(len(harfler)):
    translated = ""
    for symbol in message:
        if symbol in harfler:
            num = harfler.index(symbol)
            num = num - key
            if num < 0:
                num = num + len(harfler)
            translated = translated + harfler[num]
        else:
            translated = translated + symbol
    print(translated)
    print("Şifre Anahtarı: " + str(key))
    
