import tensorflow as tf

train_ds = tf.keras.utils.image_dataset_from_directory(
    "data/Train", image_size=(224, 224), batch_size=8
)
val_ds = tf.keras.utils.image_dataset_from_directory(
    "data/Validation", image_size=(224, 224), batch_size=8
)

print("Train classes:", len(train_ds.class_names))
print("Val classes:  ", len(val_ds.class_names))
print("Same order:", train_ds.class_names == val_ds.class_names)
print("First 5:", train_ds.class_names[:5])

for images, labels in train_ds.take(1):
    print("Train batch:", images.shape, labels.numpy())
for images, labels in val_ds.take(1):
    print("Val batch:  ", images.shape, labels.numpy())