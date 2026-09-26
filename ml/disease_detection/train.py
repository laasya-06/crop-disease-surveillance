import json
import tensorflow as tf
from preprocess import load_datasets, IMG_SIZE

TRAIN_DIR = "data/Train"
VAL_DIR = "data/Validation"
MODEL_PATH = "models/crop_disease_model.keras"
EPOCHS = 15

train_ds, val_ds = load_datasets(TRAIN_DIR, VAL_DIR)
class_names = train_ds.class_names
print(f"Classes ({len(class_names)}): {class_names}")

# --- Augmentation (training only) ---
augment = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.1),
    tf.keras.layers.RandomZoom(0.1),
])

# --- Base model ---
base = tf.keras.applications.MobileNetV2(
    input_shape=(*IMG_SIZE, 3),
    include_top=False,
    weights="imagenet",
)
base.trainable = False

# --- Full model ---
inputs = tf.keras.Input(shape=(*IMG_SIZE, 3))
x = augment(inputs)
x = tf.keras.layers.Rescaling(1./127.5, offset=-1)(x)
x = base(x, training=False)
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dropout(0.3)(x)
outputs = tf.keras.layers.Dense(len(class_names), activation="softmax")(x)

model = tf.keras.Model(inputs, outputs)

model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-3),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

# --- Callbacks ---
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor="val_loss", patience=4, restore_best_weights=True
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss", factor=0.5, patience=2, min_lr=1e-6
    ),
]

train_ds = train_ds.prefetch(tf.data.AUTOTUNE)
val_ds = val_ds.prefetch(tf.data.AUTOTUNE)

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS,
    callbacks=callbacks,
)

model.save(MODEL_PATH)
with open("models/class_names.json", "w") as f:
    json.dump(class_names, f)

print(f"Saved to {MODEL_PATH}")