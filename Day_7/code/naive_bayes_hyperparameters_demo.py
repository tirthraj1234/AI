from sklearn.naive_bayes import GaussianNB, MultinomialNB

gaussian_model = GaussianNB(var_smoothing=1e-9)

multinomial_model = MultinomialNB(
    alpha=1.0,
    fit_prior=True
)

print("Gaussian Model:", gaussian_model)
print("Multinomial Model:", multinomial_model)