# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# In this notebook we plot the world population and the gross domestic product per country

# + tags=["parameters"]
year = 2000
# -

# !pip install plotly

from plots import sundial_plot

# ## World Population

sundial_plot('SP.POP.TOTL', 'World Population', year)

# ## Gross Domestic Product (current USD)

sundial_plot('NY.GDP.MKTP.CD', 'Gross Domestic Product', year)


