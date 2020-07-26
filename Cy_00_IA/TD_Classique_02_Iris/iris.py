from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()

import seaborn as sns
import pandas as pd

sns.set()
df = pd.DataFrame(data, columns=iris['feature_names'] )
df['target'] = target
df['label'] = df.apply(lambda x: iris['target_names'][int(x.target)], axis=1)
df.head()

sns.pairplot(df, hue='label', vars=iris['feature_names'], height=2);
plt.show()