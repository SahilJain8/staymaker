# Staymaker - Hotel Hosting Data Scraper

Staymaker is a project that uses Django and Google Cloud to scrape hotel hosting data from various booking websites and save it in a MySQL database hosted on Google Cloud Platform (GCP).
Installation

To install and run Staymaker, follow these steps:

    Clone the Staymaker repository from GitHub:


git clone https://github.com/your-username/staymaker.git

Navigate to the staymaker directory:


cd staymaker

Install the required Python packages using pip:

pip install -r requirements.txt

Set up your MySQL database on GCP and configure the DATABASES setting in settings.py to use the correct database connection details.

Start the Django development server:

    python manage.py runserver

    Access the Staymaker web app by navigating to http://localhost:8000 in your web browser.

# Usage

Once you have installed and run Staymaker, you can use it to scrape hotel hosting data from various booking websites and save it in your MySQL database. To do so, follow these steps:

    Log in to the Staymaker web app using your username and password.

    Navigate to the "Scraper" section of the app.

    Enter the details of the hotels you want to scrape data for, including the website you want to scrape from and the check-in and check-out dates.

    Click the "Scrape" button to begin scraping data for the specified hotels.

    Once the scraping is complete, you can view the scraped data in the "Data" section of the app.

# Contributing

If you would like to contribute to the development of Staymaker, please follow these steps:

Fork the Staymaker repository on GitHub.

Clone your forked repository to your local machine.

Create a new branch for your changes:

git checkout -b my-new-feature

Make your changes and commit them to your branch:

sql

git commit -am 'Add some new feature'

Push your changes to your forked repository:

git push origin my-new-feature

Create a new pull request on the original Staymaker repository on GitHub and describe your changes.

# Credits

Staymaker was created by sahil jain 

The project is built on top of the following technologies:

    Django
    Google Cloud Platform
    MySQL
    Python