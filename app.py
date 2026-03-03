import gradio as gr
import os

# আপনার HTML ফাইলটি পড়ার কোড
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Gradio এর মাধ্যমে HTML টি দেখানো
with gr.Blocks() as demo:
    gr.HTML(html_content)

demo.launch()

