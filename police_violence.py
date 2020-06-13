import pandas as pd
import matplotlib.pyplot as plt

def get_data(filename):
    cols = ['Victim\'s gender','Victim\'s race','Date of Incident (month/day/year)','State']
    df = pd.read_excel(filename, sheet_name='2013-2019 Police Killings', usecols=cols)
    df.to_csv('data.csv')
    df2 = pd.read_csv('data.csv')
    combine(df2)

def stats():
    data = pd.read_csv('data.csv')

    s_dict = {}

    for idx, row in data.iterrows(): 
        if row['State'] not in s_dict:
            s_dict[row['State']] = {'Hispanic':0, 'Asian':0, 'Black':0, 'White':0,'Unknown race':0,'Native American':0, 'Pacific Islander':0}
        for k, v in s_dict.items():
            for key, val in s_dict[k].items():
                if (row['State'] == k and row['Victim\'s race'] == key):
                    s_dict[k][key] = s_dict[k].get(key) + 1

    print(s_dict)
    graph(s_dict)


def graph(dict):
    plt.figure()
    df = pd.DataFrame(dict)
    df.transpose().plot(kind="bar", stacked=True);
    plt.title('Police Violence (2013-2019)')
    plt.xlabel('State')
    plt.ylabel('Num of Killings')

    plt.show()

def main():
    filename = pd.ExcelFile('MPVDataset.xlsx')
    get_data(filename)

stats()