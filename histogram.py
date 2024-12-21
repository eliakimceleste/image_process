import numpy as np
import matplotlib.pyplot as plt
import cv2

def histogramme(image: np.ndarray, nvi:int = None):
  #Copier l'image d'entrée
  img = image.copy()
  if nvi is not None:
    pass
  else:
    unique_pixel, number_pixel = np.unique(img, return_counts=True) #R2cupérer toutes les valeurs uniues des pixels et leurs occurrences
    hist_amplitude = dict(zip(unique_pixel, number_pixel)) # Créer un dictionnaire pour l'histogramme d'amplitude à partir des pixels et nombre d'occurence

  cumulative_sum = 0
  cumulative_histogramme = {}
  for key in sorted(hist_amplitude.keys()):
    cumulative_sum +=  hist_amplitude[key]
    cumulative_histogramme[key] = cumulative_sum
  return hist_amplitude, cumulative_histogramme
