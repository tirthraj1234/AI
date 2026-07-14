# Example of Laplace Smoothing

word_count = 0
total_words = 100
vocabulary_size = 50

probability = (word_count + 1) / (total_words + vocabulary_size)

print("Smoothed Probability:", probability)