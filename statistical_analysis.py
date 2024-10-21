import pandas as pd
from scipy.stats import shapiro, mannwhitneyu, ttest_ind

# Load the dataset
data = pd.read_excel("Data.xlsx")

# Columns representing the emissions under investigation
emissions_cols = [
    'Carbon dioxide CO2 [v/v%]', 'Methane CH4 [ppm]', 'Nitrous oxide N2O [ppm]', 
    'Ammonia NH3 [ppm]', 'Propan equivalent (FTIR) [ppm]'
]

# Test for normality using the Shapiro-Wilk test
shapiro_p_values = {}
for column in emissions_cols:
    _, p_value = shapiro(data[column].dropna())
    shapiro_p_values[column] = p_value

# Compare gaseous emissions from the inside versus the outside using Mann-Whitney U test
mannwhitney_p_values = {}
piles = data['Pile'].unique()
for pile in piles:
    pile_data = data[data['Pile'] == pile]
    inside_data = pile_data[pile_data['In/out'] == 'in']
    outside_data = pile_data[pile_data['In/out'] == 'out']
    
    for column in emissions_cols:
        _, p_value = mannwhitneyu(inside_data[column].dropna(), outside_data[column].dropna())
        mannwhitney_p_values[(pile, column)] = p_value

# Independent sample t-test to compare inside emissions of the covers to the Uncovered method
ttest_p_values = {}
cover_types = ["ProfiCover", "EPTFE Cover"]
uncovered_data = data[(data['Pile Name'] == 'Uncovered') & (data['In/out'] == 'in')]

for cover in cover_types:
    cover_data = data[(data['Pile Name'] == cover) & (data['In/out'] == 'in')]
    
    for column in emissions_cols:
        _, p_value = ttest_ind(cover_data[column].dropna(), uncovered_data[column].dropna(), equal_var=False)
        ttest_p_values[(cover, column)] = p_value
