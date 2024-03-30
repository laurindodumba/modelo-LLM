import streamlit as st

# Injeta o CSS do Bootstrap ou estilos personalizados
def inject_bootstrap():
    bootstrap_link = """
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    """
    st.markdown(bootstrap_link, unsafe_allow_html=True)

def create_footer():
    footer_html = """
        <div class="footer">
        <hr style="border-top: 1px solid #bbb;">
        <p style="text-align: center; font-size: 14px;">© 2024 Sua Empresa - Todos os direitos reservados</p>
        </div>
        """
    st.markdown(footer_html, unsafe_allow_html=True)

# Configurações da página
st.set_page_config(page_title="Aplicação Web - LLM ", layout="wide")

# Injeta Bootstrap CSS
inject_bootstrap()

# Seleção de páginas
page = st.sidebar.selectbox("Navegação", ["HOME", "SERVIÇOS", "INSIGHTS", "CONFIGURAÇÃO"])

if page == "HOME":
    st.title("APLICAÇÃO WEB - LLM")
    st.image(r"C:\Users\Eduardo\Documents\Laurindo\modelo LLM\Capturar.PNG")  # Substitua pelo caminho real da imagem
    create_footer()

elif page == "SERVIÇOS":
    st.title("SERVIÇOS")
    # Conteúdo da página secundária 1
    st.write("Conteúdo da Página Secundária 1.")
    create_footer()

elif page == "INSIGHTS":
    st.title("INSIGHTS")
    # Conteúdo da página secundária 2
    st.write("Conteúdo da Página Secundária 2.")
    create_footer()

elif page == "CONFIGURAÇÃO":
    st.title("CONFIGURAÇÃO")
    st.write("parametros de configuração da API")
    create_footer()