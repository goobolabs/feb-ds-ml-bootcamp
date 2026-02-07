Assignment 1

 1. Definition of Machine Learning with Real-Life Example
Machine Learning is a field of artificial intelligence that enables computers to learn from data and improve their performance on specific tasks without being explicitly programmed. It involves algorithms that can identify patterns, make predictions, or make decisions based on input data.

Real-Life Example: Netflix Recommendation System
Netflix uses ML algorithms to analyze your viewing history, ratings, and watch patterns, along with data from millions of other users. The system learns what types of content you prefer and recommends shows and movies you're likely to enjoy, with the recommendations becoming more accurate over time as it learns from your continued interactions.

2. Supervised vs. Unsupervised Learning with Examples
 Supervised Learning:
Learning from labeled data where each training example has an input-output pair. The algorithm learns a mapping function from inputs to outputs.

Example: Loan Default Prediction
A bank trains a model using historical loan application data where each application is labeled with the outcome: "defaulted" or "repaid." The model learns patterns from applicant features like income, credit score, and employment history to predict whether future applicants are likely to default on their loans.

 Unsupervised Learning:
Learning from unlabeled data to discover hidden patterns, groupings, or structures without pre-defined categories.

Example: Network Intrusion Detection
A cybersecurity system analyzes network traffic logs without pre-labeled attack categories. The algorithm identifies clusters of unusual behavior patterns, detecting potential security threats like DDoS attacks, port scanning, or data exfiltration that don't match normal network activity patterns.

 3. Causes of Overfitting and Prevention Methods
Causes:
Overly complex models with too many parameters
Insufficient training data
Training for too many iterations
Learning noise instead of underlying patterns
Prevention:
Use more training data
Simplify the model architecture
Apply regularization techniques
Use cross-validation
Implement early stopping during training

 4. Data Splitting Methods and Their Necessity

Process:
Data is typically split into:
Training Set (70-80%): Used to train the model
Validation Set (10-15%): Used to tune model parameters
Test Set (10-15%): Used for final evaluation
Necessity:
This split prevents data leakage, ensures the model can generalize to unseen data, provides unbiased performance evaluation, and helps detect overfitting before deployment.

 5. Case Study: ML in Healthcare
Study: "Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs" - Gulshan et al., JAMA, 2016

Findings Summary:
This research developed a deep learning algorithm to detect diabetic retinopathy from retinal images. The system achieved 90-94% sensitivity and 98% specificity, comparable to ophthalmologists. It demonstrated potential for automated screening in areas with limited access to eye care specialists, enabling early detection and intervention to prevent blindness in diabetic patients. The study highlighted ML's ability to scale medical expertise and improve healthcare accessibility.

