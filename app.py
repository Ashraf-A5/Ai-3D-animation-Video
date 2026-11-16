
import gradio as gr

def create_story(title, genre, duration):
    return f"""
# {title}

Genre: {genre}
Duration: {duration}

Your AI Animation Studio is ready!
"""

with gr.Blocks(title="AI 3D Animation Studio") as demo:
    gr.Markdown("# 🎬 AI 3D Animation Studio")
    gr.Markdown("Create your own animated movie!")

    title = gr.Textbox(label="Story Title")

    genre = gr.Dropdown(
        ["Adventure", "Comedy", "Fantasy", "Friendship"],
        label="Animation Genre"
    )

    duration = gr.Dropdown(
        ["5 Minutes", "7 Minutes", "10 Minutes"],
        label="Video Duration"
    )

    output = gr.Markdown()

    button = gr.Button("Generate Story")
    button.click(
        create_story,
        inputs=[title, genre, duration],
        outputs=output
    )

demo.launch()

