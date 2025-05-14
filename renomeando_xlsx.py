import os
import pandas as pd
import re

# Caminho onde estão seus arquivos .xlsx
pasta_xlsx = "caminho/para/sua/pasta_entrada"  # 🔁 AJUSTE AQUI
pasta_saida = "caminho/para/sua/pasta_saida"   # 🔁 AJUSTE AQUI

# Garante que a pasta de saída exista
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Expressão regular para limpar "Sr.", "Sra.", "(a)", etc.
def limpar_nome(nome):
    padrao = re.compile(r"(Sr\.|Sra\.)\s*\(?a?\)?\s*", re.IGNORECASE)
    nome_limpo = padrao.sub("", nome)  # Remove prefixos
    nome_limpo = re.sub(r'[^\w\s]', '', nome_limpo)  # Remove pontuação
    return nome_limpo.strip().replace(" ", "_")

# Percorrer todos os arquivos na pasta
for arquivo in os.listdir(pasta_xlsx):
    if arquivo.lower().endswith(".xlsx"):
        caminho_arquivo = os.path.join(pasta_xlsx, arquivo)

        # Lê o Excel
        df = pd.read_excel(caminho_arquivo)

        # Verifica se a coluna "Nome" existe
        if "Nome" not in df.columns:
            print(f"❌ Coluna 'Nome' não encontrada no arquivo: {arquivo}")
            continue

        for index, linha in df.iterrows():
            nome = linha["Nome"]
            if pd.notnull(nome):
                nome_arquivo = limpar_nome(str(nome))
                caminho_saida = os.path.join(pasta_saida, f"{nome_arquivo}.xlsx")

                # Salva a linha como novo DataFrame
                linha_df = pd.DataFrame([linha])
                linha_df.to_excel(caminho_saida, index=False)

                print(f"✅ Linha {index + 1} salva como: {nome_arquivo}.xlsx")

print("✅✅ Processo concluído.")
