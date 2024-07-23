import tensorflow as tf
from utils.Loss import dice_loss,iou,dice_coef
import numpy as np


def get_chest_model(input_image):
    if os.path.isfile("model\chest_model.keras"):
        return "The issue is With Git LFS. Chest Model.keras Size it too big so maybe it extended the free tier for LFS Package. Sorry for the issue"
    try:
        model= tf.keras.models.load_model("model\chest_model.keras", custom_objects={'dice_loss': dice_loss, 'iou': iou, 'dice_coef': dice_coef})
        prediction= model.predict(input_image)
        return (prediction > 0.5).astype(np.uint8) * 255
    except:
        return "The issue is With Git LFS. Skin Cancer Model.keras Size it too big so maybe it extended the free tier for LFS Package. Sorry for the issue"



def get_skin_model(input_image):
    if os.path.isfile("model\skin_cancer_segmentation.keras"):
        return "The issue is With Git LFS. Skin Cancer Model.keras Size it too big so maybe it extended the free tier for LFS Package. Sorry for the issue"
    try:
        model= tf.keras.models.load_model("model\skin_cancer_segmentation.keras", custom_objects={'dice_loss': dice_loss, 'iou': iou, 'dice_coef': dice_coef})
        prediction= model.predict(input_image)
        return (prediction > 0.5).astype(np.uint8) * 255
    except:
        return "The issue is With Git LFS. Skin Cancer Model.keras Size it too big so maybe it extended the free tier for LFS Package. Sorry for the issue"

