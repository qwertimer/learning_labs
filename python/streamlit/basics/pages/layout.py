import streamlit as st




def show_house():
    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")
        middle_column.image(f"{chosen}.jpg")



left_column, middle_column, right_column = st.columns(3)
left_column.button('Start', on_click = show_house)
