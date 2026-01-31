from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

print(f"TensorFlow version: {tf.__version__}")

print("Loading model...")
model = tf.keras.models.load_model("bottle_classifier.h5")
print("Model loaded successfully!")
model.summary()

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        file = request.files["image"]
        img = Image.open(file).convert("RGB").resize((128, 128))
        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        result = model.predict(img)[0][0]

        if result < 0.5:
            prediction = "Bottle 🍼"
        else:
            prediction = "Not a Bottle ❌"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
