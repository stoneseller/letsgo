import streamlit as st
import drawing.ipynb as draw


st.set_option('deprecation.showfileUploaderEncoding', False) # deprecation 표시 안함
st.write("made by. 임기택")
st.title("제발 되라")

draw

def inference(text):
    image = draw(text, 1).squeeze()
    return image

demo = st.title(fn=inference, inputs="text", outputs="image")

demo.launch(debug=True)