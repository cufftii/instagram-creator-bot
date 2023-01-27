from diffusers import StableDiffusionPipeline

def generate_image(prompt, save_path):
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
    )

    image = pipe(prompt).images[0]
    image.save("results/"+save_path)