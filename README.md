#@ Scrappers
###This repo contains various forms of scrappers


###Scrapper 1 - written in Python 2.7

`Similarweb.py`

This scrapper takes in a list of website you want to scrap data, the output is a csv file.
[get]

Here are the functions:

`get_data`: input a name of website like `airbnb,com`, and returns a `dict` of data

`get_results`: take in a list of website names, and return a `list` consisted of `dict` data

`write_to_csv`: write out the all the data to `csv` file into the same directory
