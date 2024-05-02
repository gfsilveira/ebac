import streamlit as st
import pandas as pd
import numpy as np

def quinto_app() -> None:
    st.title("DataFrame completa com gráfico ao final")
    
    
    df1 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

    my_table = st.table(df1)

    df2 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

    my_table.add_rows(df2)
    # Now the table shown in the Streamlit app contains the data for
    # df1 followed by the data for df2.

    # Assuming df1 and df2 from the example above still exist...
    my_chart = st.line_chart(df1)
    my_chart.add_rows(df2)
    # Now the chart shown in the Streamlit app contains the data for
    # df1 followed by the data for df2.
    
    st.markdown("---")
    return None