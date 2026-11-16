
def generate_story_plan(title, genre, duration):
    minutes = int(duration.split()[0])
    scene_count = minutes * 3

    scenes = []

    for i in range(1, scene_count + 1):
        scenes.append({
            "scene": i,
            "title": f"{title} - Scene {i}",
            "genre": genre,
            "description": (
                f"Scene {i} of a {genre} "
                f"3D animated movie about {title}."
            ),
            "visual_style": "High-quality 3D cartoon animation",
            "duration_seconds": 20
        })

    return scenes


if __name__ == "__main__":
    result = generate_story_plan(
        "The Magical Cat",
        "Adventure",
        "5 Minutes"
    )

    for scene in result:
        print(scene)
