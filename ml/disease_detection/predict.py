import sys
import json
import numpy as np
import tensorflow as tf
from PIL import Image

MODEL_PATH = "models/crop_disease_model.h5"
CLASS_NAMES_PATH = "models/class_names.json"

model = tf.keras.models.load_model(MODEL_PATH, compile=False)
with open(CLASS_NAMES_PATH) as f:
    class_names = json.load(f)

def predict(image_path):
    img = Image.open(image_path).convert("RGB").resize((224, 224))
    arr = np.array(img, dtype=np.float32)
    arr = np.expand_dims(arr, axis=0)
    preds = model.predict(arr, verbose=0)[0]
    idx = int(np.argmax(preds))
    return {
        "disease": class_names[idx],
        "confidence": float(preds[idx]),
        "all_scores": {class_names[i]: float(preds[i]) for i in range(len(class_names))},
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict.py <image_path>")
        sys.exit(1)
    result = predict(sys.argv[1])
    print(json.dumps(result, indent=2))