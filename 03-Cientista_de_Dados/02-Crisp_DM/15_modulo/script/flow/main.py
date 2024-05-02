import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def definie_data(mean: int, std: int) -> np.array:
    data_array = np.random.normal(loc=mean, scale=std, size=100_000)

    return data_array

if __name__ == "__main__":

    data = {
        "1": definie_data(mean=100, std=1),
        "2": definie_data(mean=150, std=100),
    }

    df = pd.DataFrame(data)

    plt.figure(figsize=(10,10))
    sns.jointplot(
        x="1",
        y="2",
        kind="reg",
        data=df,
    )
    st.pyplot(fig=plt)

    st.markdown("---")