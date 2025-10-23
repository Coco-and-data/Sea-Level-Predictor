import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/master/epa-sea-level.csv')
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    years_extended = np.arange(df['Year'].min(), 2051)
    
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line1 = slope * years_extended + intercept
    ax.plot(years_extended, line1, 'r', label='Best fit line (1880-2050)')
    
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    line2 = slope2 * years_recent + intercept2
    ax.plot(years_recent, line2, 'g', label='Best fit line (2000-2050)')
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    plt.savefig('sea_level_plot.png')
    return plt.gca()
