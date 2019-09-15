

import pandas as pd
import numpy as np
# import seaborn as sns
from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')

def abandoning_user(email):
    df = pd.read_csv('conversion_data_user.csv')
    df = df[df['email'] == email]
    df.reset_index(inplace=True)
    usr_id=df.id[0]
    name=df.name[0]
    return name,abandon_prob(usr_id)

def abandon_prob(userid):
    df = pd.read_csv('conversion_data_user.csv')
    df['country'] = df['country'].astype('category')
    df['source'] = df['source'].astype('category')
    df = df[df['id'] == userid]

    df['age'] = np.where(df['age']>=80, 80,df['age'])

    sorted(df['age'],reverse=True)[:10]

    df_country = pd.get_dummies(df['country'])
    df = pd.concat([df, df_country], axis=1)
    df_source = pd.get_dummies(df['source'])
    df = pd.concat([df, df_source], axis=1)
    df.head()


    df1=pd.DataFrame()
    df1['converted']=df['converted']

    df.drop('converted',inplace=True,axis=1)
    df.drop('name',inplace=True,axis=1)
    df.drop('password',inplace=True,axis=1)
    df.drop('id',inplace=True,axis=1)
    # df.drop('country',inplace=True,axis=1)
    # df.drop('source',inplace=True,axis=1)



    #X_train, X_test, y_train, y_test = train_test_split(df[['total_pages_visited','China','Germany','UK','US','Ads','Direct','Seo','age','new_user']], df1['converted'], test_size=0.0, random_state=42)
    X_train = df[['total_pages_visited','China','Germany','UK','US','Ads','Direct','Seo','age','new_user']]
    y_train = df1['converted']


    X_train.shape


    from sklearn.externals import joblib
    filename = 'finalized_model.sav'
    loaded_model = joblib.load(filename)


    loaded_model.score(X_train,y_train)

    a=loaded_model.predict(X_train)

    return a[0]

