# In this notebook we plot the world population and the gross domestic product per country

year = 2000

# Parameters
year = 2017


# !pip install plotly

from plots import sundial_plot

# ## World Population

sundial_plot('SP.POP.TOTL', 'World Population', year)

# ## Gross Domestic Product (current USD)

sundial_plot('NY.GDP.MKTP.CD', 'Gross Domestic Product', year)


