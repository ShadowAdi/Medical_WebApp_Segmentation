from io import BytesIO
def download_image(predicted_image):
    buffered = BytesIO()
    predicted_image.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    return img_bytes

