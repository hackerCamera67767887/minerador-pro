import sys

def minerar_tudo(nicho):
    plataformas = ["YouTube", "TikTok", "Instagram", "Twitter", "Pinterest"]
    resultados = {}
    
    print(f"--- 🔍 MINERANDO TODAS AS REDES: {nicho} ---")
    for p in plataformas:
        # Lógica simulada - No futuro cada uma terá seu scraper real
        print(f"[+] Analisando {p}...")
        resultados[p] = f"Tendência extraída de {p}"
    
    return resultados

if __name__ == "__main__":
    n = sys.argv[1] if len(sys.argv) > 1 else input("Nicho: ")
    minerar_tudo(n)
