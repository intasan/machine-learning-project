from pathlib import Path
import cv2
import numpy as np

DATASET = Path('dataset')


def preprocess_image(path: str) -> np.ndarray:
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(path)
    image = cv2.resize(image, (224, 224))
    return image.astype(np.float32) / 255.0


def load_images(root: Path):
    images, labels = [], []
    if not root.exists():
        return np.empty((0, 224, 224, 3), dtype=np.float32), np.empty((0,), dtype=str)
    for label_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        for image_path in label_dir.glob('*'):
            try:
                images.append(preprocess_image(str(image_path)))
                labels.append(label_dir.name)
            except (OSError, ValueError):
                continue
    return np.asarray(images), np.asarray(labels)


if __name__ == '__main__':
    X, y = load_images(DATASET)
    print('samples:', len(X))
    print('classes:', sorted(set(y.tolist())))
