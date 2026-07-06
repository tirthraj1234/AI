# NumPy Notes

## Day 1 – NumPy Fundamentals

### What is NumPy?

NumPy (Numerical Python) is a Python library used for numerical computing. It provides support for fast and efficient operations on arrays, matrices, and mathematical functions. NumPy is one of the most important libraries in Data Science, Machine Learning, and Artificial Intelligence.

---

### Why is NumPy Used?

NumPy is used because it:

- Performs mathematical calculations quickly.
- Stores data efficiently using arrays.
- Supports matrix operations.
- Provides many built-in mathematical and statistical functions.
- Is the foundation of libraries like Pandas, Scikit-learn, TensorFlow, and PyTorch.

---

### What is an Array?

An array is a collection of elements of the same data type stored together in memory. NumPy arrays are faster and more memory-efficient than Python lists.

Example:

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])
```

---

### What are Indexing and Slicing?

#### Indexing

Indexing is used to access a specific element in an array using its position.

Example:

```python
numbers[0]
numbers[2]
numbers[-1]
```

Output:

```
10
30
50
```

---

#### Slicing

Slicing is used to access a range of elements from an array.

Example:

```python
numbers[1:4]
```

Output:

```
[20 30 40]
```

---

### NumPy Functions Used Today

The following NumPy functions and attributes were used:

- `np.array()` – Create a NumPy array.
- `shape` – Returns the shape of the array.
- `ndim` – Returns the number of dimensions.
- `size` – Returns the total number of elements.
- `dtype` – Returns the data type of the array.
- `reshape()` – Changes the shape of the array.
- `np.mean()` – Calculates the average value.
- `np.sum()` – Calculates the total sum.
- `np.max()` – Finds the maximum value.
- `np.min()` – Finds the minimum value.

---

### Mathematical Operations Performed

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)

These operations are performed element by element on NumPy arrays.

---

### Advantages of NumPy

- Fast execution
- Memory efficient
- Easy mathematical operations
- Supports multi-dimensional arrays
- Widely used in Machine Learning and Data Science

---

### Real-World Applications

- Data Analysis
- Machine Learning
- Artificial Intelligence
- Image Processing
- Scientific Computing
- Financial Analysis
- Data Visualization

---

## Key Learnings

Today I learned:

- What NumPy is and why it is important.
- How to create and use NumPy arrays.
- How to access elements using indexing.
- How to extract data using slicing.
- How to perform mathematical operations on arrays.
- How to calculate mean, sum, minimum, and maximum values.
- How to reshape arrays for different data structures.

---

## Conclusion

NumPy is a powerful Python library for numerical computing. It makes mathematical calculations faster and more efficient than Python lists. It is the foundation of many Machine Learning and Data Science libraries, making it an essential tool for AI development.