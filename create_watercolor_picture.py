from api.keras_cv_diffusion import generate_image
#from api.replicate_diffusion import generate_image, download

f = open("results/daily_post.txt",'r', encoding="utf-8")
daily_post = f.readlines()
f.close()

generate_image("In watercolor : "+str(daily_post), "post_image.png")

'''
image_url = generate_image("In watercolor : "+str(daily_post))
save_path = "results/post_image.png"
download(image_url, save_path)
'''