
import gradio as gr
from story import generate_story_plan

def create_story(title, genre, duration):
    if not title.strip():
        return "Please enter a story title."

    scenes = generate_story_plan(title, genre, duration)

    result = f"# 🎬 {title}\n\n"
    result += f"Genre: {genre}\n\n"

    for scene in scenes:
        result += f"## Scene {scene['scene']}\n"
        result += f"**{scene['title']}**\n\n"
        result += f"{scene['description']}\n\n"
        result += f"Visual: {scene['visual_style']}\n\n"
        result += "---\n\n"

    return result

with gr.Blocks(title="AI 3D Animation Studio") as demo:
    gr.Markdown("# 🎬 AI 3D Animation Studio")
    gr.Markdown("Plan your animated movie!")

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

    button = gr.Button("Generate Scene Plan")
    button.click(
        create_story,
        inputs=[title, genre, duration],
        outputs=output
    )

demo.launch()

