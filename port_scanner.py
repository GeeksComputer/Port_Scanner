# Mengimpor library
import pyfiglet
import sys
import socket
from datetime import datetime

# Menginisialisasikan fungsi "displayBanner" untuk menampung proses banning
def displayBanner():
    the_banner = pyfiglet.figlet_format("PORT SCANNER") # Menginisialisasikan variabel "the_banner" dengan hasil memanggil method figlet_format untuk membentuk sebuah kata untuk banning
    print(the_banner) # Mencetak banner yang sudah dibentuk

# Menginisialisasikan fungsi "processPortScan" untuk menampung proses pemindaian port
def processPortScan():
    if len(sys.argv) == 2: # Pengkondisian if untuk menjalankan sebuah kode program dengan tambahan sebuah argumen sebagai syarat
        target = socket.gethostbyname(sys.argv[1]) # Menginisialisasikan variabel "target" dengan hasil berupa method untuk memasukkan alamat IP target yang akan dipindai
        displayBanner() # Memanggil fungsi "displayBanner" untuk menjalankan proses banning
    else: # Pengkondisian else jika kode program dijalankan tanpa menggunakan argumen atau salah memasukkan argumen
        print("Invalid amount of Argument") # Mencetak peringatan
        
    print("-" * 50) # Mencetak banner strip
    print("Scanning Target: " + target) # Mencetak target yang dipindai
    print("Scanning started at: " + str(datetime.now())) # Mencetak string method berupa waktu sekarang
    print("-" * 50) # Mencetak banner strip
    
    try: # Try exception Handling untuk melakukan percobaan menjalankan statement
        for port in range(1, 65535): # Perulangan for untuk menampilkan angka 1 sampai 65535
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Menginisialisasikan variabel "s" dengan hasil berupa method untuk melakukan menghubungkan socket dengan port target
            socket.setdefaulttimeout(1) # Method untuk mengatur waktu habis dalam penghubungan
            
            result = s.connect_ex((target, port)) # Menginisialisasikan variabel "result" dengan hasil berupa method untuk memulai menghubungkan port target
            
            if result == 0: # Pengkondisian if jika hasil dari variabel "result" berhasil terhubung
                print("Port {} is open". format(port)) # Mencetak port target yang telah dipindai
            s.close() # Method untuk memutuskan hubungan dengan port target
    except KeyboardInterrupt: # Except jika terjadi interupsi
        print("\n Exiting Program !!!") # Mencetak peringatan
        sys.exit() # Method untuk keluar dari program sistem
    except socket.gaierror: # Except jika terjadi kesalahan pada port target tidak dapat dipindai
        print("\n Hostname Could Not Be Resolved") # Mencetak peringatan
    except socket.error: # Except jika terjadi kesalahan pada port target yang dipindai
        print("\n Server Not Responding") # Mencetak peringatan

# Pengkondisian if untuk menjalankan kode program
if __name__ == "__main__":
    processPortScan() # Memanggil fungsi untuk menjalankan proses port scanning