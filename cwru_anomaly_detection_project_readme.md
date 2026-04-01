# 🚀 Proyecto: Detección de Anomalías en Vibración (CWRU + Autoencoder)

## 🎯 Objetivo
Desarrollar un sistema de detección de anomalías en equipos industriales utilizando datos de vibración del dataset CWRU (Case Western Reserve University) y modelos de Autoencoder.

El sistema deberá ser capaz de:
- Aprender el comportamiento normal de un equipo
- Detectar desviaciones (fallas)
- Generar un score de anomalía

---

## 🧠 Enfoque
Se utilizará un enfoque de *unsupervised learning*:
- Entrenamiento solo con datos normales
- Detección de anomalías mediante error de reconstrucción

---

## 📂 Dataset
Fuente: CWRU Bearing Dataset

Contiene:
- Señales de vibración
- Condiciones normales y de falla
- Diferentes tipos de defectos en rodamientos

---

## 🏗️ Arquitectura del Proyecto

```
data → windowing → feature engineering → scaling → autoencoder → anomaly score → threshold → evaluación
```

---

## 📌 Fases del Proyecto

### Fase 1: Carga y comprensión de datos
- [ ] Descargar dataset (Hugging Face / Oficial)
- [ ] Explorar estructura de archivos
- [ ] Identificar señales normales vs fallas

### Fase 2: Preprocesamiento
- [ ] Segmentación en ventanas
- [ ] Normalización de señal

### Fase 3: Feature Engineering
- [ ] RMS
- [ ] Kurtosis
- [ ] Skewness
- [ ] Peak-to-peak
- [ ] Crest factor
- [ ] Energía
- [ ] FFT dominante

### Fase 4: Dataset final
- [ ] Construir DataFrame (features)
- [ ] Crear etiquetas (normal vs anomalía)

### Fase 5: Modelado
- [ ] Escalado (StandardScaler)
- [ ] Autoencoder (Dense)
- [ ] Entrenamiento con datos normales

### Fase 6: Detección de anomalías
- [ ] Reconstruction error
- [ ] Definir threshold

### Fase 7: Evaluación
- [ ] ROC Curve
- [ ] Confusion Matrix
- [ ] Precision / Recall

### Fase 8: Visualización
- [ ] Distribución de errores
- [ ] Score por ventana

### Fase 9: Deploy (opcional)
- [ ] Dashboard con Streamlit
- [ ] Simulación en tiempo real

---

## ⚙️ Stack Tecnológico
- Python
- Pandas / Numpy
- Scikit-learn
- TensorFlow / PyTorch
- Matplotlib / Seaborn
- Streamlit (opcional)

---

## 📊 Resultado Esperado
Un sistema capaz de:
- Detectar anomalías en vibración
- Diferenciar comportamiento normal vs falla
- Ser escalable a casos reales industriales

---

## 🧩 Próximo Paso
👉 Implementar carga del dataset CWRU y explorar su estructura

