# Renomeando_arquivos_pdf_xlsx
Renomeando arquivos .pdf e .xlsx, Usando Regex para capturar partes especificas do arquivo para seu usado para salvar como nome do arquivo em .pdf ou .xlsx

# 📂 Extrair Nomes e Separar Arquivos PDF e XLSX

Este projeto contém dois scripts Python para separar arquivos PDF e XLSX em novos arquivos individuais com base em nomes extraídos automaticamente.

---

## ✅ Pré-requisitos

Instale as bibliotecas necessárias com:

```bash
pip install pdfplumber PyPDF2 pandas openpyxl
```

---

## 📘 Script para PDF

### Objetivo:

Extrair o nome de cada página de um arquivo PDF e salvar cada página como um novo arquivo com o nome correspondente.

### Como configurar:

- Ajuste o caminho da pasta com os arquivos PDF na variável `pasta_pdf`.
- Ajuste a pasta onde deseja salvar os PDFs separados em `pasta_saida`.

### Padrão de nomes:

O script localiza nomes que começam com "Sr." ou "Sra." até a expressão "Ref.:", usando expressão regular. O padrão pode ser alterado na variável `padrao_nome`.

### Como executar:

```bash
python pdf_split_por_nome.py
```

---

## 📗 Script para XLSX

### Objetivo:

Dividir um arquivo Excel (.xlsx) em vários arquivos, baseando-se nos nomes contidos em uma coluna específica.

### Como configurar:

- Informe o caminho do arquivo `.xlsx`.
- Informe o nome da coluna usada para dividir os arquivos (ex: `"Nome"`).
- Defina a pasta onde os arquivos serão salvos.

### Como executar:

```bash
python xlsx_split_por_coluna.py
```

---

## 📁 Resultado Esperado

Os arquivos separados e renomeados serão salvos em uma pasta de saída:

```
saida/
├── Maria_Silva.pdf
├── João_Souza.pdf
├── Ana_Lima.xlsx
```

---

## 📌 Observações

- Certifique-se de que os arquivos de entrada estejam no formato correto.
- O script trata nomes com espaços e caracteres especiais, substituindo por `_`.

---

## 📬 Contato

Fique à vontade para entrar em contato para sugestões ou dúvidas.
