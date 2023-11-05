import pandas as pd
import matplotlib.pyplot as plt
import sns
def collecter_dataset():
    df = pd.read_csv('salary.csv')
    return df

def afficher_courbes(dataset):
    # le salaire en fonction du sexe
    df = dataset
    df.plot(x='Gender', y='Salary', kind='bar')
    plt.xlabel('Gender')
    plt.ylabel('Salary')
    plt.title('Salaire en fonction du sexe')
    plt.show()

def Salaire_AnneeExp(dataset):
   # le salaire en fonction du Years of Experience
    df = dataset
    df.plot(x='Years of Experience', y='Salary', kind='scatter')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.title('Salaire en fonction d\'annee d\'experience  ')
    plt.show()


def analyser_salaires(dataset):
    
    mean_salary = dataset['Salary'].mean()

    median_salary = dataset['Salary'].median()

   
    std_deviation = dataset['Salary'].std()

    print("Moyenne des salaires : ", mean_salary)
    print("Médiane des salaires : ", median_salary)
    print("Écart-type des salaires : ", std_deviation)

import seaborn as sns

def afficher_correlation(dataset):
   
    dataset_numerique = dataset.select_dtypes(include=['float64', 'int64'])

    
    correlation_matrix = dataset_numerique.corr()

    
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Matrice de corrélation')
    plt.show()


def regression_lineaire(dataset):
    from sklearn.linear_model import LinearRegression

    X = dataset[['Years of Experience']]
    y = dataset['Salary']

    model = LinearRegression()
    model.fit(X, y)

    predicted_salaries = model.predict(X)

    plt.scatter(X, y, label='Données réelles')
    plt.plot(X, predicted_salaries, color='red', label='Régression linéaire')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()
