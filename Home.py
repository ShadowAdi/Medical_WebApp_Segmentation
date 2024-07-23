import streamlit as st


st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)


st.header("Hello Users")
st.subheader("It is a Medical Image Segmentation Project")

st.text("This Is A Multipurpose project create to solve many medical related task for you.")

st.divider()

st.subheader("Chest Segmentation")

st.write("The model I created is a Chest Segmentation Project.")
st.write("You will provide an image of your chest, and it will convert it into the segmented image and return it to you.")
st.markdown("I created the model using Kaggle. [Kaggle](https://www.kaggle.com/datasets/newra008/chest-segmentation-image)")
st.markdown("I Created UNET Model from scracth and trained my model on the dataset.")
st.image("Images\Chest_Segmentation_Image_and_Mask.png","Mask_And_Normal_Image",width=500)
st.markdown("The Dataset They Provide us Contain Two Types of Images Normal One And There Segmented Image or Mask Version. The Normal Images are in grayscale format and Mask Images are either full black or white.")
st.markdown("We Also did preprocessing on our Normal And Mask Images. Like Converting our Image To Grayscale and then resizing it to a size of 256,256 and Dividing by 255 so images can range between 0 to 1")
st.markdown("We Will set A Batch size of 32 and we will run for 30 epochs with a learning rate of 1e-3 because we are going to use Adam As Optimizer")
st.markdown("We are going to judge our model results on following metrics. Accuracy,iou(Image Over Union) and dice_coef and our loss is goin to be dice_loss. Basically dice_loss is actually a negative of dice_coef")
st.markdown("If we talk about UNET. It really is a great model which contains Two Part. A Downsampling Part And An UpSampling Part. And It also Contains Spin Connections. We Are Going To Downsample our Image by MaxPooling Layer And We Can Do UpSampling By Conv2DTranspose Layer")
st.markdown("The Accuracy Score For Training Image is 94% and dice coefficient is 0.96 and iou is 0.91")
st.image("Images\segmented_image.png","Mask Image",width=500)



st.divider()

st.subheader("Skin Cancer Segmentation")

st.write("The model I created is a Skin Cancer Segmentation Project.")
st.write("You will provide an image of Skin Cancer, and it will convert it into the segmented image and return it to you.")
st.markdown("I created the model using Kaggle. [Kaggle](https://www.kaggle.com/datasets/surajghuwalewala/ham1000-segmentation-and-classification)")
st.markdown("I Created UNET Model from scracth and trained my model on the dataset.")
st.markdown("The Dataset They Provide us Contain Two Types of Images Normal One And There Segmented Image or Mask Version. The Normal Images are in grayscale format and Mask Images are either full black or white.")
st.markdown("We Also did preprocessing on our Normal And Mask Images. Like Converting our Image To Grayscale and then resizing it to a size of 256,256 and Dividing by 255 so images can range between 0 to 1")
st.markdown("We Will set A Batch size of 32 and we will run for 30 epochs with a learning rate of 1e-3 because we are going to use Adam As Optimizer")
st.markdown("We are going to judge our model results on following metrics. Accuracy,iou(Image Over Union) and dice_coef and our loss is goin to be dice_loss. Basically dice_loss is actually a negative of dice_coef")
st.markdown("If we talk about UNET. It really is a great model which contains Two Part. A Downsampling Part And An UpSampling Part. And It also Contains Spin Connections. We Are Going To Downsample our Image by MaxPooling Layer And We Can Do UpSampling By Conv2DTranspose Layer")
st.image("Images\skin_cancer_mask_and_image.jpg","Mask Image",width=500)
st.image("Images\Skin_Cancer_Mask_Image.jpg","Mask Image",width=500)
st.image("Images\skin_cancer_results.jpg","Mask Image",width=500)

st.divider()

st.header("MediBot")
st.markdown("I Created a Medical Bot for you. So you can chat with it so you can get information related to HealthCare")

