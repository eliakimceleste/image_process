import numpy as np
from image_process.histogram import histogramme

def egalisation(image:np.ndarray):
  img = image.copy()
  hist, hist_cumul = histogramme(img)
  NF = len(hist_cumul)/2 # Calcul du nombre d'intensité de l'image égalisée
  P = (img.shape[0] * img.shape[1]) / NF #proportion de pixels par pixel
  sum = 0
  bandes = []
  bande = []
  i = 0
  for pixel in sorted(hist.keys()):
    if len(hist) == i:
      bandes.append(bande)
    if sum < NF:
      sum += hist[pixel]
      bande.append(pixel)
      i += 1
    else:
      bandes.append(bande)
      bande = []
      sum = 0
      sum += hist[pixel]
      bande.append(pixel)
      i += 1
  for i in bandes:
    i = np.array(i)
    img[np.isin(img, i)] = round(np.mean(i))

  return img