import streamlit as st

def app():
    st.markdown('<style>h1 { color: Tomato; }</style>', unsafe_allow_html=True)
    st.balloons()
    left_column, right_column = st.columns(2)
    with left_column:
        st.title('Member')
        st.markdown(
        """<p style="font-size:20px;">
            ↪ Trịnh Đình Phú 👉 Leader <br>
            ↪ Vũ Đức Hiệu 👉 Data <br>
            ↪ Phạm Hùng 👉 Model <br>
            ↪ Nguyễn Hữu Trung Kiên 👉 UI
            </p>
        """, unsafe_allow_html=True)
        st.title('Contact us!:envelope_with_arrow:')
        st.markdown('''### GitHub: [Kien](https://github.com/kieenddaay)''')
    with right_column:
        st.image('https://media3.giphy.com/media/D7BfZIMFLE3DR8Koyg/200.webp?cid=790b7611k0cze5nbt3du5ofofsoxdz9bund2j78k75j8ld1n&ep=v1_stickers_search&rid=200.webp&ct=ts')
        st.image('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExazBjemU1bmJ0M2R1NW9mb2Zzb3hkejlidW5kMmo3OGs3NWo4bGQxbiZlcD12MV9zdGlja2Vyc19zZWFyY2gmY3Q9cw/3ohzdGmM14QTUne9tm/giphy.webp')