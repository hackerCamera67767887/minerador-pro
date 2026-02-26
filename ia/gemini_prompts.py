def gerar_ferramentas_fornecedor(nicho):
    print(f"--- RELATÓRIO PARA FORNECEDORES: {nicho.upper()} ---")
    print("1. Melhores Ferramentas: [CapCut, Canva Pro, VidIQ]")
    print(f"2. Prompt Mestre: 'Atue como um especialista em {nicho} e crie 10 ideias de títulos virais...'")
    print("3. Estratégia: Postar 3x ao dia com foco em retenção de 3 segundos.")

if __name__ == "__main__":
    n = input("Qual nicho os fornecedores estão pedindo? ")
    gerar_ferramentas_fornecedor(n)
