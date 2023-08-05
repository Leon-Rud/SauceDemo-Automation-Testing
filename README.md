# SauceDemo Automation Testing

This repository contains automated test scripts for the SauceDemo e-commerce website. The project follows best practices of Page Object Model (POM), extensive logging, and detailed reporting. The testing framework used is pytest, with Selenium WebDriver for browser interactions.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Page Object Model (POM)](#page-object-model-pom)
- [Setup and Installation](#setup-and-installation)
- [Running the Tests](#running-the-tests)
- [Test Cases](#test-cases)
- [Logging and Reporting](#logging-and-reporting)
- [Contact Information](#contact-information)

## Technologies Used

- Python
- Selenium WebDriver
- pytest

## Page Object Model (POM)

In this project, the following page objects have been implemented:

- LoginPage
- BasePage
- CartPage
- CheckoutPage
- InventoryPage

## Setup and Installation

### Prerequisites
* Python 3.7 or above
* Pytest 6.2 or above
* Selenium 3.141.0 or above

### Installation
1. Clone the repository to your local machine: ```git clone https://github.com/Leon-Rud/SauceDemo-Automation-Testing.git```
2. Install the project dependencies: ```pip install -r requirements.txt```

## Running the Tests

To run the tests, navigate to the project directory and run the following command:

```python -m pytest```

You can also specify additional pytest options. For example, to run the tests in verbose mode and generate a report, use:

```python -m pytest -v --html=report.html```

## Test Cases

This project includes tests for various features of the SauceDemo website, such as:

- Login functionality
- Shopping cart functionality
- Checkout process
- Inventory management

## Logging and Reporting

The project generates a detailed test execution report after every run, which includes the test case name, the status of the test case, and other relevant details.

![Screenshot 1.png](..%2F..%2FScreenshot%201.png)

## Contact Information

For any queries or discussions related to this project, feel free to contact me at:

- [LinkedIn](https://www.linkedin.com/in/leon-rudnitsky-027256105/)
- Email: leonrud6@gmail.com
