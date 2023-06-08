# Menggunakan image Python sebagai dasar
FROM python:3.8-slim-buster

# Mengatur working directory di dalam container
WORKDIR /app

# Menyalin dependencies ke dalam container
COPY requirements.txt .

# Menginstal dependencies yang dibutuhkan
RUN pip3 install --no-cache-dir -r requirements.txt

# Menyalin kode aplikasi ke dalam container
COPY . .

EXPOSE 8080

# Menjalankan aplikasi saat container dijalankan
CMD [ "python3", "app.py" ]
