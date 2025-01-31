# -*- coding: utf-8 -*-
"""bhakti

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WzJHdQPXkJsxwuIWRAu1DJ0kwTTtX3qK

**CIE1**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("/content/mtcars.csv")
data

plt.hist(data['mpg'],bins=10,color='pink',edgecolor='black')
plt.title("frequency distribution of miles per gollon")
plt.xlabel("miles per gollon")
plt.ylabel("frequency")
plt.grid(True)
plt.show()

plt.scatter(data['wt'],data['mpg'],color='green',edgecolor='black')
plt.title("Relationship between weight and miles per gollon")
plt.xlabel("miles per gollon")
plt.ylabel("weight of the car")
plt.grid(True)
plt.show()

tc=data.groupby('manufacturer').size().nlargest()
tc.plot(kind='bar',color='red')
plt.title("Types of cars")
plt.xlabel("manufacturer")
plt.ylabel('cars')
plt.grid(True)
plt.show()

data.boxplot(column='mpg',by='cyl',color='blue')
plt.title("boxplot")
plt.xlabel("mpg")
plt.ylabel("cyl")
plt.grid(True)
plt.show()

"""CIE-**2**"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

data=fetch_california_housing()
df=pd.DataFrame(data.data,columns=data.feature_names)
df['PRICE']=data.target
df

df.describe()

df.head(5)

df.isnull().sum()

x=df.drop('PRICE',axis=1)
y=df['PRICE']
print(x)
print(y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
x_train
y_train

model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
y_pred

mse=mean_squared_error(y_test,y_pred)
mse

r2_score=r2_score(y_test,y_pred)
r2_score

"""**CIE3**"""

import numpy as pd
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

data=pd.read_csv("/content/titanic.csv")
data

df.describe()
df.head(3)
df.shape
df.isnull().sum()

mean1=np.mean(data['Age'])
median1=np.median(data['Age'])
mode1=stats.mode(data['Age'],keepdims=True).mode[0]
mean2=np.mean(data['Fare'])
median2=np.median(data['Fare'])
mode2=stats.mode(data['Age'],keepdims=True).mode[0]
print("Centrol tendency")
print("mean Age:",mean1)
print("median Age:",median1)
print("mode Age:",mode1)
print("mean Fare:",mean2)
print("median Fare:",median2)
print("mode Fare:",mode2)

filtered_data = data[(data['Survived'].isin([0, 1])) & (data['Pclass'].isin([1, 2, 3]))]
print(filtered_data)

counts = filtered_data.groupby(['Survived','Pclass'])['Survived'].count().unstack()
counts.plot(kind='bar', color=['yellow','pink','red'])
plt.xlabel("Survived (0=No, 1=Yes)")
implt.ylabel("Total of Passengers")
plt.title("Number of Survived & Not Survived by Pclass")
plt.legend(title='Pclass')
plt.show()

"""CIE4"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data=pd.read_csv("/content/Mall_Customers.csv")
data

x=data.iloc[:,[3,4]].values
x

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data=pd.read_csv("/content/Mall_Customers.csv")
data
x = data.iloc[:, [3, 4]].values
wc = []
for i in range(1, 11):
  kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
  kmeans.fit(x)
  wc.append(kmeans.inertia_)
plt.plot(range(1, 11), wc)
plt.title("The Elbow method Graph")
plt.xlabel("number of clusters")
plt.ylabel("WCSS")
plt.show()

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_pred = kmeans.fit_predict(x)
y_pred

plt.scatter(x[y_pred == 0, 0], x[y_pred == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(x[y_pred == 1, 0], x[y_pred == 1, 1], s = 100, c = 'pink', label = 'Cluster 2')
plt.scatter(x[y_pred == 2, 0], x[y_pred == 2, 1], s = 100, c = 'black', label = 'Cluster 3')
plt.scatter(x[y_pred == 3, 0], x[y_pred == 3, 1], s = 100, c = 'green', label = 'Cluster 4')
plt.scatter(x[y_pred == 4, 0], x[y_pred == 4, 1], s = 100, c = 'blue', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

"""**CLE3**"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris=load_iris()
x=iris.data
y=iris.target
x
y

df=pd.DataFrame(data=x,columns=iris.feature_names)
df['species']=pd.Categorical.from_codes(iris.target,iris.target_names)
print(df.head())
print(df.describe())
print(df['species'].value_counts())

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
x_train

clf = DecisionTreeClassifier(random_state=42)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy of the Decision Tree model: {accuracy:.2f}')

"""CLE5"""