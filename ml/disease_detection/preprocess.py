import tensorflow as tf

IMG_SIZE = (224, 224)
BATCH_SIZE = 32

def load_datasets(train_dir, val_dir):
    train_ds = tf.keras.utils.image_dataset_from_directory(
        train_dir,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        seed=42,
    )
    val_ds = tf.keras.utils.image_dataset_from_directory(
        val_dir,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        seed=42,
    )
    return train_ds, val_ds