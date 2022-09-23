# MACHINE LEARNING

# Credits: https://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/


#### Three different learning styles in ML algorithms.


### 1. SUPERVISED LEARNING:

# ---- This involves training data and a known result for the variables to initially train the model.
# ---- A model is prepared through a training process which is required to do predictions. It will be corrected when it does wrong outputs. The training process continues until the model achieves a desired level of accuracy using the training data
# ---- Examples: Classification & Regression models.
# ---- Example algorithms include: Logistic Regression and the Back Propagation Neural Network.


### 2. UNSUPERVISED LEARNING:

# ---- This doesnt invlove the data with labelled or known results.
# ---- The model is prepared by deducing structures present in the input data to extract general rules.
# ---- Example: Clustering, Dimensionality Reduction, & Association Rule Mining 
# ---- Example algorithms include: K-Means & Apriori algorithm.


### 3. SEMI-SUPERVISED LEARNING:

# ---- In this case, the input data will be a mixture of labelled and unlabelled results.
# ---- Here the model is expected to learn the structures in the data and make desired predictions.
# ---- Examples: Classification & Regression models.



# Knowing which algorithm exists for a business problem is crucual in machine learning. ML algorithms can be grouped in different ways. However, I find it useful to group them by the learning styles.

#### 1. REGRESSION ALGORITHMS:

# ---- Regression is all about modelling the relationship among the variables that iteratively refined by a a measure of error in predictions made by the model. The most popular regression algorithms are:
# ------- a. Ordinary Least Squares Regression (OLSR)
# ------- b. Linear Regression
# ------- c. Logistic Regression
# ------- d. Stepwise Regression
# ------- e. Multivariate Adaptive Regression Splines (MARS)
# ------- f. Locally Estimated Scatterplot Smoothing (LOESS)


### 2. REGULARIZATION ALGORITHMS

# ---- This is an extention made to above Regression algoriths.
# ---- These are modifications made to other algorithms. The examples are:
# ------- a. Ridge Regression
# ------- b. Least Absolute Shrinkage & Selection Operator (LASSO)
# ------- c. Elastic Net
# ------- d. Least Angle Regression (LARS)


### 3. INSTANCE-BASED ALGORITHMS (MEMORY BASED LEARNING):

# ---- Instance based learning model is a decision problem with instances or examples of training data that are deemed important or required to the model.
# ---- Such methods usually build up a database of example data & compare new data to the database using similarity measures in order to find the best match and make the prediction. Hence this is also called Memory based learning.
# ---- The most popular regression algorithms are:
# ------- a. k-Nearest Neighbor (kNN)
# ------- b. Learning Vector Quantization (LVQ)
# ------- c. Self Organizing Map (SOM)
# ------- d. Locally Weighted Learning (LWL)
# ------- e. Support Vector Machines (SVM)


### 4. DECISION TREE ALGORITHMS

# ---- Decision Tree methods constructs a model of decision made based on actual values of attributes in the data.
# ---- Decisions fork-in tree structures until a prediction decision is made for a given record. Decision tree methods are often fast and accurate. The most popular algorithms are:
# ------- a. Classification & Regression Tree (CART)
# ------- b. Iterative Dichotomiser 3 (ID3)
# ------- c. C4.5 and C5.0 (different versions of a powerful approach)
# ------- d. Chi-squared Automatic Interaction Detection (CHAID)
# ------- e. Decision Stump
# ------- f. M5
# ------- g. Conditional Decision Trees


### 5. BAYESIAN ALGORITHMS

# ---- These explicitly apply Baye's theorem on classification and regression problems.
# ---- The most popular algorithms are: 
# ------- a. Naive Bayes
# ------- b. Gaussian Naive Bayes
# ------- c. Multinomial Naive Bayes
# ------- d. Averaged One-Dependence Estimators (AODE)
# ------- e. Bayesian Belief Network (BBN)
# ------- f. Bayesian Network (BN)


### 6. CLUSTERING ALGORITHMS

# ---- Clustering methods are typically organized by modelling approache such as centroid-based & hierarchal.
# ---- All methods are concerned with using inherent structures in the data into groups of maximum commonality.
# ---- The most popular algorithms are:
# ------- a. k-MEANS
# ------- b. k-MEDIANS
# ------- c. Expectation-Maximization (EM)
# ------- d. ierarchical Clustering


### 7. ASSOCIATION RULE LEARNING ALGORITHMS

# ---- This is used to extract the observed relationshipns among the data points. This can discover important and commercially useful associations in large multidimensional datasets
# ---- The most popular algorithms are:
# ------- a. Apriori
# ------- b. ECLAT algorithm


### 8. ARTIFICAL NEURAL NETWORK ALGORITHMS

# ---- These are models inspired by structure and/or function of biological neural networks.
# ---- These are a class of pattern matching that are commonly used for regression and classification problems.
# ------- a. Perceptron
# ------- b. Multilayer Perceptrons (MLP)
# ------- c. Back-Propagation
# ------- d. Stochastic Gradient Descent
# ------- e. Hopfield Network
# ------- f. Radial Basis Function Network (RBFN)


### 9. DEEP LEARNING ALGORITHMS

# ---- These are a modern update to Artificial Neural Networks that exploit abundant cheap computation. They are concerned with building much larger and more complex neural networks and many methods are concerned with very large datasets of labelled analog data, such as image, text. audio, and video.
# ------- a. Convolutional Neural Network (CNN)
# ------- b. Recurrent Neural Networks (RNNs)
# ------- c. Long Short-Term Memory Networks (LSTMs)
# ------- d. Stacked Auto-Encoders
# ------- e. Deep Boltzmann Machine (DBM)
# ------- f. Deep Belief Networks (DBN)


### 10. DIMENSIONALITY REDUCTION ALGORITHMS

# ---- Like clustering methods, dimensionality reduction is also concerned with the inherent structure in the data.
# ---- But in this case, its in an unsupervised manner or order to summarize or describe data using less information.
# ---- This can be useful to visualize dimensional data or to simplify data which can then be used in a supervised learning method. Many of these methods can be adapted for use in classification and regression. The most popular algorithms are:
# ------- a. Principal Component Analysis (PCA)
# ------- b. Principal Component Regression (PCR)
# ------- c. Partial Least Squares Regression (PLSR)
# ------- d. Sammon Mapping
# ------- e. Multidimensional Scaling (MDS)
# ------- f. Projection Pursuit
# ------- g. Linear Discriminant Analysis (LDA)
# ------- h. Mixture Discriminant Analysis (MDA)
# ------- i. Quadratic Discriminant Analysis (QDA)
# ------- j. Flexible Discriminant Analysis (FDA)


### 11. ENSEMBLE ALGORITHMS

# ---- Ensemble methods are models composed of multiple weaker models that are independently trained and whose predictions are combined in some way to make the overall prediction.
# ---- Much effort is put into what types of weak learners to combine and the ways in which to combine them. This is a very powerful class of techniques and as such is very popular.
# ------- a. Boosting
# ------- b. Bootstrapped Aggregation (Bagging)
# ------- c. AdaBoost
# ------- d. Weighted Average (Blending)
# ------- e. Stacked Generalization (Stacking)
# ------- f. Gradient Boosting Machines (GBM)
# ------- g. Gradient Boosted Regression Trees (GBRT)
# ------- h. Random Forest


### 12. OTHER MACHINE LEARNING ALGORITHMS

# ---- The algorithms which are not covered in the above listing are:
# ------- a. Feature selection algorithms
# ------- b. Algorithm accuracy evaluation
# ------- c. Performance measures
# ------- d. Optimization algorithms
# ------- e. Computational intelligence (evolutionary algorithms, etc.)
# ------- f. Computer Vision (CV)
# ------- g. Natural Language Processing (NLP)
# ------- h. Recommender Systems
# ------- i. Reinforcement Learning
# ------- j. Graphical Models
