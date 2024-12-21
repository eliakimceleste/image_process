import numpy as np

def recadrage(image: np.ndarray, a:int = None, b:int = None):
  img = image.copy()
  if (a is not None and b is not None):
    img_recadre = (img - np.min(img)) * ((b - a) / (np.max(img) - np.min(img))) + a
    img_recadre = np.round(img_recadre).astype(np.uint8)
    return img_recadre
  else:
    img_recadre = (img - np.min(img))*(255/(np.max(img) - np.min(img)))
    img_recadre = np.round(img_recadre).astype(np.uint8)
    return img_recadre