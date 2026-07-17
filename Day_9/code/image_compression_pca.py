import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.decomposition import PCA

# Load image
img = mpimg.imread("Day_9/dataset/grayscale_image.png")

# Convert RGB to Grayscale if needed
if len(img.shape) == 3:
    img = img.mean(axis=2)

print("Original Shape:", img.shape)

# Apply PCA
pca = PCA(n_components=50)

compressed = pca.fit_transform(img)
reconstructed = pca.inverse_transform(compressed)

print("Compressed Shape:", compressed.shape)
print("Explained Variance:", sum(pca.explained_variance_ratio_))

# Display Original Image
plt.figure(figsize=(6,6))
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")
plt.show()

# Display Compressed Image
plt.figure(figsize=(6,6))
plt.imshow(reconstructed, cmap="gray")
plt.title("Compressed Image using PCA")
plt.axis("off")
plt.show()