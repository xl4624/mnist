import numpy as np
import matplotlib.pyplot as plt

def show_image(pixels: np.ndarray) -> None:
    plt.imshow(pixels, cmap='gray')
    plt.show()