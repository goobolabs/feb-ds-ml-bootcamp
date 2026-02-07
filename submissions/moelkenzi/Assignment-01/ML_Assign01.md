# Machine Learning Assignment One

## 1. Defining Machine Learning

Machine Learning is a branch of Artificial Intelligence that enables computers to learn patterns from data and improve task performance without being explicitly programmed with predefined rules.

The system adjusts its internal parameters based on experience and uses what it has learned to make predictions or decisions.

### Real-life example

**Crop disease detection from satellite and drone imagery.**

- **Inputs:** multispectral satellite images, weather history, soil data.
- **Task:** predict fields at high risk of fungal infection so targeted treatment can be applied.
- **Why ML:** disease signatures are subtle, non-linear, and vary with local conditions — rule lists are brittle but ML models can learn complex spatial and temporal patterns and update from new labeled observations.

---

## 2. Supervised vs Unsupervised Learning — comparative analysis

ML methods are often categorized by the supervision level in training data.

### Supervised learning (predictive mapping)

- **Data:** labeled examples (features + target).
- **Tasks:**
  - _Classification_ (discrete labels) — e.g., defect / no-defect in manufacturing.
  - _Regression_ (continuous targets) — e.g., short-term solar power output prediction.
- **Validation:** straightforward because ground truth exists.
- **Industrial use:** risk scoring, demand forecasting, diagnostic models.

**Example (original): Predictive maintenance in manufacturing**

- Use sensor streams (vibration, temperature, runtimes) labeled with failure/no-failure to predict imminent failures and schedule servicing.

### Unsupervised learning (structural discovery)

- **Data:** unlabeled; the algorithm discovers structure.
- **Tasks:** clustering, anomaly detection, dimensionality reduction, association rules.
- **Use cases:** customer segmentation, exploratory analysis, anomaly detection in networks.

**Example (original): Urban sound clustering**

- Cluster short audio clips collected around a city to group similar noise sources (construction, traffic, sirens). Clusters reveal patterns useful for urban planning or automated labeling.

### Compact comparison

| Aspect                      | Supervised                        | Unsupervised                           |
| :-------------------------- | :-------------------------------- | :------------------------------------- |
| **Labels required**         | Yes                               | No                                     |
| **Goal**                    | Predict or map inputs → outputs   | Discover structure or anomalies        |
| **Typical outputs**         | Class labels, numeric predictions | Clusters, reduced features, outliers   |
| **Example industrial uses** | Credit scoring, medical diagnosis | Market segmentation, anomaly detection |

---

## 3. Overfitting: mechanisms and prevention

### What overfitting is

Overfitting occurs when a model captures idiosyncratic noise in the training data rather than the underlying signal, producing excellent training performance and poor generalization on new data.

### Theoretical lens: bias–variance tradeoff

- **Bias:** error from wrong model assumptions (underfitting).
- **Variance:** error from sensitivity to training data fluctuations (overfitting).
  > Total expected error ≈ Bias² + Variance + Irreducible noise.

### Causes of overfitting

- Excessive model complexity relative to data volume
- Noisy, irrelevant features
- Insufficient or unrepresentative training data
- Data leakage during training/tuning

### Prevention strategies (practical techniques)

- **Regularization**: penalize large weights (L2/ridge), or use L1/lasso to encourage sparsity. Elastic Net mixes both.
- **Cross-validation**: use K-fold CV to estimate performance reliably and set hyperparameters.
- **Early stopping**: halt iterative training when validation loss stops improving.
- **Ensembling**: average many models (bagging, boosting) to reduce variance.
- **Feature selection / dimensionality reduction**: remove irrelevant inputs or compress via PCA.
- **Gather more and better data**: increase representative coverage.

### Quick diagnostics table

| Situation                             | Probable cause              | Recommended remedy                      |
| :------------------------------------ | :-------------------------- | :-------------------------------------- |
| Low train & low val performance       | Underfitting (high bias)    | Increase model complexity, add features |
| High train & low val performance      | Overfitting (high variance) | Regularize, add data, reduce complexity |
| Train loss improving, val loss rising | Overfitting during training | Early stopping, dropout                 |

---

## 4. Training data and test data

### Why splitting matters

Evaluating a model on the same data used to train it gives overly optimistic results (memorization ≠ generalization). Proper partitioning provides an unbiased estimate of performance.

### Common partitions

- **Training set:** fit model parameters
- **Validation (dev) set:** tune hyperparameters and do model selection
- **Test set:** single final unbiased performance estimate

A typical split is **~70–80% train / 10–15% val / 10–20% test**, but proportions depend on dataset size. With very large datasets, a smaller test fraction may suffice.

### Sampling strategies

- **Random sampling** — simple, works well with large, homogeneous data.
- **Stratified sampling** — ensures class proportions are preserved in splits (important for imbalanced classes).
- **Stable hashing for reproducibility** — use a deterministic hash (e.g., CRC32 or other stable hash) of a record’s stable identifier to decide membership so the test set remains constant across experiments.

### Diagnosing distribution mismatch

If model performance is good on a training-representative set but poor on production-like validation data, you have a **data mismatch** (feature shift, covariate shift, or label shift). The remedy may involve collecting representative labeled data, domain adaptation techniques, or monitoring and retraining pipelines.

---

## 5. Machine learning in infrastructure — case studies

> The three concise case studies below illustrate how the computational foundations translate into industry outcomes.

### 1) Transportation — Dakhla–Paris corridor (route optimization)

- **Objective:** optimize transcontinental route selection for reduced travel time, fuel cost, and better compliance with constraints.
- **Approach:** combine historical GPS, traffic density, weather, and safety data; train and evaluate multiple models including neural networks and tree-based ensembles.
- **Findings:** neural networks captured complex non-linear interactions and outperformed simpler statistical baselines; the system enabled dynamic switching among precomputed routes (a rolling optimization) and delivered measurable reductions in travel time and fuel consumption.
- **Practical notes:** success depended heavily on data quality, temporal alignment of inputs, and careful out-of-sample validation to avoid leakage.

### 2) Healthcare — inpatient bed demand / clinical risk prediction

- **Objective:** forecast bed demand and identify patients at risk of acute outcomes (e.g., AKI).
- **Approach:** use EHR time series, labs and vitals; apply supervised models and validate across hospitals.
- **Findings:** ML models can identify patients earlier than standard clinical scores and forecast resource needs more accurately; however, model drift across hospitals requires local recalibration and continual monitoring.
- **Practical notes:** regulatory, ethical, and data-privacy considerations are essential for deployment (explainability and audit trails matter).

### 3) Business — SME inventory and demand forecasting (Kolay.ai style)

- **Objective:** help SMEs forecast sales and automate segmentation to improve inventory planning.
- **Approach:** combine historic sales, promotions, and calendar features; apply gradient boosted trees or recurrent models for time-series demand.
- **Findings:** improved forecast accuracy reduced stockouts and overstock; automated segments enabled targeted promotions.
- **Practical notes:** even simpler models trained on good-quality data often deliver large ROI; integrating forecasts into business workflows (ordering, replenishment) is crucial.

---

## 6. Conclusions and practical lessons

1. **Data quality beats algorithm complexity.** A simpler model fed high-quality, representative data often outperforms a complex model trained on noisy, biased samples.
2. **Partition correctly and avoid leakage.** Proper train/validation/test separation and stable sampling procedures are essential to estimate real-world performance.
3. **Regularize and validate.** Use regularization, cross-validation, and ensembling to control overfitting and reduce variance.
4. **Monitor and maintain deployed models.** Concept drift and distribution shifts require monitoring, periodic retraining, and robust logging for traceability.
5. **Context matters.** No single algorithm works for all problems (No Free Lunch). Success combines domain knowledge, careful data engineering, and statistical rigor.

---
