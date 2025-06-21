import unittest
import numpy as np
import matplotlib.pyplot as plt

# function for grayscale to RGB conversion
def grayscale_to_rgb(image):
    return np.stack((image, image, image), axis=-1)

class TestGrayscaleToRGB(unittest.TestCase):
    
    def test_grayscale_to_rgb(self):
        gray_image = np.array([[0.5, 0.3, 0.2], [0.4, 0.1, 0.6], [0.8, 0.7, 0.9]])
        expected_rgb_image = np.array([[[0.5, 0.5, 0.5], [0.3, 0.3, 0.3], [0.2, 0.2, 0.2]],
                                       [[0.4, 0.4, 0.4], [0.1, 0.1, 0.1], [0.6, 0.6, 0.6]],
                                       [[0.8, 0.8, 0.8], [0.7, 0.7, 0.7], [0.9, 0.9, 0.9]]])
        rgb_image = grayscale_to_rgb(gray_image)
        
        # plot the grayscale and RGB images side by side
        fig, axs = plt.subplots(1, 2)
        axs[0].imshow(gray_image, cmap='gray')
        axs[0].set_title('Grayscale Image')
        axs[1].imshow(rgb_image)
        axs[1].set_title('RGB Image')
        plt.show()
        
        self.assertEqual(rgb_image.shape, (3, 3, 3))
        self.assertTrue(np.allclose(rgb_image, expected_rgb_image, rtol=1e-03, atol=1e-03))

    def test_grayscale_to_rgb_full_black(self):
        gray_image = np.zeros((3, 3))
        expected_rgb_image = np.zeros((3, 3, 3))
        rgb_image = grayscale_to_rgb(gray_image)
        
        # plot the grayscale and RGB images side by side
        fig, axs = plt.subplots(1, 2)
        axs[0].imshow(gray_image, cmap='gray')
        axs[0].set_title('Grayscale Image')
        axs[1].imshow(rgb_image)
        axs[1].set_title('RGB Image')
        plt.show()
        
        self.assertEqual(rgb_image.shape, (3, 3, 3))
        self.assertTrue(np.allclose(rgb_image, expected_rgb_image, rtol=1e-03, atol=1e-03))


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

