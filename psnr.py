from math import log10, sqrt
import cv2
import numpy as np

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return "Infinite"
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

def main():
    original = cv2.imread("original.jpeg")
    compressed = cv2.imread("saved_eccv16.png", 1)

    if original is None or compressed is None:
        print("Error: Failed to load image files.")
    else:
        # Resize images to the same dimensions
        original = cv2.resize(original, (1055, 1390))
        compressed = cv2.resize(compressed, (1055, 1390))

        value = PSNR(original, compressed)
        print(f"PSNR value is {value} dB")

if __name__ == "__main__":
    main()

