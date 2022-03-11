import matplotlib.pyplot as plt
import numpy as np
import cv2
from tqdm import tqdm


def show_galaxies(gal_ids, n_gal=25, n_row=5, n_col=5):
    """Fonction qui affiche des galaxies sélectionnées au hasard
    parmi une liste d'id de galaxie"""
    selected = np.random.choice(gal_ids, n_gal, replace=False)
    plt.figure(figsize=(16,16))
    for i in range(n_gal):
        plt.subplot(n_row,n_col,i+1)
        img = cv2.imread(f"data/images_training_rev1/{selected[i]}.jpg")
        plt.imshow(img)
        plt.title(f"Id={selected[i]}", fontsize='small')

        
        
shape_in =  (424,424)
crop =      (256,256)
shape_out = (64,64)
    
def get_crop_resize_images(df, shape_out=shape_out, crop=crop):
    """Fonction qui importe, taille et redimensionne les images
    à partir des fichiers jpg"""
    x_start = (shape_in[0] - crop[0])//2
    y_start = (shape_in[1] - crop[1])//2
    
    x_end = x_start + crop[0]
    y_end = y_start + crop[1]
   
    val = df.values
    ids = val[:,0].astype(int).astype(str)
    y = val[:,1:]
    X = []
    
    for i in tqdm(ids):
        x = cv2.imread(f'data/images_training_rev1/{i}.jpg')
        x = x[x_start:x_end, y_start:y_end]
        x = cv2.resize(x, shape_out)
        x = x/255.
        X.append(x)        
    X = np.array(X)
    return X, y