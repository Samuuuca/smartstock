import pytesseract
from PIL import Image

# Caminho para o executável do Tesseract (se necessário)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\CS3 Recepção\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'  # No Windows, ajuste o caminho

# Abrir a imagem
imagem = Image.open(r'C:\Users\CS3 Recepção\Documents\Samuel\StockSmart\Model\img\nota_fiscal.png')

# Extrair texto usando o Tesseract
texto = pytesseract.image_to_string(imagem)

# Se necessário, decodificar o texto
try:
    textoencoded = texto.encode('utf-8')
    print(textoencoded)

    with open("Output.txt", "w") as text_file:
        text_file.write(texto)
except UnicodeDecodeError:
    texto = texto.encode('latin-1')  # Ou outro encoding apropriado