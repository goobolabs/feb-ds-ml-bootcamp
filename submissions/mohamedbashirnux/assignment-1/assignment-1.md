# Research Assignment: Introduction to Machine Learning

**Student:** Mohamed Bashir  
**Date:** February 5, 2026

---

## 1. Define Machine Learning using a real-life example

Machine Learning is a subset of artificial intelligence where algorithms learn patterns from data and make predictions without being explicitly programmed. Instead of following fixed rules, ML models improve through experience by adjusting their parameters during training. The goal is generalization—performing well on new, unseen data.

**Real-Life Example: Email Spam Detection**

Email spam filters use machine learning to automatically identify spam. Instead of programmers writing rules for every spam type, the system learns from thousands of labeled emails ("spam" or "not spam"). It identifies patterns like suspicious words, sender addresses, or formatting. Once trained, it accurately classifies new emails without human intervention, adapting as spam tactics evolve.

---

## 2. Compare Supervised Learning and Unsupervised Learning, giving an example of each

**Supervised Learning** uses labeled data where each input has a correct output. The algorithm learns to map inputs to outputs by studying these examples. During training, it makes predictions, calculates errors, and adjusts to improve accuracy.

**Example:** Medical diagnosis systems learn from patient data (symptoms, test results) labeled with confirmed diagnoses. The model learns which symptoms indicate which diseases, then predicts diagnoses for new patients.

**Unsupervised Learning** works with unlabeled data, discovering hidden patterns without predefined answers. The algorithm explores data to find natural groupings or structures.

**Example:** Customer segmentation groups customers based on purchasing behavior and demographics without predetermined categories. The algorithm finds natural customer clusters for targeted marketing.

**Key Differences:**

| Aspect | Supervised Learning | Unsupervised Learning |
|--------|-------------------|---------------------|
| **Data** | Labeled (known outputs) | Unlabeled (no outputs) |
| **Goal** | Predict outcomes | Discover patterns |
| **Feedback** | Direct error measurement | No explicit feedback |
| **Use Cases** | Classification, regression | Clustering, pattern discovery |

![Supervised vs Unsupervised Learning Comparison](images/Supervised%20learning.avif)

---

## 3. What causes Overfitting? How can it be prevented?

**What is Overfitting?**

Overfitting occurs when a model learns training data too well, memorizing noise and outliers instead of learning general patterns. The model performs excellently on training data but poorly on new, unseen data.

**Main Causes:**

1. **Too Complex Model:** Models with too many parameters memorize training data instead of learning patterns. Like a student memorizing answers instead of understanding concepts.

2. **Too Little Data:** Small datasets don't provide enough examples for the model to learn general patterns, leading to memorization.

3. **Training Too Long:** Extended training causes the model to fit training data peculiarities rather than general patterns.

4. **No Regularization:** Without constraints, models create overly complex decision boundaries that don't generalize.

**Prevention Methods:**

1. **Cross-Validation:** Train on different data subsets and test on held-out portions. If performance drops consistently on test portions, the model is overfitting.

2. **Regularization:** Add penalties for model complexity (L1/L2 regularization) to keep the model simple.

3. **Early Stopping:** Monitor validation performance and stop training when it starts declining.

4. **Data Augmentation:** Increase training data by creating variations (flipping, rotating images) so the model learns robust patterns.

5. **Feature Selection:** Remove irrelevant features to simplify the model.

6. **Ensemble Methods:** Combine multiple models to balance out individual biases.

---

## 4. Explain how training data and test data are split, and why this process is necessary

**How Data is Split:**

Machine learning datasets are divided into three parts:

1. **Training Set (60-80%):** Used to train the model and learn patterns.

2. **Validation Set (10-20%):** Used to tune model settings and make adjustments during development.

3. **Test Set (10-20%):** Kept completely separate until final evaluation to assess real-world performance.

Common split ratios are 70-15-15 or 80-10-10. For small datasets, cross-validation is used instead of a fixed validation set.

**Why It's Necessary:**

1. **Prevent Overfitting:** Without separate test data, we can't tell if the model memorized training data or learned real patterns. Testing on training data gives falsely high accuracy.

2. **Honest Evaluation:** Test data the model has never seen provides an unbiased measure of how it will perform in the real world.

3. **Check Generalization:** If a model performs well on both training and test data, it has learned genuine patterns, not just memorized examples.

4. **Avoid Misleading Results:** Testing on training data is like giving students the exact exam questions beforehand—the scores don't reflect true understanding.

The train-test split ensures we build models that work on new data, not just the data they were trained on.

---

## 5. Case Study: Machine Learning Application in Healthcare

**Title:** "AI Model Accurately Predicts Treatment Outcomes Using Large Patient Datasets"

**Source:** Ohio State University research published in *Patterns* journal (May 2024). Researchers: Ruoqi Liu and Dr. Ping Zhang.

**Background:**

Researchers developed CURE (CaUsal tReatment Effect estimation), an AI model that predicts the best treatments for preventing stroke in heart disease patients. The model was trained on 3 million patient cases from healthcare claims data (2012-2017), including 9,435 medical codes and 9,153 medication codes. It uses a foundation model approach similar to ChatGPT, combining patient data with biomedical knowledge graphs.

**Key Findings:**

1. **Better Performance:** CURE outperformed seven existing ML models by 7-8%.

2. **Matches Clinical Trials:** The model's treatment recommendations matched results from four randomized clinical trials—the gold standard in medical research.

3. **Unique Capability:** No other algorithm can replicate clinical trial results this accurately.

4. **Personalized Medicine:** The model predicts which treatment works best for individual patients based on their characteristics.

**Impact:**

This research shows ML can accelerate drug discovery by identifying promising treatments faster, allowing smaller, more focused clinical trials. Future applications could include FDA-approved AI tools that help doctors access a patient's "digital twin" to guide treatment decisions. The model can be adapted to different diseases and drugs, potentially saving time and money while improving personalized patient care without replacing traditional clinical trials.

---

## References

1. Bergmann, D. (2024). "What is machine learning?" *IBM Think*. Retrieved from https://www.ibm.com/think/topics/machine-learning

2. TechGlad. (2025). "Understand Overfitting in Machine Learning & How to Avoid It." Retrieved from https://techglad.com/overfitting-in-machine-learning/

3. FasterCapital. (2025). "Overfitting: Avoiding Model Risk through Overfitting Prevention Techniques." Retrieved from https://fastercapital.com/content/Overfitting--Avoiding-Model-Risk-through-Overfitting-Prevention-Techniques-update.html

4. Lightly.ai. (2025). "Causes, Detection, and Prevention of Overfitting." Retrieved from https://lightly.ai/blog/overfitting

5. Lightly.ai. (2025). "Train Test Validation Split." Retrieved from https://www.lightly.ai/blog/train-test-validation-split

6. NumberAnalytics. (2025). "Ultimate Overfitting Guide for Regression." Retrieved from https://www.numberanalytics.com/blog/ultimate-overfitting-guide-regression

7. NumberAnalytics. (2025). "Mastering Train and Test Splits in Regression." Retrieved from https://www.numberanalytics.com/blog/training-test-sets-regression

8. HitReader. (2025). "Why train/test split matter: A Statistical Perspective." Retrieved from https://www.hitreader.com/why-train-test-split-matter-a-statistical-perspective/

9. Toxigon. (2024). "What Are Train-Test Split Methods and Why Are They Important in Machine Learning." Retrieved from https://toxigon.com/train-test-split-methods

10. EDUCBA. (2024). "Machine Learning Dataset Split Models Evaluation." Retrieved from https://www.educba.com/train-and-test-in-machine-learning/

11. EMB Global. (2024). "Best Practices for Machine Learning: Train and Test Data." Retrieved from https://blog.emb.global/train-and-test-data/

12. EurekAlert. (2024). "With huge patient dataset, AI accurately predicts treatment outcomes." *The Ohio State University*. Retrieved from https://www.eurekalert.org/news-releases/1043184

13. Liu, R., Chen, P., Wu, L., & Zhang, P. (2024). "CURE: CaUsal tReatment Effect estimation." *Patterns*. The Ohio State University.

---

**Note:** All answers are based on independent research from scholarly articles, books, and reliable sources. AI tools were used for assistance but all content has been verified and understood.
