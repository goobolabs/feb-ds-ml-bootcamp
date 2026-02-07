# Data Foundations for Machine Learning

In Lesson 1, we explored what Machine Learning is, its types, and the overall workflow.
👉 Now it’s time to focus on the **core ingredient of ML: data**.

Before we can train any model, we must understand:

- What **features (X)** and **labels (y)** are,
- How **samples** come together to form a **dataset**,
- Where data comes from, and what makes it **good or bad**,
- And finally, how to **prepare data** so it’s ready for algorithms.

---

## 🎯 Learning Objectives

By the end of this lesson, students will be able to:

1. Understand the concepts of **features (X)** and **labels (y)**, and explain their role in ML problems.
2. Distinguish between a **sample** (single row) and a **dataset** (collection of samples).
3. Recognize the importance of **data collection**, and identify what makes data relevant, accurate, sufficient, and representative.
4. Explain why **preprocessing** is necessary before training ML models.
5. Apply knowledge of the main preprocessing techniques conceptually, including:

   - Handling missing values
   - Encoding categorical data
   - Scaling numerical features
   - Engineering and selecting features
   - Performing advanced data processing (dimensionality reduction, balancing, noise removal)

---

## Features & Labels

Before training any Machine Learning model, we must clearly define what goes **into** the model and what we want to **get out** of it.
👉 The **inputs** are called **features (X)**, and the **output** we want to predict is called the **label (y)**.

Understanding features and labels is the **first step** in framing an ML problem, because they tell us exactly what the model should learn from the data. Without this distinction, the model has no direction.

---

### 🎨 Visual Analogy

Think of solving a mystery:

- **Features (X) = clues** 🕵️ (footprints, fingerprints, witness reports).
- **Label (y) = the answer** 🧩 (who committed the crime).

Just like a detective uses many clues to figure out the truth, an ML model uses features to predict the correct label.

![Machine Learning Workflow](../images/image-8.png)
---

### 🏡 Example: Housing Dataset

| Size (sq ft) | Bedrooms | Location | Price (\$) |
| ------------ | -------- | -------- | ---------- |
| 1000         | 2        | Suburb   | 200,000    |
| 1500         | 3        | City     | 300,000    |
| 2000         | 4        | Suburb   | 400,000    |
| 1800         | 3        | Rural    | 220,000    |

- **Features (X):** Size, Bedrooms, Location
- **Label (y):** Price

👉 Each row is one **sample** (features + label). Together, all rows form the **dataset**.

“By now, you should be able to identify X and y in any dataset.”

---

## Sample vs Dataset

Once we know what features and labels are, the next step is to see how they are organized in our data.
👉 In ML, data is structured into **samples** (individual examples) and **datasets** (collections of samples).

---

### 1. What is a Sample?

- **Definition:** A **sample** is a single example from the dataset.
- It contains all the **feature values (X)** and the **label (y)** for one case.
- Usually represented as **one row in a table**.

#### Example: One house (sample)

| Size (sq ft) | Bedrooms | Location | Price (\$) |
| ------------ | -------- | -------- | ---------- |
| 1500         | 3        | City     | 300,000    |

- **Features (X):** \[1500, 3, “City”]
- **Label (y):** 300,000

👉 Think of a sample as one **flashcard** — clues (features) on the front, answer (label) on the back.

---

### 2. What is a Dataset?

- **Definition:** A **dataset** is a collection of many samples.
- It is the full table we use to train and test models.
- In tabular form:

  - **Rows = samples**
  - **Columns = features + label**

#### Example Dataset (Houses)

| Size (sq ft) | Bedrooms | Location | Price (\$) |
| ------------ | -------- | -------- | ---------- |
| 1000         | 2        | Suburb   | 200,000    |
| 1500         | 3        | City     | 300,000    |
| 2000         | 4        | Suburb   | 400,000    |
| 1800         | 3        | Rural    | 220,000    |

- Each **row = sample**
- Entire **table = dataset**

---

### 3. Why the Distinction Matters

- **Training:** The model learns from one sample at a time, but across the whole dataset.
- **Splitting:** Later, we divide the dataset into training and test sets — samples are the atomic units being split.
- **Evaluation:** Performance is measured across many samples, not on a single one.

---

### 🎨 Analogy

Imagine you are studying with flashcards:

- **One flashcard = sample** (features on the front, label on the back).
- **The whole deck = dataset.**

👉 The more diverse and complete the deck, the better you can learn.

“You should now be able to differentiate a row (sample) from the full table (dataset).”
![Machine Learning Workflow](../images/image-9.png)

## Data Collection

### 1. Introduction

Every Machine Learning project starts with **data**.
👉 If you don’t have good data, you can’t build a good model — no matter how advanced the algorithm is.

There’s a famous saying in ML:
**“Garbage in → Garbage out.”**
If your dataset is poor quality, the predictions will also be poor.
![Garbage in, Garbage out](../images/image-10.png)

So before preprocessing or modeling, we must carefully consider **where our data comes from** and whether it’s good enough for the task.

---

### 2. Sources of Data

Data can come from many places. Some common sources include:

1. **Databases (internal company systems):**

   - Sales records, customer information, product inventories.
   - Example: Amazon using purchase history to recommend products.

2. **Sensors & IoT devices:**

   - Cameras, microphones, GPS trackers, weather stations.
   - Example: Tesla cars collecting driving data from sensors.

3. **User-generated behavior:**

   - Clicks, likes, shares, time spent on a page.
   - Example: YouTube recommending videos based on your watch history.

4. **Public datasets:**

   - Kaggle, UCI ML Repository, government open data portals.
   - Example: Titanic passenger dataset (predict survival).

5. **APIs / Web Scraping:**

   - Twitter API for tweets, financial APIs for stock prices.
   - Example: Collecting live news headlines to predict market sentiment.

“Always ensure legal basis, consent, and anonymization when working with sensitive data.”

---

### 3. Qualities of Good Data

Not all data is useful. Good datasets should be:

1. **Relevant** – Must match the problem you want to solve.

   - If predicting house prices, don’t collect unrelated data like the owner’s favorite color.

2. **Accurate** – Free from mistakes and errors.

   - Wrong house sizes or incorrect prices will mislead the model.

3. **Sufficient** – Enough examples to learn patterns.

   - A dataset with only 10 houses isn’t enough to build a reliable price predictor.

4. **Representative** – Covers all types of cases.

   - If you only collect city houses, your model won’t work for rural houses.

---

### 4. Example: Housing Dataset (Collected)

Let’s say we collect housing sales data from a real estate website.

| Size (sq ft) | Bedrooms | Location | Price (\$) |
| ------------ | -------- | -------- | ---------- |
| 1000         | 2        | Suburb   | 200,000    |
| 1500         | 3        | City     | 300,000    |
| 2000         | 4        | Suburb   | 400,000    |
| 1800         | 3        | Rural    | 220,000    |
| 1200         | 2        | City     | 250,000    |

- **Relevant:** All columns help predict price.
- **Accurate:** Sizes and prices are correct.
- **Sufficient:** We would need **thousands** of rows like this.
- **Representative:** Must include houses from different regions (City, Suburb, Rural).

---

### 5. Common Challenges in Data Collection

- **Missing data:** Some rows don’t have complete information.
- **Bias:** If only one group is represented (e.g., city houses only).
- **Noisy data:** Wrong entries or typos (e.g., “3000000” instead of “300000”).
- **Privacy:** Some data (like medical or financial) may be restricted.

👉 This is why preprocessing (next step) is critical.

---

### 6. Analogy

Think of ML like cooking:

- **Data = ingredients.**
- **Preprocessing = washing and cutting the vegetables.**
- **Model = the recipe you apply.**
  
![Data = ingredients, Preprocessing = washing and cutting the vegetables, Model = the recipe you apply](../images/image11.png)

If your ingredients (data) are rotten, the final dish (model prediction) will be terrible, no matter how good the chef (algorithm) is.

“You should now understand that the quality of data determines the quality of the model.”

---

## Data Preprocessing

### 1. Introduction

Raw data in the real world is **messy**:

- Some values are missing.
- Some columns are text, which computers can’t process directly.
- Some features are on very different scales.

👉 **Preprocessing** is the step where we **clean and transform** raw data into a format that a machine learning model can use effectively.

Without preprocessing, even the best algorithm will give poor results.

---

### 2. Why Preprocessing is Important

- **Completeness:** Missing data confuses the model.
- **Consistency:** Text categories must be converted into numbers.
- **Fairness:** Features on large scales shouldn’t dominate small-scale features.
- **Accuracy:** Cleaned data → better predictions.

📌 Think of preprocessing as _washing and preparing ingredients before cooking_.

---

### 3. Example Raw Housing Dataset

| Size (sq ft) | Bedrooms | Location | Price (\$) |
| ------------ | -------- | -------- | ---------- |
| 1000         | 2        | Suburb   | 200,000    |
| 1500         | 3        | City     | 300,000    |
| NaN          | 4        | Suburb   | 400,000    |
| 1800         | NaN      | Rural    | 220,000    |
| 1200         | 2        | **??**   | 250,000    |

Problems here:

- Missing **Size** (row 3).
- Missing **Bedrooms** (row 4).
- Unknown **Location** (row 5).

---

## 4. Preprocessing Techniques

### Handling Missing Values

Options:

1. **Remove** rows/columns (if very few are missing).

   - Example: Drop row 5 (location unknown).

2. **Fill (Impute)** missing values with:

   - **Numerical columns** → Mean, Median, or Mode.

     - Example: Replace missing Size with average of other sizes.

   - **Categorical columns** → Most Frequent Category.

     - Example: Fill missing Bedrooms with the most common number of bedrooms (3).

👉 This ensures the dataset stays usable.

---

### Encoding Categorical Data

ML models only understand **numbers**, not text like “City” or “Suburb.”

Two main methods:

1. **Label Encoding**

   - Assign a unique number to each category.
   - Example: City=0, Suburb=1, Rural=2.
   - Problem: Implies order (City < Suburb < Rural), which may not be true.

2. **One-Hot Encoding (preferred for most ML)**

   - Create a new column for each category.
   - Example:

| Size | Bedrooms | Loc_City | Loc_Suburb | Loc_Rural | Price |
| ---- | -------- | -------- | ---------- | --------- | ----- |
| 1000 | 2        | 0        | 1          | 0         | 200k  |
| 1500 | 3        | 1        | 0          | 0         | 300k  |
| 2000 | 4        | 0        | 1          | 0         | 400k  |
| 1800 | 3        | 0        | 0          | 1         | 220k  |

👉 Now the model can “see” location as numbers without fake ordering.

---

### Feature Scaling

Once features are encoded into numbers, there’s still another problem:
👉 Different features may exist on **very different scales**.

For example, in our housing dataset:

- **Size (sq ft):** 1000–2000
- **Bedrooms:** 2–4
- **Price:** 200,000–400,000

Here, “Size” has values in the thousands, while “Bedrooms” is a small integer. If we train models directly, the algorithm may mistakenly think “Size” is far more important than “Bedrooms” simply because its numbers are larger.

---

#### 1. Why Scaling Matters

- **Distance-based models** (KNN, K-Means, SVM) → need scaling to measure distances fairly.
- **Gradient-based models** (Logistic Regression, Neural Networks) → scale helps optimization converge faster.
- **Regularization-based models** (Ridge, Lasso) → penalization depends on feature size.
- **Tree-based models** (Decision Trees, Random Forest, XGBoost) → mostly unaffected by scaling.

👉 In short: **most ML models need scaling**, except for trees.

---

#### 2. Methods of Scaling

There are several ways to scale features:

###### 🔹 A. Normalization (Min-Max Scaling)

- Rescales data to a fixed range, usually **\[0, 1]**.

- Formula:

  $$
  X' = \frac{X - X_{\text{min}}}{X_{\text{max}} - X_{\text{min}}}
  $$

- Example: If Size ranges from 1000–2000, then Size = 1500 →

$$
X' = \frac{1500-1000}{2000-1000} = 0.5
$$

✅ Keeps values bounded, good for neural networks.
❌ Sensitive to outliers.

---

###### B. Standardization (Z-score Scaling)

- Centers data around **mean = 0** and **standard deviation = 1**.
- Formula:

$$
X' = \frac{X - \mu}{\sigma}
$$

---

**Example with Bedrooms = \[2, 3, 4]:**

- Mean ($\mu$) = (2+3+4)/3 = 3
- Standard Deviation ($\sigma$) = √(((2−3)² + (3−3)² + (4−3)²)/3) = √(2/3) ≈ 0.82

Now, for **Bedroom = 4**:

$$
X' = \frac{4 - 3}{0.82} \approx 1.22
$$

---

✅ Good default, works even with outliers.
✅ Preferred for algorithms assuming normal distribution.

---

###### C. Robust Scaling

- Uses **Median** and **IQR (Q3 − Q1)** instead of mean/std.
- Formula:

$$
X' = \frac{X - \text{Median}}{\text{IQR}}
$$

**Example:** Sizes = \[1000, 1500, 2000, 10,000]

- Median = 1750
- Q1 = 1375, Q3 = 3250 → IQR = 1875

Scaled values:

- 1000 → (1000−1750)/1875 = −0.40
- 1500 → (1500−1750)/1875 = −0.13
- 2000 → (2000−1750)/1875 = 0.13
- 10,000 → (10000−1750)/1875 = 4.40

👉 Outlier (10,000) doesn’t distort the smaller values.

---

###### D. Unit Vector Scaling (Normalization by Norm)

- Scales each **row** so its length = 1.
- Formula:

$$
X' = \frac{X}{\|X\|}, \quad \|X\| = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}
$$

**Example:** Row = \[3, 4]

- Norm = √(3² + 4²) = √25 = 5
- Scaled = \[3/5, 4/5] = \[0.6, 0.8]

👉 Often used in **text mining, NLP, and cosine similarity**.

---

#### 3. Housing Example with Scaling

Raw dataset:

| Size (sq ft) | Bedrooms | Price (\$) |
| ------------ | -------- | ---------- |
| 1000         | 2        | 200,000    |
| 1500         | 3        | 300,000    |
| 2000         | 4        | 400,000    |

---

**Min-Max Normalization (0–1):**

| Size_norm | Bedrooms_norm | Price_norm |
| --------- | ------------- | ---------- |
| 0.0       | 0.0           | 0.0        |
| 0.5       | 0.5           | 0.5        |
| 1.0       | 1.0           | 1.0        |

---

**Standardization (mean=0, std=1):**

| Size_std | Bedrooms_std | Price_std |
| -------- | ------------ | --------- |
| -1.0     | -1.0         | -1.0      |
| 0.0      | 0.0          | 0.0       |
| 1.0      | 1.0          | 1.0       |

---

#### 4. Which Scaling to Use?

- **Min-Max Normalization** → Neural Networks, KNN (when no outliers).
- **Standardization (Z-score)** → General-purpose, safe default.
- **Robust Scaling** → When dataset has many outliers.
- **Unit Vector Scaling** → For text/cosine similarity tasks.

---

👉 **Key idea:** Feature scaling doesn’t change the meaning of data — it only makes features comparable, ensuring that algorithms learn fairly.

---

### Feature Engineering & Advanced Data Processing

#### 1. Introduction

After **basic preprocessing** (cleaning, encoding, scaling), we often need to go further:
👉 **Feature Engineering** = creating new features or transforming existing ones to improve model performance.
👉 **Other Data Processing** = extra steps like dimensionality reduction, balancing datasets, or noise filtering.

These steps are often the **“secret sauce”** of good ML projects.

---

#### 2. What is Feature Engineering?

**Definition:**
Feature engineering is the process of using **domain knowledge + creativity** to create, transform, or select features that make machine learning models more effective.

#### Examples with Housing Dataset

| Size (sq ft) | Bedrooms | Location | Price |
| ------------ | -------- | -------- | ----- |
| 1000         | 2        | Suburb   | 200k  |
| 1500         | 3        | City     | 300k  |
| 2000         | 4        | Suburb   | 400k  |
| 1800         | 3        | Rural    | 220k  |

#### Possible Feature Engineering:

1. **Create new features**

   - `Price per sq ft = Price / Size`
   - `Bedrooms per 1000 sq ft = Bedrooms / Size`

2. **Transform features**

   - Convert “Location” into urban=1 vs non-urban=0.
   - Apply log transformation to “Size” if skewed.

3. **Combine features**

   - “House Age” + “Renovation Year” → “Effective Age.”

---

### 3. Feature Selection

Not all features are useful. Some may be irrelevant or harmful (noise).
👉 Feature selection is the process of choosing the **most important features**.

#### Methods:

- **Manual selection** using domain knowledge.
- **Statistical tests** (correlation, chi-square).
- **Model-based selection** (e.g., Random Forest feature importance).

📌 Example: If “Owner’s favorite color” is in the dataset → drop it, because it’s irrelevant to predicting price.

---

### Other Data Processing Steps

#### A. Dimensionality Reduction

- When you have **too many features**, models become slow and may overfit.
- Technique: **Principal Component Analysis (PCA)** reduces features while keeping most of the information.
- Example: 1000 pixel features in images → reduce to 50 principal components.

---

#### B. Balancing Datasets

- Many real-world datasets are **imbalanced** (e.g., 95% healthy patients, 5% sick).
- Models tend to predict the majority class always.
- Solutions:

  - **Oversampling** minority class (e.g., SMOTE).
  - **Undersampling** majority class.

📌 Example: Fraud detection (only 1% of transactions are fraud) → must balance.

---

#### C. Noise Reduction

- Real data may contain errors (sensor glitches, typos).
- Techniques:

  - Smoothing noisy time-series (moving averages).
  - Removing outliers (values far from normal distribution).

---

### Step-by-Step (with Housing Example)

#### 1. **Collect Data**

| Size (sq ft) | Bedrooms | Location | Price (\$) |
| ------------ | -------- | -------- | ---------- |
| 1000         | 2        | Suburb   | 200,000    |
| 1500         | 3        | City     | 300,000    |
| NaN          | 4        | Suburb   | 400,000    |
| 1800         | NaN      | Rural    | 220,000    |
| 1200         | 2        | ??       | 250,000    |

❌ Missing values
❌ Unknown location
❌ Mix of text & numbers

---

#### 2. **Preprocess Data**

##### A. Clean Missing Values

| Size (sq ft) | Bedrooms | Location | Price (\$) |
| ------------ | -------- | -------- | ---------- |
| 1000         | 2        | Suburb   | 200,000    |
| 1500         | 3        | City     | 300,000    |
| 1433 (mean)  | 4        | Suburb   | 400,000    |
| 1800         | 3 (mode) | Rural    | 220,000    |
| 1200         | 2        | City     | 250,000    |

✅ Filled missing **Size** with mean (1433)
✅ Filled missing **Bedrooms** with mode (3)
✅ Fixed unknown location

---

##### B. Encode Categories

| Size | Bedrooms | Loc_City | Loc_Suburb | Loc_Rural | Price |
| ---- | -------- | -------- | ---------- | --------- | ----- |
| 1000 | 2        | 0        | 1          | 0         | 200k  |
| 1500 | 3        | 1        | 0          | 0         | 300k  |
| 1433 | 4        | 0        | 1          | 0         | 400k  |
| 1800 | 3        | 0        | 0          | 1         | 220k  |
| 1200 | 2        | 1        | 0          | 0         | 250k  |

✅ One-hot encoded “Location”

---

##### C. Scale Features

| Size_norm | Bedrooms_std | Loc_City | Loc_Suburb | Loc_Rural | Price |
| --------- | ------------ | -------- | ---------- | --------- | ----- |
| 0.0       | -1.0         | 0        | 1          | 0         | 200k  |
| 0.5       | 0.0          | 1        | 0          | 0         | 300k  |
| 0.4       | 1.0          | 0        | 1          | 0         | 400k  |
| 0.8       | 0.0          | 0        | 0          | 1         | 220k  |
| 0.2       | -1.0         | 1        | 0          | 0         | 250k  |

✅ Size normalized to 0–1
✅ Bedrooms standardized (mean=0, std=1)

---

#### 3. **Feature Engineering**

Add new useful features:

| Size_norm | Bedrooms_std | Price_per_sqft | Loc_City | Loc_Suburb | Loc_Rural | Price |
| --------- | ------------ | -------------- | -------- | ---------- | --------- | ----- |
| 0.0       | -1.0         | 200            | 0        | 1          | 0         | 200k  |
| 0.5       | 0.0          | 200            | 1        | 0          | 0         | 300k  |
| 0.4       | 1.0          | 280            | 0        | 1          | 0         | 400k  |
| 0.8       | 0.0          | 122            | 0        | 0          | 1         | 220k  |
| 0.2       | -1.0         | 208            | 1        | 0          | 0         | 250k  |

✅ Added **Price per sq ft** as new feature

---

#### 4. **Feature Selection**

Remove irrelevant features (if any).
👉 Example: “Owner’s Name” column (not useful for predicting price).

---

#### 5. **Advanced Processing**

- **Dimensionality Reduction:** If 1000s of features → compress with PCA.
- **Balancing:** If predicting classes (e.g., luxury vs non-luxury homes), balance class counts.
- **Noise Removal:** Filter out outliers (e.g., a house mistakenly listed at \$10M).

---

#### 6. **Final Dataset → Model Training**

Now the dataset is:

- Numeric ✅
- Complete (no missing) ✅
- On similar scales ✅
- With engineered + selected features ✅

---

## ✅ Lesson Summary

- **Features (X):** Inputs used for prediction (e.g., size, bedrooms, location).
- **Labels (y):** Outputs we want to predict (e.g., house price).
- **Sample vs Dataset:** One row = sample, collection of rows = dataset.
- **Data Collection:** Good data must be relevant, accurate, sufficient, and representative.
- **Preprocessing:** Essential for model success — includes handling missing values, encoding categories, and scaling features.
- **Feature Engineering & Advanced Processing:** Create new features, drop irrelevant ones, reduce dimensions, balance classes, and handle noise to make data model-ready.

---

## 🔚 End of Lesson 2

🎉 Congratulations! You’ve completed **Data Foundations for Machine Learning**.

---