# Statistical Analysis of Gaseous Emissions

This repository contains a Python script used to perform statistical analysis of gaseous emissions data for thesis work. The analysis compares emissions under different conditions (inside versus outside, covered versus uncovered) to explore significant differences using statistical tests.

## Dataset
The analysis uses a dataset with emissions data for various gases such as:
- Carbon Dioxide (CO2)
- Methane (CH4)
- Nitrous Oxide (N2O)
- Ammonia (NH3)
- Propan equivalent (FTIR)

Each emission is recorded for different piles under two conditions:
- **In/Out**: Emissions measured inside vs outside.
- **Pile Cover Types**: Covered piles (ProfiCover, Gore Cover) vs uncovered piles.

The dataset must be provided in an Excel format, and the file name should be specified as `Data.xlsx`.

## Statistical Tests

### 1. Shapiro-Wilk Test
- **Purpose**: Checks for normality of the emission data.
- **Output**: A dictionary of p-values for each emission column indicating whether the data follows a normal distribution.

### 2. Mann-Whitney U Test
- **Purpose**: Compares emissions from inside vs outside for each pile type.
- **Output**: A dictionary of p-values indicating significant differences between inside and outside emission measurements.

### 3. Independent T-test
- **Purpose**: Compares the emissions from covered piles (ProfiCover and Gore Cover) versus uncovered piles, only for inside data.
- **Output**: A dictionary of p-values showing whether there are significant differences in emissions between covered and uncovered piles.

## How to Run the Script

1. **Install Required Libraries**:
   Install the required Python libraries using the following command:
   ```bash
   pip install pandas scipy
   ```

2. **Place Your Dataset**:
   Place the `Data.xlsx` file in the same directory as the script.

3. **Run the Script**:
   Execute the script using Python:
   ```bash
   python statistical_analysis.py
   ```

4. **Output**:
   - The script will output the p-values for each test, stored in dictionaries:
     - `shapiro_p_values`: p-values for the Shapiro-Wilk normality test.
     - `mannwhitney_p_values`: p-values for the Mann-Whitney U test comparing inside vs outside emissions.
     - `ttest_p_values`: p-values for the independent t-test comparing covered vs uncovered pile emissions.

## Notes
- The p-values provide insight into whether the differences observed are statistically significant (p < 0.05 is typically considered significant).
- The data cleaning and handling steps, such as dealing with missing data using `.dropna()`, are embedded in the statistical tests.

## License
This project is licensed under the MIT License. Feel free to use or modify the code as needed.
