# -*- coding: utf-8 -*-
from lxml import html
import requests
import csv

page = requests.get('http://www.similarweb.com/website/fietsenwinkel.nl')
tree0 = html.fromstring(page.content)

# Import website lists
name_list = ['airbnb.com', 'bbc.com', 'CNN.com']


# return a list of data from a single website

def get_data(website_name):
    # Generate tree
    full_name = ''.join(['http://www.similarweb.com/website/', website_name])
    page = requests.get(full_name)
    tree = html.fromstring(page.content)
    dict0 = dict()
    # Metrics
    categories = tree.xpath('//a[@class="rankingItem-subTitle is-link"]/text()')[2]
    total_visits = \
    tree.xpath('//span[@class="engagementInfo-value engagementInfo-value--large u-text-ellipsis"]/text()')[0]
    basic = tree.xpath('//span[@class="engagementInfo-value u-text-ellipsis"]/text()')
    time_on_site = basic[0];
    page_views = basic[1];
    bounce_rate = basic[2]
    # List of 5 countries
    country_name = tree.xpath('//a[@class="country-name country-name--link"]/text()')
    country1 = tree.xpath('//span[@class="traffic-share-value traffic-share-value--large"]/text()')
    country_rest = tree.xpath('//span[@class="traffic-share-value "]/text()')
    # List of 5 percentages
    country_per = country1 + country_rest
    traffic_sources = tree.xpath('//div[@class="trafficSourcesChart-value"]/text()')
    direct = traffic_sources[0];
    referral = traffic_sources[1];
    search = traffic_sources[2]
    social = traffic_sources[3];
    mail = traffic_sources[4];
    display = traffic_sources[5]
    search = tree.xpath('//span[@class="searchPie-number"]/text()')
    organic_search = search[0];
    paid_search = search[1]
    social_names = tree.xpath('//a[@class="socialItem-title name link"]/text()')
    social_networks = tree.xpath('//div[@class="socialItem-value"]/text()')

    dict0['name'] = website_name
    dict0['categories'] = categories;
    dict0['total_visits'] = total_visits;
    dict0['time_on_site'] = time_on_site

    return dict0


# Compile all data into a dictionary #website_data is a dictionary data for each website

def get_results(name_list):
    results = []
    for name in name_list:
        results.append(get_data(name))
    return results


# Write data to csv file
# combined_list is a dict file

def write_to_csv(combined_list, output_file):
    colnames = ['name', 'time_on_site', 'total_visits', 'categories']

    with open(output_file, 'w') as outcsv:
        writer = csv.DictWriter(outcsv, fieldnames=colnames)
        writer.writeheader()
        writer.writerows(combined_list)


#######################################
#  Testing ############################
#######################################

if __name__ == '__main__':
    data_dict = get_results(name_list)
    write_to_csv(data_dict, 'data.csv')
