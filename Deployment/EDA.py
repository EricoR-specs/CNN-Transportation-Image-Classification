import streamlit as st

def run():
    st.title('Transportation Klassifications System')
    st.sidebar.title('About this page')
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
    st.image('https://promova.com/content/transportation_vocabulary_09188cbada.png')

    # Create a dictionary to store vehicle classes and their characteristics
    vehicle_classes = {
        'Kelas Bajaj': {
            'image': 'Visualization\Auto Rickshaw (752).jpg',
            'characteristics': [
                'Memiliki 2-3 roda',
                'Memiliki ukuran yang kecil dibandingkan dengan mobil',
                'Tidak memiliki pintu.',
                'Memiliki desain yang cenderung sama.'
            ]
        },
        'Kelas Mobil': {
            'image': 'Visualization\cybertruck.jpg',
            'characteristics': [
                'Memiliki roda 2 hingga 4.',
                'Memiliki pintu.',
                'Memiliki desain yang berbeda-beda, cenderung body.'
            ]
        },
        'Kelas Motor': {
            'image': 'Visualization\Yamaha Niken.jpg',
            'characteristics': [
                'Memiliki 2 roda.',
                'Memiliki roda yang tebal namun tidak lebar seperti sepeda.',
                'Memiliki body yang menutupi rangka.',
                'Memiliki desain yang berbeda-beda tergantung body.'
            ]
        },
        'Kelas Sepeda': {
            'image': 'Visualization\Bike (720).jpg',
            'characteristics': [
                'Memiliki 2 roda.',
                'Memiliki Roda yang lebar.',
                'Memiliki rangka yang terlihat.',
                'Memiliki desain yang cenderung sama.'
            ]
        },
        'Kelas Kereta': {
            'image': 'Visualization\Whoosh.jpg',
            'characteristics': [
                'Memiliki bentuk yang pipih dan memanjang',
                'Memiliki background daratan.'
            ]
        },
        'Kelas Pesawat': {
            'image': 'Visualization\Plane (66).jpg',
            'characteristics': [
                'Terlihat memiliki sayap yang lebar.',
                'Memiliki ukuran besar.',
                'Untuk beberapa pesawat memiliki kecenderungan posisi sayap yang sama.'
            ]
        },
        'Kelas Kapal': {
            'image': 'Visualization\Ship (593).jpg',
            'characteristics': [
                'Memiliki lambung yang terlihat',
                'Kebanyakan memiliki background air.'
            ]
        }
    }

    # Loop through the vehicle classes and display images and characteristics
    for vehicle_class, info in vehicle_classes.items():
        st.subheader(vehicle_class)
        st.write("")  # Add a blank line for spacing
        col1, col2 = st.columns([1, 3])  # Create two columns
        with col2:  # Center the image in the second column
            st.image(info['image'], caption='Visualisasi Data Transportasi', width=400)
        st.write("")  # Add a blank line for spacing
        st.write('Berdasarkan gambar di atas, karakteristik {} adalah:'.format(vehicle_class))
        for characteristic in info['characteristics']:
            st.write('- {}'.format(characteristic))
        st.write("")  # Add a blank line for spacing

if __name__ == '__main__':
    run()