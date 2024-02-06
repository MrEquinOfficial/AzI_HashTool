import hashlib
import pyfiglet
def hash_cracker(hash_value, hash_type, wordlist):
    with open(wordlist, "r") as f:
        for line in f:
            word = line.strip()
            if hash_type == "md5":
                hash_obj = hashlib.md5(word.encode())
            elif hash_type == "sha1":
                hash_obj = hashlib.sha1(word.encode())
            elif hash_type == "sha3":
                hash_obj = hashlib.sha3_256(word.encode())
                hash_obj = hashlib.sha3_512(word.encode())
            elif hash_type == "blake2":
                hash_obj = hashlib.blake2b(your_passwd).hexdigest()
                hash_obj = hashlib.blake2s(your_passwd).hexdigest()
            if hash_obj.hexdigest() == hash_value:
                return word
    return None
banner = pyfiglet.figlet_format("QrNX\nHASH TOOL")
print(""" \033[96m

   ('-.       .-') _           ('-. .-.   ('-.      .-')    ('-. .-. 
  ( OO ).-.  (  OO) )         ( OO )  /  ( OO ).-. ( OO ). ( OO )  / 
  / . --. /,(_)----.   ,-.-') ,--. ,--.  / . --. /(_)---\_),--. ,--. 
  | \-.  \ |       |   |  |OO)|  | |  |  | \-.  \ /    _ | |  | |  | 
.-'-'  |  |'--.   /    |  |  \|   .|  |.-'-'  |  |\  :` `. |   .|  | 
 \| |_.'  |(_/   /     |  |(_/|       | \| |_.'  | '..`''.)|       | 
  |  .-.  | /   /___  ,|  |_.'|  .-.  |  |  .-.  |.-._)   \|  .-.  | 
  |  | |  ||        |(_|  |   |  | |  |  |  | |  |\       /|  | |  | 
  `--' `--'`--------'  `--'   `--' `--'  `--' `--' `-----' `--' `--' 

""")
wordlist = "w0rdlist.txt"
option = int(input("        {1} Encode(Şifrələ)\n        {2} Decode(Şifrəni qır)\n\nSeçimini yaz > "))
while True:
    if option == 1:
        your_passwd = str(input("Şifrələyəcəyin sətiri qeyd et > ")).encode()
        algorithm = int(input("Şifrələmə tipini seç :\n1-MD5\n2-SHA2\n3-SHA3\n4-BLAKE2\n > "))
        if algorithm == 1:
            print("Şifrələnmiş sətir : \033[95m",hashlib.md5(your_passwd).hexdigest(),"\033[96m")
        elif algorithm == 2:
            print("Şifrələnmiş sətir(SHA2-256Bit) : \033[95m",hashlib.sha256(your_passwd).hexdigest(),"\033[96m")
            print("Şifrələnmiş sətir(SHA2-512Bit) : \033[95m",hashlib.sha512(your_passwd).hexdigest(),"\033[96m")
        elif algorithm == 3:
            print("Şifrələnmiş sətir(SHA3-256Bit) : \033[95m",hashlib.sha3_256(your_passwd).hexdigest(),"\033[96m")
            print("Şifrələnmiş sətir(SHA3-512Bit) : \033[95m",hashlib.sha3_512(your_passwd).hexdigest(),"\033[96m")
        elif algorithm == 4:
            print("Şifrələnmiş sətir(BLAKE2B) : \033[95m",hashlib.blake2b(your_passwd).hexdigest(),"\033[96m")
            print("Şifrələnmiş sətir(BLAKE2S) : \033[95m",hashlib.blake2s(your_passwd).hexdigest(),"\033[96m")
        cont = input("Davam eləmək istəyirsən? [h/y] > ")
        if cont == "y":
            break
    elif option == 2:
        your_passwd = str(input("Qırılacaq şifrəni qeyd et > "))
        algorithm = int(input("Qırılacaq şifrənin tipini qeyd et :\n1-MD5\n2-SHA2\n3-SHA3\n4-BLAKE2\n > "))
        if algorithm == 1:
            plain_text = hash_cracker(your_passwd,"md5", wordlist)
            if plain_text:
                print("Şifrə asanlıqla qırıldı.\n Qırılmış şifrə : \033[95m", plain_text, "\033[96m")
            else:
                print("Wordlist-də bu şifrə tapılmadı.")
        elif algorithm == 2:
            plain_text = hash_cracker(your_passwd,"sha1", wordlist)
            if plain_text:
                print("Şifrə asanlıqla qırıldı.\n Qırılmış şifrə : \033[95m", plain_text, "\033[96m")
            else:
                print("Wordlist-də bu şifrə tapılmadı.")
        elif algorithm == 3:
            plain_text = hash_cracker(your_passwd,"sha3", wordlist)
            if plain_text:
                print("Şifrə asanlıqla qırıldı.\n Qırılmış şifrə : \033[95m", plain_text, "\033[96m")
            else:
                print("Wordlist-də bu şifrə tapılmadı.")
        elif algorithm == 4:
            plain_text = hash_cracker(your_passwd,"blake2", wordlist)
            if plain_text:
                print("Şifrə asanlıqla qırıldı.\n Qırılmış şifrə : \033[95m", plain_text, "\033[96m")
            else:
                print("Wordlist-də bu şifrə tapılmadı.")
        cont = input("Davam eləmək istəyirsən? [h/y] > ")
        if cont == "y":
            break
