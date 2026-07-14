from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

gaussian_model = GaussianNB()
multinomial_model = MultinomialNB()
bernoulli_model = BernoulliNB()

print("Gaussian Naive Bayes:", gaussian_model)
print("Multinomial Naive Bayes:", multinomial_model)
print("Bernoulli Naive Bayes:", bernoulli_model)