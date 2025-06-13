import fitz  # PyMuPDF

pdf_path = "app/documents/Livro-do-Desassossego-.pdf"
txt_path = "app/documents/personagem.txt"

with fitz.open(pdf_path) as doc:
    full_text = ""
    for page in doc:
        full_text += page.get_text()

with open(txt_path, "w", encoding="utf-8") as f:
    f.write(full_text)

print("✅ Texto extraído e salvo como personagem.txt")
