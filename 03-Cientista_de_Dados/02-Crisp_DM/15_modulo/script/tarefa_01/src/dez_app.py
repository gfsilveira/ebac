import streamlit as st

def dez_app() -> None:
    st.title("Mostra um JSON")
    
    st.json({
        'foo': 'bar',
        'baz': 'boz',
        'stuff': [
            'stuff 1',
            'stuff 2',
            'stuff 3',
            'stuff 5',
        ],
    })
    st.markdown("---")
    return None