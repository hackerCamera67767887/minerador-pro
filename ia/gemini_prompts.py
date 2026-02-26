def gerar_prompt(nicho, tendencia):
    return f"Roteiro TikTok: Nicho {nicho}, Trend {tendencia}. Use tom viral."

if __name__ == "__main__":
    n = input("Nicho: "); t = input("Trend: ")
    print(gerar_prompt(n, t))
