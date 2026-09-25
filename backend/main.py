import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import json
import numpy as np
import tensorflow as tf
from PIL import Image

# Paths — relative to backend/ folder
MODEL_PATH = "../ml/disease_detection/models/crop_disease_model.keras"
CLASSES_PATH = "../ml/disease_detection/models/class_names.json"

app = FastAPI(title="Crop Disease Detection API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

if not os.path.exists(MODEL_PATH):
    raise RuntimeError(
        f"Model not found at {MODEL_PATH}. "
        "Train the model first: cd ml/disease_detection && python train.py"
    )

print(f"TensorFlow version: {tf.__version__}")
print("Loading model (legacy Keras mode)...")
model = tf.keras.models.load_model(MODEL_PATH, compile=False)
class_names = json.load(open(CLASSES_PATH))
print(f"Model loaded. {len(class_names)} classes.")

@app.get("/health")
def health():
    return {"status": "ok", "classes": len(class_names)}

@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    if image is None:
        raise HTTPException(status_code=400, detail="no image provided")
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(await image.read())
            tmp_path = tmp.name

        img = Image.open(tmp_path).convert("RGB").resize((224, 224))
        arr = np.expand_dims(np.array(img, dtype=np.float32), 0)

        preds = model.predict(arr, verbose=0)[0]
        idx = int(np.argmax(preds))
        conf = float(preds[idx])

        os.unlink(tmp_path)

        return {
            "disease": class_names[idx],
            "confidence": conf,
            "low_confidence": conf < 0.7,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"prediction failed: {str(e)}")