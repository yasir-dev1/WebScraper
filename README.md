# Web Scraping GUI Application  
# Description

This Python application provides a graphical user interface (GUI) for web scraping using PyQt5 and a custom web scraping module (presumably in the Scraper.py file). Users can specify a CSV file containing URLs, select a folder to save the scraped results, and provide a "tag" and a "class" for scraping.
# Prerequisites

Python 3.x installed on your system.
PyQt5 library installed (pip install PyQt5).
A web scraping module (Scraper.py) that provides the Scrap function for the actual scraping logic.

# How to Use

1.Make sure you have all the prerequisites installed.

2.Place the Scraper.py file in the same directory as this code.

3.Create a user interface file named GUI.ui using the Qt Designer tool or another method.

4.Run the code using the following command:

    python Main.py


# 5.The GUI will appear with the following options:

* CSV File: Click on the "Browse" button to select a CSV file containing URLs for scraping.

* Result Folder: Click on the "Browse" button to select a folder where the scraped data will be saved.

* Tag: Enter an HTML tag to specify which elements you want to scrape (e.g., 'div', 'a', 'p').

* Class: Enter an HTML class attribute value to further filter the elements to be scraped (optional).

* Start: Click this button to initiate the web scraping operation.

6.Once you click "Start," a progress bar will appear, indicating that the scraping process is ongoing.

5.After the scraping is complete, the progress bar will disappear, and the scraped data should be saved in the selected folder.

# Important Notes

* Ensure that the Scraper.py module contains the necessary web scraping logic. The Scrap class in the code handles running this logic in a separate thread to prevent freezing the GUI.

* Make sure to handle any exceptions or errors that may occur during web scraping in the Scraper.py module.

* This code provides a basic framework for creating a web scraping GUI. You may need to customize it further to suit your specific scraping needs and error handling.

* PyQt5 is used for the GUI, so you can style and design the UI further using Qt Designer or by modifying the GUI.ui file.

