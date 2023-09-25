import os

def allowed_file(filename):
    ALLOWED_FILE = {'png', 'jpg', 'jpeg'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE

def get_image():
    image_folder = "static"
    image_path = os.path.join(image_folder,"no-image.png")
    for file in os.listdir(image_folder): 
        if file[0] == "1":
            image_path = os.path.join(image_folder,file)
    return image_path 

def delete_cache(): 
    for file in os.listdir("static"): 
        if file == "styles" or file == "no-image.png" or file == "arsitektur.png":
            continue
        os.remove(os.path.join("static",file))