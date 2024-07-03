import streamlit as st
from pdf2image import convert_from_path
from PIL import Image

st.title("Konversi PDF ke Gambar")

# Unggah file PDF
uploaded_file = st.file_uploader("Unggah file PDF", type="pdf")

if uploaded_file is not None:
    # Simpan file PDF yang diunggah
    with open("uploaded_pdf.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Konversi dua halaman pertama dari PDF ke gambar
    pages = convert_from_path("uploaded_pdf.pdf", first_page=1, last_page=2)

    # Tampilkan gambar di aplikasi
    st.subheader("Hasil Konversi:")
    for i, page in enumerate(pages):
        st.image(page, caption=f'Halaman {i+1}')

    # Berikan opsi untuk mengunduh gambar
    #for i, page in enumerate(pages):
    #    page.save(f'page_{i+1}.png')
    #    with open(f'page_{i+1}.png', 'rb') as file:
    #        btn = st.download_button(
    #            label=f"Unduh Gambar Halaman {i+1}",
    #            data=file,
    #            file_name=f'page_{i+1}.png',
    #            mime="image/png"
    #        )
