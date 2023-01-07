import cohere
co = cohere.Client('ABzZ8IBzGxi8n5t7ZfqdCuU99kxlsChGKCyuDpXd')
def write_post(topic):
  response = co.generate(
  model='command-xlarge-20221108',
  prompt=f'Create a Blogpost with Table of contents for \"{topic}":',
  max_tokens=400,
  temperature=0.9,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[],
  return_likelihoods='NONE')
  return (response.generations[0].text)

import gradio as gr

with gr.Blocks() as demo:
  gr.Markdown("# AI generated Blogpost with Cohere API")
  #with gr.Row():
  gr.Image(shape=(100, 100),type='C:/Users/md/Downloads/My project (2).jpg')
  #inp=gr.Number(0)
  inp =gr.Textbox(placeholder='Type a word or words you want to generate after',label="Topic")
  btn =gr.Button("Generate ")
  out=gr.Textbox()
  btn.click(fn=write_post, inputs=inp,outputs=out)
demo.launch(share=True)

