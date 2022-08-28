import streamlit as st


def main():
    """
    Simple slider with a key to show the ability to access key,
    change length of slider with shown here 1000.
    """
    x = st.slider('x', 1000, key = "square")  #Widget , second value is length of widget.
    st.write(x, 'squared is', x*x)
    st.write(st.session_state.square)

if __name__ =="__main__":
    main()
