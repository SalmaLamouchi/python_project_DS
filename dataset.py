import pandas as pd
import matplotlib.pyplot as plt
import sns
import seaborn as sns
def collecter_dataset():
    df = pd.read_csv('salary.csv')
    return df

def afficher_courbes(dataset):
    
    df = dataset
    df.plot(x='Gender', y='Salary', kind='bar')
    plt.xlabel('Gender')
    plt.ylabel('Salary')
    plt.title('Salaire en fonction du sexe')
    plt.show()

def Salaire_AnneeExp(dataset):
   
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

    
    plt.figure(figsize=(10, 6))
    sns.histplot(dataset['Salary'], kde=True, color='purple')
    plt.axvline(mean_salary, color='red', linestyle='dashed', linewidth=2, label=f'Moyenne: {mean_salary:.2f}')
    plt.axvline(median_salary, color='green', linestyle='dashed', linewidth=2, label=f'Médiane: {median_salary}')
    plt.title('Distribution des Salaires')
    plt.xlabel('Salaire')
    plt.ylabel('Fréquence')
    plt.legend()
    plt.show()

   
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=dataset['Salary'], color='orange')
    plt.title('Boîte à Moustaches des Salaires')
    plt.xlabel('Salaire')
    plt.show()

    
    print("Moyenne des salaires : ", mean_salary)
    print("Médiane des salaires : ", median_salary)
    print("Écart-type des salaires : ", std_deviation)


def analyser_age(dataset):
   
    mean_age = dataset['Age'].mean()
    median_age = dataset['Age'].median()
    std_deviation = dataset['Age'].std()

   
    plt.figure(figsize=(10, 6))
    sns.histplot(dataset['Age'], kde=True, color='blue')
    plt.axvline(mean_age, color='red', linestyle='dashed', linewidth=2, label=f'Moyenne: {mean_age:.2f}')
    plt.axvline(median_age, color='green', linestyle='dashed', linewidth=2, label=f'Médiane: {median_age}')
    plt.title('Distribution des Ages')
    plt.xlabel('Âge')
    plt.ylabel('Fréquence')
    plt.legend()
    plt.show()

  
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=dataset['Age'], color='orange')
    plt.title('Boîte à Moustaches des Ages')
    plt.xlabel('Âge')
    plt.show()

   
    print("Moyenne des ages : ", mean_age)
    print("Médiane des ages : ", median_age)
    print("Écart-type des ages : ", std_deviation)




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


def comparer_salaires_par_age(dataset):
    
    bins = [20, 30, 40, 50, 60, 70, 80, 90]
    labels = ['20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89']

    dataset['AgeGroup'] = pd.cut(dataset['Age'], bins=bins, labels=labels, right=False)

    
    moyennes_salaires = dataset.groupby('AgeGroup')['Salary'].mean().reset_index()

    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='AgeGroup', y='Salary', data=moyennes_salaires, palette='viridis')
    plt.xlabel('Groupe d\'Âge')
    plt.ylabel('Salaire Moyen')
    plt.title('Comparaison des Salaires Moyens par Groupe d\'Âge')
    plt.show()

def comparer_salaires_par_gender(dataset):
    
    dataset['GenderGroup'] = dataset['Gender']

   
    moyennes_salaires = dataset.groupby('GenderGroup')['Salary'].mean().reset_index()

    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='GenderGroup', y='Salary', data=moyennes_salaires, palette='viridis')
    plt.xlabel('Genre')
    plt.ylabel('Salaire Moyen')
    plt.title('Comparaison des Salaires Moyens par Genre')
    plt.show()

    
    print("Salaires moyens par groupe de Genre :")
    print(moyennes_salaires)


def comparer_salaires_par_experience(dataset):
   
    bins = [0, 3, 6, 9, 12, 15, 18, 21]
    labels = ['0-3', '4-6', '7-9', '10-12', '13-15', '16-18', '19-21']
    dataset['ExperienceGroup'] = pd.cut(dataset['Years of Experience'], bins=bins, labels=labels, right=False)

    
    moyennes_salaires = dataset.groupby('ExperienceGroup')['Salary'].mean().reset_index()

    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='ExperienceGroup', y='Salary', data=moyennes_salaires, palette='viridis')
    plt.xlabel('Années d\'Expérience')
    plt.ylabel('Salaire Moyen')
    plt.title('Comparaison des Salaires Moyens par Années d\'Expérience')
    plt.show()

    
    print("Salaires moyens par groupe d'expérience :")
    print(moyennes_salaires)
