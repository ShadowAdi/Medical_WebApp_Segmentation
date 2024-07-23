import streamlit as st
from PIL import Image
from utils.Download_Image import download_image
from utils.Image_Augmentation import skin_segmentation
from utils.getModelChestSegmentation import get_skin_model



st.set_page_config(
    page_title="Skin Cancer Segmentation",
    page_icon="😷",
)





st.write("The model I created solves Skin Cancer  Segmentation Problem. It will Help Identify Skin Cancer Related probelms")
st.write("You will provide an image of your Skin, and it will convert it into the segmented image and return it to you.")

    

img=st.file_uploader("Upload an image of Skin", type=["png", "jpg", "jpeg"])



if img is not None:
    input_image=skin_segmentation(img)
    prediction=get_skin_model(input_image=input_image)
    try:
        predicted_image = Image.fromarray(prediction.squeeze(), mode='L')
        img_bytes=download_image(predicted_image=predicted_image)

        st.image(img, caption="Original Image", use_column_width=True)
        st.image(input_image, caption="Image Augmented Image", use_column_width=True)
        st.image(prediction.squeeze(), caption="Segmented Image", use_column_width=True)

        st.download_button(
            label="Download Segmented Image",
            data=img_bytes,
            file_name="segmented_image.png",
            mime="image/png"
        )
    except:
        st.error(prediction)






