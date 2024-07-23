import tensorflow as tf
from tensorflow.keras import backend as K
from tensorflow.keras.utils import register_keras_serializable


smooth = 1e-15

@register_keras_serializable(package='Custom', name='dice_coef')
def dice_coef(y_true,y_pred):
    y_true_flat=tf.keras.layers.Flatten()(y_true)
    y_pred_flat=tf.keras.layers.Flatten()(y_pred)
    intersection=tf.reduce_sum(y_true*y_pred)
    return (2.*intersection+smooth)/(tf.reduce_sum(y_true)+tf.reduce_sum(y_pred)+smooth)

@register_keras_serializable(package='Custom', name='dice_loss')
def dice_loss(y_true,y_pred):
    return 1.0-dice_coef(y_true,y_pred)


@register_keras_serializable(package='Custom', name='iou')
def iou(y_true, y_pred, smooth=1e-5):
    y_pred = tf.cast(y_pred > 0.5, tf.float32)
    
    intersection = K.sum(y_true * y_pred, axis=[1, 2, 3])
    union = K.sum(y_true, axis=[1, 2, 3]) + K.sum(y_pred, axis=[1, 2, 3]) - intersection
    
    iou = (intersection + smooth) / (union + smooth)
    
    return K.mean(iou)