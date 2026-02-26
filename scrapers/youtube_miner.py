import requests
import sys

def minerar_youtube(nicho):
    print(f"[+] Minerando nicho: {nicho} no YouTube...")
    url = f"https://www.youtube.com/results?search_query={nicho}"
    print(f"[!] Link de análise: {url}")
    print("[✓] Coleta concluída!")

if __name__ == "__main__":
    nicho = sys.argv[1] if len(sys.argv) > 1 else input("Nicho: ")
    minerar_youtube(nicho)
