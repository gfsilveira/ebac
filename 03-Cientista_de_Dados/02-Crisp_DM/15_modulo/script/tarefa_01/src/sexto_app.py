import streamlit as st
import pandas as pd

def sexto_app() -> None:
    st.title("Mostra uma DataFrame editável")
    
    df = pd.DataFrame(
        [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
    )
    edited_df = st.data_editor(df)

    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

    st.markdown("---")
    return None