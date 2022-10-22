from tika import parser

raw = parser.from_file('bibliotecas/tika/texto_pdf.pdf')
print(raw["metadata"])
print(raw["content"])