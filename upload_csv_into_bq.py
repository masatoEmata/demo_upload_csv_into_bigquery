import pandas as pd

file_path = './sample.csv'

df = pd.read_csv(file_path, encoding='shift-jis')
print(df)

dataset_id = 'demo_dataset'
table_id = 'demo_table'

df.to_gbq('{}.{}'.format(dataset_id, table_id), if_exists='replace')
