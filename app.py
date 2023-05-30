import gradio as gr
import textblob
from textblob.translate import Translator

def text_translate(text, to_language):
    translate = Translator()

    to_language = to_language.lower()
    if to_language == 'yoruba':
        to_lang_ = 'yo'
    elif to_language == 'hausa':
        to_lang_ = 'ha'
    elif to_language == 'igbo':
        to_lang_ = 'ig'    

    translation_ = translate.translate(str(text), from_lang='en', to_lang=to_lang_)
    return str(translation_)

languages_ = ['Yoruba', 'Hausa', 'Igbo']
with gr.Blocks() as demo:
    text_ = gr.Textbox(label = 'Input text', placeholder = 'Input text to be translated')
    lang_to_translate_to = gr.Textbox(label = 'Language to translate to', placeholder='Input Language to translate to')
    output = gr.Textbox(label = 'Message')
    btn = gr.Button('Translate Text')
    btn.click(fn = text_translate, inputs = [text_, lang_to_translate_to], outputs = output)

demo.launch(share = True)