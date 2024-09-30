import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2

# Load model
model = tf.keras.models.load_model("model_first.h5")

def labeling(image, label):
    df = pd.DataFrame()
    df["image"] = [image]
    df["label"] = [label]
    return df

def feature_engineering(df):
    images = []
    for index, row in df.iterrows():
        uploaded_file = row["image"]
        file_buffer = uploaded_file.getbuffer()
        file_bytes = np.asarray(bytearray(file_buffer), dtype=np.uint8)

        if file_bytes.size > 0:
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            if img is not None:
                img = cv2.resize(img, (64, 64))
                img = img.astype(np.uint8)
                img = img / 255.0
                img = (img * 255).astype(np.uint8)
                if len(img.shape) == 2:
                    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
                else:
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                images.append(img)
            else:
                print(f"Gagal memuat gambar: {uploaded_file}")
                dummy_img = np.zeros((64, 64, 3), dtype=np.uint8)
                images.append(dummy_img)
        else:
            print(f"Gagal membaca file: {uploaded_file}")
            dummy_img = np.zeros((64, 64, 3), dtype=np.uint8)
            images.append(dummy_img)

    df["image"] = images
    return df

def predict_and_display(df):
    images = df['image']
    images = [np.array(img) for img in images]  # Convert lists to numpy arrays
    images = np.array(images)  # Convert list of numpy arrays to a single numpy array
    images_tensor = tf.convert_to_tensor(images, dtype=tf.uint8)
    predictions = model.predict(images_tensor)
    st.write('Hasil prediksi:')
    labels = ['Auto Rickshaws/ Bajaj', 'Bikes', 'Cars', 'Motorcycles', 'Planes', 'Ships', 'Trains']
    for i, prediction in enumerate(predictions):
        predicted_label = np.argmax(prediction)
        st.write(f'Predicted label: {labels[predicted_label]}')

def run():
    st.title("Prediksi Transportasi")
    st.sidebar.title("About This Page")
    st.sidebar.write("""
**Klasifikasi Gambar Kendaraan dengan Neural Network untuk Optimasi Rute**

Teknologi *neural network*, sebuah cabang dari kecerdasan buatan (AI), memiliki kemampuan luar biasa dalam mengidentifikasi objek dalam gambar. Dalam konteks pengiriman, *neural network* dapat digunakan untuk mengklasifikasikan jenis kendaraan (mobil, motor, truk, dll.) dari gambar.

Dengan informasi ini, sistem optimasi rute dapat:

* **Memilih rute optimal:** Menentukan rute tercepat dan paling efisien berdasarkan jenis kendaraan, kondisi lalu lintas, dan lokasi pengiriman.
* **Mengelola armada:** Mengalokasikan kendaraan yang tepat untuk setiap pengiriman, meminimalkan biaya operasional.
* **Meningkatkan efisiensi:** Mengurangi waktu pengiriman, konsumsi bahan bakar, dan biaya operasional secara keseluruhan.

**Contoh:** Jika sistem mendeteksi bahwa sebagian besar pengiriman hari ini memerlukan kendaraan roda dua, maka sistem akan memprioritaskan rute yang sesuai dengan karakteristik motor, seperti jalan yang lebih sempit atau jalur khusus kendaraan roda dua.

**Manfaat Utama:**

* **Efisiensi:** Pengiriman lebih cepat, biaya operasional lebih rendah.
* **Akurasi:** Pengambilan keputusan berdasarkan data yang akurat dan real-time.
* **Fleksibilitas:** Sistem dapat dengan mudah disesuaikan dengan berbagai jenis kendaraan dan kondisi lalu lintas.
* **Skalabilitas:** Dapat diterapkan pada berbagai skala bisnis, mulai dari UMKM hingga perusahaan logistik besar.
""")

    # Create a section for image upload
    st.write("## Upload an Image")
    with st.form(key="data"):
        image = st.file_uploader("Select an image", type=["jpg", "png"])
        if image is not None:
            image_bytes = image.read()
            st.image(image_bytes, caption=image.name, use_column_width=True)
        submit = st.form_submit_button("Predict")

    if submit:
        # Create a section for prediction results
        st.write("## Prediction Results")

        data = labeling(image, "unknown")
        data = feature_engineering(data)
        predict_and_display(data)

if __name__ == "__main__":
    run()