import numpy as np #type:ignore
import matplotlib.pyplot as plt #type:ignore -for plotting training history
import tensorflow as tf # type:ignore  -building and training deep learning model
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # type:ignore -Augmenting images for training
from tensorflow.keras.models import Sequential  # type:ignore -Linear sack of neural network layers
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout  # type:ignore -Convolutional layers for feature extraction
from tensorflow.keras.optimizers import Adam  # type:ignore -Optimizer for training
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping  # type:ignore -Callbacks for saving and early stopping

#setting random seed for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

#defining constant values
IMAGE_SIZE = (256, 256)  # Input image size - all imagaes will be having this size
BATCH_SIZE = 32 # THese are the recommended number of images that can be processed in one batch
EPOCHS = 20  # Number of full passes (epochs) to train the model
NUM_CLASSES = 2  # Number of classes for crop disease detection (Healthy vs Diseased)
ANIMAL_CLASSES = 3  # Number of classes for animal filtering (Dog, Cat, Human)

#defining dataset directory and model path
DATASET_DIR = "dataset"  # Directory containing the dataset
MODEL_PATH = "agric_model.h5"  # Path to save the trained model

def create_model(input_shape, num_classes):
    """Create a CNN model for classification"""
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(256, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dropout(0.5),
        Dense(512, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer=Adam(learning_rate=0.0001),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def train_crop_model():
    """Train the main crop disease detection model"""
    # Data generators with augmentation
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest',
        validation_split=0.2
    )

    # Load datasets
    train_generator = train_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "crops"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training'
    )

    validation_generator = train_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "crops"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation'
    )

    # Create and train model
    model = create_model(IMAGE_SIZE + (3,), NUM_CLASSES)

    callbacks = [
        ModelCheckpoint(MODEL_PATH, save_best_only=True),
        EarlyStopping(patience=5, restore_best_weights=True)
    ]

    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // BATCH_SIZE,
        epochs=EPOCHS,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // BATCH_SIZE,
        callbacks=callbacks
    )

    # Plot training history
    plot_training_history(history)
    return model


def train_animal_filter():
    """Train a secondary model to filter out animals/humans"""
    animal_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

    train_generator = animal_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "animals"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training'
    )

    validation_generator = animal_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "animals"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation'
    )

    model = create_model(IMAGE_SIZE + (3,), ANIMAL_CLASSES)

    model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // BATCH_SIZE,
        epochs=10,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // BATCH_SIZE
    )

    return model


def plot_training_history(history):
    """Plot training and validation accuracy/loss"""
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(len(acc))

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')

    plt.savefig('training_history.png')
    plt.close()


def predict_image(model, animal_model, image_path):
    """Predict if image is healthy/diseased crop or animal/human"""
    img = tf.keras.preprocessing.image.load_img(
        image_path, target_size=IMAGE_SIZE
    )
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # First check if it's an animal/human
    animal_pred = animal_model.predict(img_array)
    animal_classes = ['dog', 'cat', 'human']
    animal_prob = np.max(animal_pred)

    if animal_prob > 0.9:  # High confidence it's an animal/human
        return {
            'type': 'animal',
            'class': animal_classes[np.argmax(animal_pred)],
            'confidence': float(animal_prob)
        }

    # If not animal, check for crops
    crop_pred = model.predict(img_array)
    crop_classes = ['healthy', 'diseased']
    return {
        'type': 'crop',
        'class': crop_classes[np.argmax(crop_pred)],
        'confidence': float(np.max(crop_pred))
    }


if __name__ == "__main__":
    # Train or load models
    if not os.path.exists(MODEL_PATH):
        print("Training crop disease model...")
        crop_model = train_crop_model()
        print("Training animal filter model...")
        animal_model = train_animal_filter()
    else:
        print("Loading existing models...")
        crop_model = tf.keras.models.load_model(MODEL_PATH)
        animal_model = create_model(IMAGE_SIZE + (3,), ANIMAL_CLASSES)
        # Note: In production, you should save/load the animal model too

    # Test prediction
    test_image = "test_image.jpg"  # Replace with your test image
    if os.path.exists(test_image):
        prediction = predict_image(crop_model, animal_model, test_image)
        print("\nPrediction Results:")
        print(f"Type: {prediction['type']}")
        print(f"Class: {prediction['class']}")
        print(f"Confidence: {prediction['confidence']:.2%}")
    else:
        print(f"Test image {test_image} not found")
