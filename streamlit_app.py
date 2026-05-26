# import streamlit as st

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st
import numpy as np
from PIL import Image
from ai_edge_litert.interpreter import Interpreter

st.title("Pengelompokkan Jenis Makanan")

st.divider()
st.header("Area untuk Mengunggah Gambar")
uploaded_image = st.file_uploader("Upload gambar...", type=["jpg", "jpeg", "png"])

class_names = ['chicken_curry', 'chicken_wings', 'fried_rice',
    'grilled_salmon', 'hamburger', 'ice_cream', 'pizza', 'ramen',
    'steak', 'sushi']

# @st.cache_resource
# def load_model():
#     interpreter = Interpreter(model_path="src/model.tflite")
#     return interpreter

# interpreter = load_model()
# interpreter.allocate_tensors()

# input_details = interpreter.get_input_details()
# output_details = interpreter.get_output_details()

# input_shape = input_details[0]['shape']

if uploaded_image is not None:
    image = Image.open(uploaded_image).convert("RGB")
#     resized_img = image.resize((224,224))
#     img_array = np.array(resized_img, dtype=np.float32)
#     input_data = np.expand_dims(img_array, axis=0)

#     interpreter.set_tensor(input_details[0]['index'], input_data)
#     interpreter.invoke()
#     output_data = interpreter.get_tensor(output_details[0]['index'])
#     pred_class = class_names[output_data.argmax()]
   
    st.divider()
    st.header("Area Menampilkan Hasil")
#     st.subheader(pred_class)
    st.image(image, width='stretch')
