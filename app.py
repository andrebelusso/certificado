import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import uuid
import io

st.set_page_config(page_title="Gerador de Certificados")
st.title("🎓 Gerador de Certificados")
st.markdown("Insira seu nome completo para gerar o certificado:")

nome = st.text_input("Nome completo")

if st.button("Gerar Certificado") and nome:
    fundo = Image.open("certificado_base.jpg").convert("RGB")
    draw = ImageDraw.Draw(fundo)

    fonte_nome = ImageFont.truetype("arial.ttf", 50)
    fonte_rodape = ImageFont.truetype("arial.ttf", 20)

    # Nome centralizado na linha
    draw.text((950, 450), nome, font=fonte_nome, fill="black")

    # Data e serial no rodapé
    data = datetime.now().strftime("%d/%m/%Y")
    serial = str(uuid.uuid4())[:8].upper()
    draw.text((950, 700), f"Data de emissão: {data}", font=fonte_rodape, fill="black")
    draw.text((950, 800), f"ID: {serial}", font=fonte_rodape, fill="black")
   
    buffer = io.BytesIO()
    fundo.save(buffer, format="PNG")
    st.success("✅ Certificado gerado com sucesso!")

    st.download_button(
        label="📥 Baixar Certificado",
        data=buffer.getvalue(),
        file_name="certificado.png",
        mime="image/png"
    )
