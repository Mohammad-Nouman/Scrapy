# **Zameen.com Home Listings Scraper**

A web scraper designed to extract detailed information about home listings from Zameen.com, a popular real estate website. This project collects home data and saves it in both CSV and MySQL database formats for easy analysis and storage.

## **Installation**

To run this scraper, you need to have **Scrapy** and **MySQL Connector** installed.

## **Install the dependencies with:**

```bash
pip install scrapy mysql-connector-python
```
## **Usage**

To start scraping home listings, run the following command:

scrapy crawl homes
This command initiates the scraper and begins collecting home data from Zameen.com.

## **Configuration**
Data Feed: Configure data output in settings.py by setting the **FEED_FORMAT** to CSV and the **FEED_URI** to **output.csv**. This saves the scraped data in a CSV file named output.csv.
Pipeline: Enable **ZameenHomePipeline** in settings.py to automatically store data in a MySQL database. Ensure the pipeline is correctly configured with your MySQL credentials.
## **Output**
The scraper saves output in two formats:

CSV File: A structured CSV file (output.csv) containing the home listing details.
MySQL Database: Data is also stored in a MySQL database table for easy querying and further analysis.
## **Legal and Ethical Notice**
Please ensure that your use of this scraper complies with Zameen.com's Terms of Service and respects their robots.txt file. This project is for educational and personal use only.



