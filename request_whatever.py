from api.completion import generate_txt
from api.replicate_diffusion import download, generate_image

def save_text(prompt, filename):
    response = generate_txt(prompt, 0.9)
    save_path = "results/{}".format(filename)
    
    f = open(save_path, 'w', encoding='utf-8')
    print(response, end = '', file = f)
    f.close()
    
def save_image(prompt, filename):
    save_path = "results/{}".format(filename)
    download(generate_image(prompt), save_path)
    
    

print("If you want to create a text, press t. Or if you want to create an image, press i.")
type = str(input())

if type=="t":
    print("You chose a text. Please write a prompt.")
    prompt = str(input())
    
    print("Write your savepath in a form : yourpath.txt")
    filename = str(input())
    
    save_text(prompt, filename)
    
if type=="i":
    print("You chose an image. Please write a prompt.")
    prompt = str(input())
    
    print("Write your savepath in a form : yourpath.png")
    filename = str(input())
    
    save_image(prompt, filename)