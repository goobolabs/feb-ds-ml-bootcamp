# Assignment one machine learning

**NAME:** ABDISHAKUUR ALI DAAHIR

---

## 1. What is machine learning?

Machine learning is a subset of artificial intelligence (AI) that enables computers to learn from data and make predictions or decisions without being explicitly programmed for every specific task.

**Examples:**
- Facial recognition
- Product recommendation
- Financial accuracy

---

## 2. compare supervised learning and un supervised learning give an example each other?

In supervised learning, the algorithm is trained on a labeled dataset, meaning each input is paired with the corresponding correct output. The algorithm learns a mapping function from the input to the output, allowing it to predict labels for new, unseen data.

**Example:**  
Email Spam Detection

Unsupervised learning works with unlabeled data, meaning the algorithm is given raw data and must find structures, patterns, or relationships on its own. There is no "answer key" to guide the training.

**Examples:**  
Customer Segmentation

---

## 3. what causes overfitting? how can it be prevent?

Overfitting primarily occurs due to an imbalance between model complexity and the available data. Key causes include:

- Excessive Model Complexity: The model has too many parameters, layers, or nodes (high capacity) relative to the amount of information in the data, allowing it to "memorize" the training set.
- Small Training Dataset: If the dataset is too small, the model fails to find general patterns and instead maps to specific, non-generalizable data points.
- Noisy Data/Outliers: The presence of incorrect, irrelevant, or inconsistent data points ("noise") leads the model to learn these anomalies as true, underlying patterns.

Preventing overfitting involves increasing the model's ability to generalize to new data. Key strategies include:

- Increase Training Data: Providing more data points helps the model better distinguish between true patterns and random noise.
- Data Augmentation: Artificially expanding the dataset by creating variations of existing data (e.g., rotating, flipping, or zooming in image processing).
- Regularization Techniques:
  - L1 Regularization (LASSO): Penalizes model complexity by driving irrelevant feature weights to zero, effectively performing feature selection.
  - L2 Regularization (Ridge): Reduces the magnitude of all weights, preventing any single feature from having too much influence.
  - Dropout (for Neural Networks): Randomly "turns off" neurons during training to prevent the network from relying on specific, narrow pathways.

---

## 4. explain how training data and test data are split , and why this process is necessary?

Training data and test data are typically split using a process called cross-validation to evaluate a machine learning model's performance on unseen data. This process is necessary to ensure the model generalizes well to new, real-world examples rather than simply memorizing the data it was trained on.

### How the Data is Split?

The most common method for splitting data is a straightforward division, typically into a training set and a testing set.

- Training Set: This portion of the data (often 70-80% of the total dataset) is used to fit and train the machine learning model. The model learns patterns and relationships from this data.
- Test Set: This remaining portion (typically 20-30%) is held back and used only after the model has been fully trained. It acts as an independent benchmark to evaluate the model's performance on data it has never seen before.

### Why This Process is Necessary?

The primary reason for splitting data is to prevent a phenomenon known as overfitting and to provide an unbiased evaluation of the model's true performance.

- Preventing Overfitting: Overfitting occurs when a model becomes too complex and learns the specific noise and random fluctuations in the training data, rather than the general, underlying patterns.
- Unbiased Evaluation: By using a separate, unseen test set, data scientists can get a reliable estimate of how well the model is likely to perform in real-world scenarios.
- Model Selection and Tuning: The split data allows for the comparison of different models or the tuning of a single model's hyperparameters. The test set provides an objective way to choose the best-performing model.

---

## 5. find one case study (research paper or Titile) that explain how machine learning has been applied in health care, buisness, or transportation, summarize and its findings?

### Case study health care:

This research focused on using machine learning (ML) to improve patient retention in HIV care—a major challenge in many low-resource countries (like in parts of Africa). Patients who stop attending HIV treatment appointments (“loss to follow-up” or LTFU) are less likely to stay healthy and more likely to spread the virus.

The study used routine electronic health records (EMRs) of 3,720 adult HIV-positive patients from urban health facilities in Ethiopia. Six different ML algorithms were tested to see which one best predicts whether a patient will miss future clinic visits.
