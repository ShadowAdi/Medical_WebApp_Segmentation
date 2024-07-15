import tensorflow as tf
from utils.Loss import dice_loss,iou,dice_coef
import numpy as np


def get_chest_model(input_image):
    model= tf.keras.models.load_model("./model/chest_model.keras", custom_objects={'dice_loss': dice_loss, 'iou': iou, 'dice_coef': dice_coef})
    prediction= model.predict(input_image)
    return (prediction > 0.5).astype(np.uint8) * 255


def get_skin_model(input_image):
    model= tf.keras.models.load_model("./model/skin_cancer_segmentation.keras", custom_objects={'dice_loss': dice_loss, 'iou': iou, 'dice_coef': dice_coef})
    prediction= model.predict(input_image)
    return (prediction > 0.5).astype(np.uint8) * 255

