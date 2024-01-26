from bs4 import BeautifulSoup
import requests
import csv

def get_links_sellercenter(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    # Extract links from <td> elements with data-title="Store"
    for td in soup.find_all('td', {'data-title': 'Store'}):
        anchor = td.find('a', href=True)
        if anchor:
            links.append(anchor['href'])

    return links

def get_links_webinopoly(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    # Extract links from <td> elements with data-title="Store Address"
    for td in soup.find_all('td', {'data-title': 'Store Address'}):
        anchor = td.find('a', href=True)
        if anchor:
            links.append(anchor['href'])

    return links

def save_links_to_csv_combined(sellercenter_links, webinopoly_links, csv_filename='combined_links.csv'):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Write links from sellercenter
        for link in sellercenter_links:
            writer.writerow({'Link': link})

        # Write links from webinopoly
        for link in webinopoly_links:
            writer.writerow({'Link': link})

if __name__ == "__main__":
    sellercenter_links = get_links_sellercenter('https://sellercenter.io/top-500-shopify-stores')
    webinopoly_links = get_links_webinopoly('https://webinopoly.com/blogs/news/top-100-most-successful-shopify-stores')

    save_links_to_csv_combined(sellercenter_links, webinopoly_links)

    print("Links saved to combined_links.csv")
