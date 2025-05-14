import os
import pdfplumber
import re
from PyPDF2 import PdfWriter, PdfReader

# Caminho onde estão seus arquivos PDF
pasta_pdf = "caminho/pata/base/arquivos.pdf"  # Ajuste esse caminho

# Expressão regular ajustada para capturar o nome com "Sr." ou "Sra." e o "(a)"
# Agora captura nomes com abreviações como "C.", "Jr." e outros sobrenomes completos
padrao_nome = re.compile(r"(Sr\.|Sra\.)\s*\(?a?\)?\s*([\wÀ-ÿ\s\.]+(?:\s+[A-Za-zÀ-ÿ\s\.]+)*)", re.IGNORECASE)

# Função para extrair o nome até a referência "Ref.:"
def extrair_nome_ate_ref(texto):
    # Limpa o texto, removendo quebras de linha e espaços extras
    texto_limpo = " ".join(texto.split())
    
    # Buscando o texto até a palavra "Ref.:"
    texto_ate_ref = texto_limpo.split("Ref.:")[0]
    
    # Agora, buscamos o nome após "Dr." ou "Dra." no texto extraído
    match = padrao_nome.search(texto_ate_ref)
    if match:
        return match.group(2).strip()  # Retorna o nome completo encontrado (grupo 2)
    return None

# Função para salvar cada página separadamente
def salvar_paginas_separadas(caminho_pdf, pasta_saida):
    try:
        with pdfplumber.open(caminho_pdf) as pdf:  # Abre o PDF
            pdf_reader = PdfReader(caminho_pdf)  # Leitura do PDF com PyPDF2
            for i, pagina in enumerate(pdf.pages):  # Processa cada página
                texto = pagina.extract_text()  # Extrai o texto da página
                if texto:  # Se houver texto na página
                    nome_extraido = extrair_nome_ate_ref(texto)  # Extrai o nome da página
                    if nome_extraido:
                        # Remover caracteres especiais e espaços extras no nome
                        nome_final = re.sub(r'[^\w\s\.]', '', nome_extraido).strip()  # Remove caracteres não alfanuméricos
                        nome_final = nome_final.replace(" ", "_")  # Substitui espaços por underscores

                        # Renomeia o arquivo com base no nome extraído
                        novo_nome = f"{nome_final}.pdf"
                        caminho_novo = os.path.join(pasta_saida, novo_nome)

                        # Cria um novo PDF com a página extraída
                        pdf_writer = PdfWriter()
                        pdf_writer.add_page(pdf_reader.pages[i])

                        # Salva a página extraída como um novo arquivo PDF
                        with open(caminho_novo, "wb") as output_pdf:
                            pdf_writer.write(output_pdf)

                        print(f"Página {i+1} renomeada e salva como: {novo_nome}")
                    else:
                        print(f"Nome não encontrado para a página {i+1} do arquivo {caminho_pdf}")
    except Exception as e:
        print(f"Erro ao processar {caminho_pdf}: {e}")

# Pasta para salvar os arquivos de saída
pasta_saida = "caminho/pata/base/arquivosSaidapdf/nomes_saida111"  # Ajuste esse caminho

# Verifica e cria a pasta de saída, se não existir
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Percorrer todos os arquivos na pasta
for arquivo in os.listdir(pasta_pdf):
    if arquivo.lower().endswith(".pdf"):  # Verifica se é um PDF
        caminho_antigo = os.path.join(pasta_pdf, arquivo)
        
        # Salva as páginas separadas com novo nome
        salvar_paginas_separadas(caminho_antigo, pasta_saida)

print("Processo concluído.")