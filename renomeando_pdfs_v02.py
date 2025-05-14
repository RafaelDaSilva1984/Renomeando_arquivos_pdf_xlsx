import os
import pdfplumber
import re
from PyPDF2 import PdfWriter, PdfReader

# Caminho para a pasta que contém os arquivos PDF de entrada
pasta_pdf = r"C:\CAMINHO\DA\PASTA\ENTRADA"  # <<-- Altere aqui

# Caminho para a pasta onde os novos arquivos serão salvos
pasta_saida = r"C:\CAMINHO\DA\PASTA\SAIDA"  # <<-- Altere aqui

# Cria a pasta de saída, se não existir
os.makedirs(pasta_saida, exist_ok=True)

# Expressão regular para capturar nomes com "Sr.", "Sra.", "(a)", etc.
padrao_nome = re.compile(r"(Sr\.|Sra\.)\s*\(?a?\)?\s*([\wÀ-ÿ\s\.]+(?:\s+[A-Za-zÀ-ÿ\s\.]+)*)", re.IGNORECASE)

def extrair_nome_ate_ref(texto):
    texto_limpo = " ".join(texto.split())  # Remove quebras de linha e espaços duplicados
    texto_ate_ref = texto_limpo.split("Ref.:")[0]
    match = padrao_nome.search(texto_ate_ref)
    if match:
        return match.group(2).strip()
    return None

def salvar_paginas_separadas(caminho_pdf, pasta_saida):
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            pdf_reader = PdfReader(caminho_pdf)
            for i, pagina in enumerate(pdf.pages):
                texto = pagina.extract_text()
                if texto:
                    nome_extraido = extrair_nome_ate_ref(texto)
                    if nome_extraido:
                        nome_limpo = re.sub(r'[^\w\s\.]', '', nome_extraido).strip().replace(" ", "_")

                        # Evita sobrescrever arquivos com nomes iguais
                        nome_base = nome_limpo
                        contador = 1
                        while os.path.exists(os.path.join(pasta_saida, f"{nome_limpo}.pdf")):
                            nome_limpo = f"{nome_base}_{contador}"
                            contador += 1

                        novo_nome = f"{nome_limpo}.pdf"
                        caminho_novo = os.path.join(pasta_saida, novo_nome)

                        # Salva a página como novo PDF
                        pdf_writer = PdfWriter()
                        pdf_writer.add_page(pdf_reader.pages[i])
                        with open(caminho_novo, "wb") as output_pdf:
                            pdf_writer.write(output_pdf)

                        print(f"[✔] Página {i+1} salva como: {novo_nome}")
                    else:
                        print(f"[!] Nome não encontrado na página {i+1} do arquivo {os.path.basename(caminho_pdf)}")
    except Exception as e:
        print(f"[ERRO] Ao processar {caminho_pdf}: {e}")

# Processa todos os PDFs na pasta
for arquivo in os.listdir(pasta_pdf):
    if arquivo.lower().endswith(".pdf"):
        caminho_arquivo = os.path.join(pasta_pdf, arquivo)
        salvar_paginas_separadas(caminho_arquivo, pasta_saida)

print("\n✅ Processo finalizado com sucesso.")


    """
    Instalar as dependências (caso ainda não tenha):

No bash instalar:
    pip install pdfplumber PyPDF2
    pip install pandas openpyxl
    pip install openpyxl
    pip install xlsxwriter

    """