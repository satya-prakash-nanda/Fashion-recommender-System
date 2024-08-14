import streamlit as st
import os
from PIL import Image
import numpy as np
import pickle
from annoy import AnnoyIndex
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from numpy.linalg import norm

# Load the precomputed features and filenames
feature_list = np.array(pickle.load(open('embeddings.pkl', 'rb')))
filenames = pickle.load(open('filenames.pkl', 'rb'))

# Initialize the model
model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model.trainable = False

model = tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])

st.title('Fashion Recommender System')


def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('uploads', uploaded_file.name), 'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1
    except:
        return 0


def feature_extraction(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    result = model.predict(preprocessed_img).flatten()
    normalized_result = result / norm(result)

    return normalized_result


def build_annoy_index(feature_list, num_trees=10):
    # Assuming feature_list is a 2D array with shape (num_samples, num_features)
    f = feature_list.shape[1]
    annoy_index = AnnoyIndex(f, metric='euclidean')

    for i in range(len(feature_list)):
        annoy_index.add_item(i, feature_list[i])

    annoy_index.build(num_trees)
    return annoy_index


def recommend_annoy(features, annoy_index, num_neighbors=5):
    indices = annoy_index.get_nns_by_vector(features, num_neighbors)
    return indices


# Build the Annoy index
annoy_index = build_annoy_index(feature_list)

# File upload and recommendation steps
uploaded_file = st.file_uploader("Choose an image")
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        # Display the uploaded file
        display_image = Image.open(uploaded_file)
        st.image(display_image)
        # Feature extraction
        features = feature_extraction(os.path.join("uploads", uploaded_file.name), model)
        # Recommendation using Annoy
        indices = recommend_annoy(features, annoy_index)
        # Display recommendations
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.image(filenames[indices[0]])
        with col2:
            st.image(filenames[indices[1]])
        with col3:
            st.image(filenames[indices[2]])
        with col4:
            st.image(filenames[indices[3]])
        with col5:
            st.image(filenames[indices[4]])
    else:
        st.header("Some error occurred in file upload")
