from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set()

# Conversion des données en DataFrame Panda pour les afficher avec seaborn
df = pd.DataFrame(iris.data, columns=iris['feature_names'] )
df['target'] = iris.target
df['label'] = df.apply(lambda x: iris['target_names'][int(x.target)], axis=1)
df.head()

sns.pairplot(df, hue='label', vars=iris['feature_names'], height=2)
plt.show()