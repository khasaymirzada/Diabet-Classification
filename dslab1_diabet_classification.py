# -*- coding: utf-8 -*-
"""DSlab1_Diabet_Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-CJH7eXGfqGrcyXeOcWZQRtDQlgkE9bq

**Data importing**
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing  
label = preprocessing.LabelEncoder()

dataset=pd.read_csv('/content/Diabetes .csv')

dataset.head()

"""# **Descriptive part**"""

dataset.describe()

"""# **Data cleaning : Missing value**"""

print(dataset.isnull().sum())

updated_df = dataset
updated_df['Chol']=updated_df['Chol'].fillna(updated_df['Chol'].mean())
updated_df.info()

updated_df = updated_df.dropna(axis=0)

print(updated_df.isnull().sum())

numeric_data = updated_df.drop(["CLASS","ID","Gender"],axis=1)
numeric_data.head()

corr = numeric_data.corr()
ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);

updated_df['CLASS'] = updated_df['CLASS'].replace(['Y'],'Yes')

updated_df['CLASS'] = updated_df['CLASS'].replace(['N'],'No')

updated_df['Gender'] = updated_df['Gender'].replace(['f'],'F')

updated_df = updated_df[updated_df["CLASS"].isin(["Yes", "No"])]

"""# **Data preparation**"""

from sklearn import preprocessing
import pandas as pd
d = preprocessing.normalize(numeric_data)
names=numeric_data.columns
scaled_df = pd.DataFrame(d,columns=names)
scaled_df.head()

updated_df['Gender']= label.fit_transform(updated_df['Gender']) 
print(updated_df['Gender'].unique())

concatenated = pd.concat([scaled_df, updated_df[['CLASS']]], axis=1)
concatenated.head()

print(concatenated.isnull().sum())

concatenated = concatenated.dropna(axis=0)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(scaled_df)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['pc1', 'pc2'])

pcadf = pd.concat([principalDf, updated_df['CLASS']], axis=1)
pcadf.head()

"""# **Logistic Regression**"""

feature_cols = ['No_Pation', 'AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL',
       'VLDL', 'BMI']
X = concatenated[feature_cols] # Features
y = concatenated.CLASS # Target variable

X.columns

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression()

# fit the model with data
logreg.fit(X_train,y_train)

#
y_pred=logreg.predict(X_test)

from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
cnf_matrix

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(max_depth = 2, 
                             random_state = 0)

clf.fit(X_train, y_train)

from sklearn import tree

tree.plot_tree(clf);

"""# **Support Vector Machine**"""

from sklearn import svm

#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred1 = clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred1))

from sklearn import metrics

# Model Accuracy: how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred1))

"""# **KNN**"""

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

"""# **Random Forest**"""

y_train = np.array(y_train)

X_train = np.array(X_train)

from sklearn.ensemble import RandomForestClassifier
# Instantiate model with 1000 decision trees
rf = RandomForestClassifier(n_estimators = 100) 
# Train the model on training data
rf.fit(X_train, y_train);
y_pred = rf.predict(X_test)

print("ACCURACY OF THE MODEL: ", metrics.accuracy_score(y_test, y_pred))

"""# **Decision Tree**"""

from sklearn.tree import DecisionTreeClassifier

dec_tree = DecisionTreeClassifier(criterion = "gini",
            random_state = 100,max_depth=3, min_samples_leaf=5)
  
# Performing training
dec_tree.fit(X_train, y_train)

y_pred = dec_tree.predict(X_test)

from sklearn.metrics import accuracy_score

print ("Accuracy : ",accuracy_score(y_test,y_pred)*100)

"""# **Information Gain**"""

def comp_feature_information_gain(df, target, descriptive_feature, split_criterion):
    """
    This function calculates information gain for splitting on 
    a particular descriptive feature for a given dataset
    and a given impurity criteria.
    Supported split criterion: 'entropy', 'gini'
    """
    
    print('target feature:', target)
    print('descriptive_feature:', descriptive_feature)
    print('split criterion:', split_criterion)
            
    target_entropy = compute_impurity(df[target], split_criterion)

    # we define two lists below:
    # entropy_list to store the entropy of each partition
    # weight_list to store the relative number of observations in each partition
    entropy_list = list()
    weight_list = list()
    
    # loop over each level of the descriptive feature
    # to partition the dataset with respect to that level
    # and compute the entropy and the weight of the level's partition
    for level in df[descriptive_feature].unique():
        df_feature_level = df[df[descriptive_feature] == level]
        entropy_level = compute_impurity(df_feature_level[target], split_criterion)
        entropy_list.append(round(entropy_level, 3))
        weight_level = len(df_feature_level) / len(df)
        weight_list.append(round(weight_level, 3))

    print('impurity of partitions:', entropy_list)
    print('weights of partitions:', weight_list)

    feature_remaining_impurity = np.sum(np.array(entropy_list) * np.array(weight_list))
    print('remaining impurity:', feature_remaining_impurity)
    
    information_gain = target_entropy - feature_remaining_impurity
    print('information gain:', information_gain)
    
    print('====================')

    return(information_gain)

def compute_impurity(feature, impurity_criterion):
    """
    This function calculates impurity of a feature.
    Supported impurity criteria: 'entropy', 'gini'
    input: feature (this needs to be a Pandas series)
    output: feature impurity
    """
    probs = feature.value_counts(normalize=True)
    
    if impurity_criterion == 'entropy':
        impurity = -1 * np.sum(np.log2(probs) * probs)
    elif impurity_criterion == 'gini':
        impurity = 1 - np.sum(np.square(probs))
    else:
        raise ValueError('Unknown impurity criterion')
        
    return(round(impurity, 3))



# how to test for an incorrect compute_impurity_criterion value:
# print('impurity using gini index:', compute_impurity(df['stream'], 'foo'))

split_criteria = 'gini'
for feature in concatenated.drop(columns='CLASS').columns:
    feature_info_gain = comp_feature_information_gain(concatenated, 'CLASS', feature, split_criteria)