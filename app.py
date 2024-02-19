import streamlit as st
def main():
    st.title("PLANT DESEASES")
    uploaded_file=st.file_uploader("choose an image",type=["jpg","jpeg","png"])
    if uploaded_file is not None:
        st.image(uploaded_file,caption="uploaded image",use_column_width=True)
    button_clicked=st.button("Continue")
main()    


