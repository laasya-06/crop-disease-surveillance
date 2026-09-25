import json
import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix

VAL_DIR = "data/Validation"

model = tf.keras.models.load_model("models/crop_disease_model.h5", compile=False)
with open("models/class_names.json") as f:
    class_names = json.load(f)

val_ds = tf.keras.utils.image_dataset_from_directory(
    VAL_DIR, image_size=(224, 224), batch_size=32, shuffle=False
)

y_true, y_pred = [], []
for images, labels in val_ds:
    preds = model.predict(images, verbose=0)
    y_true.extend(labels.numpy())
    y_pred.extend(np.argmax(preds, axis=1))

print(classification_report(y_true, y_pred, target_names=class_names))
print("\nConfusion matrix rows=true, cols=predicted:")
print("Classes:", class_names)
print(confusion_matrix(y_true, y_pred))