import streamlit as st
import pandas as pd

def quarto_app() -> None:
    st.title("DataFrame com botão de expanção")

    # Cache the dataframe so it's only loaded once
    @st.cache_data
    def load_data():
        return pd.DataFrame(
            {
                "first column": [1, 2, 3, 4],
                "second column": [10, 20, 30, 40],
            }
        )

    # Boolean to resize the dataframe, stored as a session state variable
    st.checkbox("Use container width", value=False, key="use_container_width")

    df = load_data()

    # Display the dataframe and allow the user to stretch the dataframe
    # across the full width of the container, based on the checkbox value
    st.dataframe(df, use_container_width=st.session_state.use_container_width)
    st.markdown("---")
    return None