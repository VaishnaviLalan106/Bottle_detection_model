# 🍾 Bottle Detection AI

A sleek, modern web application powered by **TensorFlow** and **Flask** that identifies bottles in images with high precision.

## 🌟 Features

- **Real-time AI Inference**: Uses a pre-trained Keras model (`.h5`) for instant bottle detection.
- **Glassmorphic UI**: Beautiful, premium interface with blur effects, gradients, and micro-animations.
- **Responsive Design**: Works perfectly on mobile, tablet, and desktop browsers.
- **Robust Error Handling**: Optimized image preprocessing (128x128 RGB conversion) to ensure model compatibility.

## 🛠️ Built With

- **Python 3.11** - Core logic
- **Flask** - Web framework
- **TensorFlow / Keras** - Deep Learning model
- **NumPy & Pillow** - Image processing and numerical computing
- **HTML5 & Vanilla CSS** - Modern, responsive front-end

## 🚀 Getting Started

### Prerequisites

- Python 3.11 (Recommended)
- Virtual Environment tool (`venv`)

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/VaishnaviLalan106/Bottle_detection_model.git
   cd Bottle_detection_model
   ```

2. **Initialize and Activate Virtual Environment**
   ```powershell
   # Create environment
   python -m venv en

   # Activate (Windows)
   en\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install flask tensorflow==2.15.0 "numpy<2.0.0" Pillow
   ```

4. **Run the Application**
   ```bash
   python app.py or
   en\Scripts\python app.py
   ```

5. **Access the App**
   Open your browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```text
├── app.py                   # Flask Application Engine
├── bottle_classifier.h5     # Trained Keras Model (Large File)
├── templates/
│   └── index.html           # Glassmorphic Front-end
└── en/                      # Virtual Environment
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the model accuracy or the UI design.

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---
Developed with ❤️ by [Vaishnavi Lalan](https://github.com/VaishnaviLalan106)
