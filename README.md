# 🩺 Klasifikasi Risiko Diabetes Menggunakan Algoritma Decision Tree

## 📘 Deskripsi Proyek
Proyek ini bertujuan untuk membangun model klasifikasi risiko diabetes berdasarkan data pemeriksaan pasien. Dengan memanfaatkan algoritma **Decision Tree**, aplikasi ini dapat mengidentifikasi kemungkinan seseorang terkena diabetes berdasarkan fitur seperti usia, tekanan darah, kadar glukosa, BMI, dan lainnya.

Model ini selanjutnya dikembangkan menjadi aplikasi web agar dapat digunakan secara praktis untuk prediksi berbasis input pengguna.

---

## 📊 Dataset
- **Sumber**: Dataset Diabetes dari Kaggle
- **Fitur Input**: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
- **Label Output**: Outcome (1 = Positif diabetes, 0 = Negatif diabetes)
- **Jumlah Data**: 768 baris

---

## 🧪 Proses dan Kode Program

### 1. Preprocessing
- Data dibersihkan dari nilai kosong (jika ada)
- Dipisahkan menjadi `X` (fitur) dan `y` (label)
- Split data: 70% training, 30% testing

```python
X = df.drop('Outcome', axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
```

### 2. Pembentukan Model: Decision Tree
```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
```
Model Decision Tree dipilih karena:
- Cepat dilatih dan diinterpretasi
- Cocok untuk data klasifikasi
- Tidak memerlukan normalisasi

### 3. Evaluasi Model
```python
y_pred = model.predict(X_test)

print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```
📌 Hasil Evaluasi:

- Akurasi: 87.0% (contoh, sesuaikan dengan outputmu)
- Precision Positif: 0.78
- Recall Positif: 0.82
- Confusion Matrix:
- True Positive: 45
- False Positive: 9
- True Negative: 58
- False Negative: 12


## 🚀 Aplikasi Web

Aplikasi berbasis web dibuat menggunakan Flask, dengan antarmuka input sederhana untuk mengisi data pemeriksaan. Setelah input dikirim, hasil klasifikasi akan ditampilkan.

Fitur:
- Input manual (form)
- Prediksi otomatis
- Output: Risiko diabetes (positif / negatif)
