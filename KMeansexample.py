from sklearn.cluster import KMeans

# Чтение данных из файла CSV
df = pd.read_csv('path_to_your_data.csv')

# Выбор колонок для кластеризации
cols_to_cluster = ['col1', 'col2', 'col3'] # замените на нужные колонки

# Применение алгоритма K-средних
kmeans = KMeans(n_clusters=3, random_state=0).fit(df[cols_to_cluster])

# Добавление метки кластера к DataFrame
df['cluster'] = kmeans.labels_

# Визуализация результатов кластеризации
df.plot.scatter(x='col1', y='col2', c='cluster')
