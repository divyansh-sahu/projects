


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
#from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score

parkinsons_data = pd.read_csv('parkinsons.csv')
parkinsons_data.head()
parkinsons_data.shape()
parkinsons_data.info()

parkinsons_data.isnull().sum()

parkinsons_data.describe()
parkinsons_data['status'].value_counts()

parkinsons_data.groupby('status').mean()


# In[33]:


import seaborn as sns
sns.heatmap(parkinsons_data.corr())


# In[34]:


cor = parkinsons_data.corr()['status']
print(cor)




X = parkinsons_data.drop(columns=['name','status'], axis = 1)
Y = parkinsons_data['status']


# In[ ]:


print(X)


# In[ ]:


print(Y)


# In[ ]:


X_train, X_test, Y_train, Y_test = train_test_split(X , Y, test_size = 0.2, random_state=2)


# In[ ]:


print(X.shape, X_train.shape, X_test.shape)


# In[ ]:





# # DATA STANDARDISATIION

# In[ ]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()


# In[ ]:


scaler.fit(X_train)


# In[ ]:


X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# In[ ]:


print(X_train)


# # Suport vector machine model

# In[ ]:


from sklearn.svm import SVC
classifier = SVC(kernel='rbf')
classifier.fit(X_train, Y_train)


# In[ ]:


y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(Y_test, y_pred)
print(cm)
accuracy_score(Y_test, y_pred)


# # Building a predictive System

# # K - Nearest Neighbour classifier

# In[ ]:


from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=11)
classifier.fit(X_train, Y_train)


# In[ ]:


y_pred = classifier.predict(X_test)


# In[ ]:


from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(Y_test, y_pred)
print(cm)
accuracy_score(Y_test, y_pred)


# # Random Forest Algorithm

# In[ ]:


from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 15, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, Y_train)


# In[ ]:


y_pred1 = classifier.predict(X_test)


# In[ ]:


from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(Y_test, y_pred1)
print(cm)
accuracy_score(Y_test, y_pred1)


# ## XG Bosst Algorithm

# In[ ]:


from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X_train, Y_train)
y_pred2 = classifier.predict(X_test)
cm = confusion_matrix(Y_test, y_pred2)
print(cm)
accuracy_score(Y_test, y_pred2)

