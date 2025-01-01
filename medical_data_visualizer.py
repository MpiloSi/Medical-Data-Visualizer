import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['BMI'] = df['weight'] / (df['height'] ** 2)
df['overweight'] = (df['BMI'] > 25).astype(int)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else (1 if x > 1 else x))
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else (1 if x > 1 else x))

# 4
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
                     var_name='feature', value_name='value')
    df_cat = df_cat[df_cat['value'].isin([0, 1])]

    fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

    # Plot for cardio = 0
    sns.countplot(x='feature', hue='value', data=df_cat[df_cat['cardio'] == 0], ax=axes[0])
    axes[0].set_title('Cardio = 0')
    axes[0].set_xlabel('Feature')
    axes[0].set_ylabel('Count')

    # Plot for cardio = 1
    sns.countplot(x='feature', hue='value', data=df_cat[df_cat['cardio'] == 1], ax=axes[1])
    axes[1].set_title('Cardio = 1')
    axes[1].set_xlabel('Feature')

    plt.suptitle('Counts of Categorical Features by Cardio Status')
    
    fig.savefig('catplot.png')
    plt.show()
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.copy()

    df_heat = df_heat[(df_heat['ap_lo'] <= df_heat['ap_hi']) & 
                      (df_heat['height'] >= df_heat['height'].quantile(0.025)) & 
                      (df_heat['height'] <= df_heat['height'].quantile(0.975)) &
                      (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) & 
                      (df_heat['weight'] <= df_heat['weight'].quantile(0.975))]
    
    df_heat = df_heat.drop(['BMI', 'overweight'], axis=1)

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(8, 6))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', square=True,
                cbar_kws={"shrink": .8}, ax=ax)

    ax.set_title('Correlation Heatmap')
    

    # 16
    fig.savefig('heatmap.png')
    return fig