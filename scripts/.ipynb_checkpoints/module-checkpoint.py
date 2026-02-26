
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import matplotlib.patches as mpatches  # For patterns
import scipy.stats as stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from scipy.stats import chi2_contingency
from statsmodels.stats.diagnostic import lilliefors
from scipy.stats import bartlett, levene
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import normaltest
from scipy.stats import kruskal

department_mapping = {
    1: "Applied Mathematics and Statistics",
    2: "Chemical and Biological Engineering",
    3: "Civil and Environmental Engineering",
    4: "Chemistry",
    5: "Computer Science",
    6: "Economics and Business",
    7: "Engineering, Design, and Society",
    8: "Electrical Engineering",
    9: "Geology and Geological Engineering",
    10: "Geophysics",
    11: "Humanities, Arts, and Social Sciences",
    12: "Mechanical Engineering",
    13: "Metallurgical and Materials Engineering",
    14: "Mining Engineering",
    15: "Petroleum Engineering",
    16: "Physics",
    # Add more mappings as needed
}

Cluster = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5]
Department = ['Mechanical Engineering', 'Civil and Environmental Engineering',
              'Computer Science', 'Electrical Engineering', 'Applied Mathematics and Statistics',
              'Metallurgical and Materials Engineering', 'Geology and Geological Engineering', 'Mining Engineering',
              'Petroleum Engineering', 'Geophysics', 'Physics', 'Chemistry', 'Chemical and Biological Engineering',
              'Economics and Business', 'Engineering, Design, and Society', 'Humanities, Arts, and Social Sciences']

c1 = []
c2 = []
c3 = []
c4 = []
c5 = []

def count_usage_cases(dept, con, dic):
    for i in range(len(con)):
        if con[i] == 1:
            #print(department_mapping[dept[i]])
            dic[department_mapping[dept[i]]] += 1
    return dic

def create_degree_lists(df, column_index, num_categories):
    """
    Generalizes the creation of degree-specific lists from a DataFrame column.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        column_index (int): The column index to use for degree values.
        num_categories (int): The number of degree categories (e.g., 3 for undergrad, MS, PhD).

    Returns:
        dict: A dictionary with keys as degree categories (1, 2, 3, ...) 
              and values as lists with binary indicators for each row.
    """
    # Initialize dictionary to hold degree lists
    degree_lists = {category: [0] * len(df) for category in range(1, num_categories + 1)}

    # Extract the relevant column
    degree_column = df.iloc[:, column_index]

    # Populate the lists based on the degree column values
    for i in range(len(degree_column)):
        if degree_column[i] in degree_lists:
            degree_lists[degree_column[i]][i] = 1

    return degree_lists

def count_cluster_wise(dic):
    Cluster = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5]
    Department = ['Mechanical Engineering', 'Civil and Environmental Engineering',
              'Computer Science', 'Electrical Engineering', 'Applied Mathematics and Statistics',
              'Metallurgical and Materials Engineering', 'Geology and Geological Engineering', 'Mining Engineering',
              'Petroleum Engineering', 'Geophysics', 'Physics', 'Chemistry', 'Chemical and Biological Engineering',
              'Economics and Business', 'Engineering, Design, and Society', 'Humanities, Arts, and Social Sciences']

    # Initialize count list with zeros, one for each cluster (0-indexed, so 6 clusters in total)
    count = [0] * 6  # Clusters range from 1 to 5, hence need to handle indexing carefully
    for key in dic:  # Iterate through dictionary `dic`
        for i in range(len(Department)):  # Iterate through each department
            if key == Department[i]:  # If department in `dic` matches a department
                indx = Cluster[i]  # Get corresponding cluster from `Cluster`
                count[indx] += dic[key]  # Adjust index to 0-based
    return count


def pre_vec(vec):
    c1.append(vec[1])
    c2.append(vec[2])
    c3.append(vec[3])
    c4.append(vec[4])
    c5.append(vec[5])


def nordept(vec):
    total = np.sum(vec)
    # Normalize each element in the vector and round to the nearest 10th
    for i in range(len(vec)):
        vec[i] = round((vec[i] / total) * 100, 1)
    return vec


def deptwisecount(df, columns_to_check, clusterno):
    # Combine the columns into a new DataFrame
    combined_df = pd.concat(columns_to_check, axis=1)
    
    # Calculate if each student answered at least one question
    df['answered_any'] = combined_df.sum(axis=1) > 0
    
    # Get the department column
    dept = df['What department or program are you in?']
    
    # Group by department and count students who answered at least one question
    count = 0
    dept_wise_count = df[df['answered_any']].groupby(dept)['answered_any'].count()
    for i in range(len(Cluster)):
        if Cluster[i] == clusterno:
            dept = Department[i]
            #print(dept)
            # Find the corresponding key
            key = next((k for k, v in department_mapping.items() if v == dept), None)
            #print(key)
            count += dept_wise_count[key]
    return count

def normalized_dept_cluster(df, vec, columns_to_check, clusterno):
    total = deptwisecount(df, columns_to_check, clusterno)
    print(total)
    # Normalize each element in the vector and round to the nearest 10th
    for i in range(len(vec)):
        vec[i] = round((vec[i] / total) * 100, 1)
    return vec



def create_vector(df, loc):
    l1 = {dept_name: 0 for dept_name in department_mapping.values()}
    dept = df['What department or program are you in?']
    
    l1_att = df.iloc[:, loc]  
    
    l1 = count_usage_cases(dept, l1_att, l1)
    
    count = count_cluster_wise(l1)
    
    print(count)
    
    pre_vec(count)
    print(c1)
    return c1, c2, c3, c4, c5


def create_vector2(data):
    l1 = {dept_name: 0 for dept_name in department_mapping.values()}
    dept = df['What department or program are you in?']
    
    l1_att = data  
    
    l1 = count_usage_cases(dept, l1_att, l1)
    
    count = count_cluster_wise(l1)
    
    print(count)
    
    pre_vec(count)
    print(c1)


def clear_vec():
    c1.clear()
    c2.clear()
    c3.clear()
    c4.clear()
    c5.clear()


def culster_wise_val(dept, att):
    
    departments = ['Mech-Civil', 'CS-EE-AMS', 'Met-Geo-Pet', 'Phys-Chem', 'Society']
    scores_mech = []
    scores_cs = []
    scores_met = []
    scores_phys = []
    scores_society = []


    for i in range(len(att)):
        if not pd.isna(att[i]):
            d = department_mapping[dept[i]]
            clusterno = 0
            for j in range(len(Department)):
                if d == Department[j]:
                    clusterno = Cluster[j]
                    #print(clusterno)
                    #print(d)
                    break
            if clusterno == 1:
                scores_mech.append(att[i])
            elif clusterno == 2:
                scores_cs.append(att[i])
            elif clusterno == 3:
                scores_met.append(att[i])
            elif clusterno == 4:
                scores_phys.append(att[i])
            elif clusterno == 5:
                scores_society.append(att[i])
    return scores_mech, scores_cs, scores_met, scores_phys, scores_society
        


def create_con_table(att1, att2):
    # Create a contingency table
    contingency_table = pd.crosstab(att1, att2)
    return contingency_table


def chi_square_test(contigency_table):
    # Perform the chi-square test
    data = contigency_table.to_numpy()
    chi2, p, dof, expected = chi2_contingency(data)
    
    print(f"Chi-Square Statistic: {chi2:.4f}")
    print(f"P-Value: {p:}")
    print(f"Degrees of Freedom: {dof}")
    print("Expected Frequencies:")
    print(expected)
    
    # Interpretation
    if p < 0.05:
        print("There is a significant relationship")
    else:
        print("There is no significant relationship")
    return data, expected


def residuals_cal(observed, expected):
    # Calculate standardized residuals
    standardized_residuals = (observed - expected) / np.sqrt(expected)
    
    # Print standardized residuals
    print("Standardized Residuals:")
    print(standardized_residuals)
    
    # Identify significant cells
    significant_cells = np.abs(standardized_residuals) > 2
    print("\nSignificant Cells (Residuals > 2 or < -2):")
    print(significant_cells)
    return standardized_residuals


def create_group(dep, indep):
    low = []
    high = []
    for i in range(len(indep)):
        if indep[i] >=0 and indep[i] <= 40 and not pd.isna(indep[i]) and not pd.isna(dep[i]):
            low.append(dep[i])
        elif indep[i] > 40 and indep[i] <= 100 and not pd.isna(indep[i]) and not pd.isna(dep[i]):
            high.append(dep[i])
    return low, high


def normality_test(group): # assumption 2 testing: data are normally distributed
    # Shapiro-Wilk test
    stat, p = stats.shapiro(group)  # Test for normality
    print(f"Shapiro-Wilk Test: Statistic={stat}, P-value={p}")
    
    # Decision
    if p < 0.05:
        print(f" Group: Data is NOT normally distributed.\n")
    else:
        print(f" Group: Data is normally distributed.\n")

    # Plot histogram and Q-Q plot
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.hist(group, bins=10, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title("Histogram")
    plt.xlabel("SES")
    plt.ylabel("Frequency")
    
    plt.subplot(1, 2, 2)
    stats.probplot(group, dist="norm", plot=plt)
    plt.title("Q-Q Plot")
    plt.tight_layout()
    plt.show()


def agostino_pearson_test(data): # test for normal distribution
    stat, p = normaltest(data)
    print(f"D'Agostino and Pearson's Test: Statistic={stat}, P-value={p}")
    # Decision
    if p < 0.05:
        print(f" Group: Data is NOT normally distributed.\n")
    else:
        print(f" Group: Data is normally distributed.\n")


def kruskal_wallis_test(sample1, sample2): # non-parametric
    # Kruskal-Wallis H-test
    stat, p = kruskal(sample1, sample2)
    print(f"Kruskal-Wallis Test: Statistic={stat}, P-value={p}")
    
    # Interpretation
    if p < 0.05:
        print("Reject the null hypothesis: There is a significant difference")
    else:
        print("Fail to reject the null hypothesis: No significant difference.")


