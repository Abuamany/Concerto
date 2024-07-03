import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
import os

# Judul aplikasi
st.title("PDF to JPG Converter")

# Fungsi untuk menyimpan gambar

# Gabungkan dua halaman menjadi satu gambar
def show_image(pages):
    widths, heights = zip(*(i.size for i in pages))
    total_width = max(widths)
    total_height = sum(heights)

    new_image = Image.new('RGB', (total_width, total_height))

    y_offset = 0
    for page in pages:
        new_image.paste(page, (0, y_offset))
        y_offset += page.size[1]
    
    # Tampilkan gambar di Streamlit
    st.image(new_image, caption='Combined Image', use_column_width=True)

# Unggah file PDF
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Simpan file PDF yang diunggah ke disk
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Tampilkan tombol untuk mengonversi PDF
    if st.button("Convert PDF to JPG"):
        pages = convert_from_path('temp.pdf', first_page=1, last_page=2)
        save_image(pages)
        st.write("Conversion done!")
