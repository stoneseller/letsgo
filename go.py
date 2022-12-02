import streamlit as st
import drawing.ipynb as draw


st.set_option('deprecation.showfileUploaderEncoding', False) # deprecation 표시 안함
st.write("made by. 임기택")
st.title("제발 되라")


import gradio as gr

def inference(text):
    image = draw(text, 1).squeeze()
    return image

demo = gr.Interface(fn=inference, inputs="text", outputs="image")

demo.launch(debug=True)
