from PIL import Image
import numpy as np

def chest_segmentation(image):
    IMG_H, IMG_W = 256, 256  # Replace with your model's input dimensions
    image = Image.open(image).convert('L')  # Convert to grayscale
    image = image.resize((IMG_H, IMG_W))
    image = np.array(image, dtype=np.float32) / 255.0  # Normalize to [0, 1]
    image = np.expand_dims(image, axis=-1)  # Add channel dimension
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image


def skin_segmentation(image):
    IMG_H, IMG_W = 256, 256  # Replace with your model's input dimensions
    image = Image.open(image).convert('RGB')  # Convert to RGB
    image = image.resize((IMG_H, IMG_W))
    image = np.array(image, dtype=np.float32) / 255.0  # Normalize to [0, 1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image


def polyp_segmentation(image_path):
    IMG_H, IMG_W = 256, 256  # Replace with your model's input dimensions
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    image = image.resize((IMG_H, IMG_W))
    image = np.array(image, dtype=np.float32) / 255.0  # Normalize to [0, 1]
    image = np.expand_dims(image, axis=-1)  # Add channel dimension
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image