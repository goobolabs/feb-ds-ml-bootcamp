## 1. Definition of Machine Learning (with Real-Life Example)

Machine Learning (ML) is a subfield of artificial intelligence in which computer systems learn patterns from data instead of being explicitly programmed with rules. The system is trained on examples so it can make predictions or decisions when presented with new data. ML uses statistical methods to optimize models so they improve performance over time on a given task.

## Real-Life Example:
A practical application of Machine Learning is movie recommendation on streaming platforms such as Netflix or YouTube. The system learns from a user’s past behavior — for example, the movies they watch, like, or skip. By analyzing patterns in this data and comparing them with the behavior of similar users, the ML model can recommend new movies or videos that the user is likely to enjoy. This reduces the time users spend searching for content and improves their overall experience on the platform.

## 2. Supervised vs. Unsupervised Learning
# Supervised Learning

Definition: A type of ML in which the algorithm learns a mapping from input features to output labels using labeled training data — that is, examples where the correct answers are known.

Goal: To predict outcomes for new, unseen data by generalizing from the training examples.

## Example (Real-World):
House price prediction: Given a dataset with characteristics like size, number of bedrooms, and location (inputs) together with known sale prices (outputs), a supervised model (e.g., linear regression or random forest) learns to predict prices for new homes.

# Unsupervised Learning

Definition: A type of ML where the algorithm learns inherent patterns in unlabeled data — data without explicit output labels. Algorithms seek to find structure by identifying clusters, associations, or lower-dimensional representations.

Example (Real-World):
Customer segmentation: A retail company may use unsupervised clustering (e.g., k-means) to divide customers into groups based on purchasing behavior — even though the customers have no predefined labels. The groups can then be used to tailor marketing offers.

Comparison Table


## 3. Overfitting — Causes and Prevention
What Causes Overfitting?

Overfitting occurs when a model fits the training data too closely, including noise or random fluctuations that are not part of the true underlying pattern. As a result, it performs well on training data but poorly on new/unseen data.

Common Causes:

Excessive model complexity: Too many parameters relative to data points.

Insufficient training data: The model learns spurious noise rather than general trends.

Poor validation techniques: Including information from validation/test sets into model training (data leakage).

# How to Prevent Overfitting
Technique	How It Helps
Cross-Validation	Tests model on multiple data splits to avoid overfitting
Regularization (L1/L2)	Penalizes large weights to simplify the model
Early Stopping	Stops training before fitting noise
Data Augmentation	Expands dataset size to reduce noise influence
Simplify Model	Reduces parameters to prevent memorizing noise

Cross-Validation Example: K-fold cross-validation divides data into subsets. The model is trained on several combinations and tested on remaining parts to ensure it generalizes well beyond a single split.

## 4. Training Data and Test Data Splitting
How Are They Split?

In ML workflows, the full dataset is divided into:

Training set: Used to train the model by updating internal parameters.

Test set: Held back from the training process and used only at the end to evaluate generalization.

A typical split might be 70–80% for training and 20–30% for testing, though this varies by dataset size and domain.

# Why Is Splitting Necessary?

Without splitting, you cannot measure how well a model performs on data it has never seen — crucial for evaluating generalization instead of mere memorization. If a model is evaluated only on the data it was trained on, it may appear strong despite failing in real-world use.

Proper splitting guards against inflated performance metrics due to data leakage and ensures the model’s usefulness on new, unseen data.

## 5. Case Study: Machine Learning Applied in Healthcare
Title: Estimating the Incidence of Diabetes Using Machine Learning

Source: PubMed article on public health algorithm development.

Study Overview

Researchers developed a supervised machine learning algorithm to estimate the incidence of diabetes mellitus from health administrative databases in France. The study used a large epidemiological cohort (CONSTANCES) linked to the French National Health Database (SNDS) and applied ML steps including feature selection, model training, and validation.

# Key Findings

A supervised ML model was trained to estimate diabetes incidence using coded variables extracted from reimbursement data (e.g., medical service use).

The final model was validated on a test dataset distinct from the training set — illustrating practical ML splitting and generalization evaluation.

This approach demonstrated the potential of ML to support public health surveillance and disease burden estimation from administrative data.

### References

Supervised & Unsupervised Learning overview — IBM.

Definitions of Machine Learning — Wikipedia; Google ML intro.

Overfitting causes and prevention — IBM & regularization guides.

Data splitting reasoning — ML theory.

Case Study: Diabetes incidence prediction — PubMed.