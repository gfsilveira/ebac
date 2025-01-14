import streamlit as st


def inicia() -> None:
    st.markdown("Entrada")
    uploaded_files = st.file_uploader("Choose a CSV file")
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)


if __name__ == "__main__":
    inicia()
