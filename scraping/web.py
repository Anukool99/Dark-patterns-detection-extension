from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

def get_links_from_ecommerce_list(url):
    # Set up Chrome WebDriver (you can use other browsers by downloading their drivers)
    driver = webdriver.Chrome()

    # Navigate to the URL
    driver.get(url)

    # Find all links within h3 tags
    links = driver.find_elements(By.XPATH, "//h3//a[@href]")

    ecommerce_links = [link.get_attribute("href") for link in links]

    # Close the browser window
    driver.quit()

    return ecommerce_links

def save_links_to_csv(links, csv_filename='ecommerce_links.csv'):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for link in links:
            writer.writerow({'Link': link})

if __name__ == "__main__":
    ecommerce_links = get_links_from_ecommerce_list('https://nuvoretail.com/ultimate-guide-top-100-ecommerce-platforms-in-india/')
    save_links_to_csv(ecommerce_links)

    print("Links saved to ecommerce_links.csv")
