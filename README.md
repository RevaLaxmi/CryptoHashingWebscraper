# Cryptocurrency Web Scraper and Automated Trading System

## Project Overview
Developed a cryptocurrency website automation tool using Python and Selenium for efficient web scraping. The tool significantly reduced manual data extraction time and provided real-time updates on cryptocurrency trends and prices. This system automates the entire process of trading cryptocurrencies, including logging transactions, computing taxes, and managing wallets.

## Table of Contents
1. [Introduction](#introduction)
2. [Project Description](#project-description)
3. [System Features](#system-features)
   - [Automated Trading](#automated-trading)
   - [Tax Calculation](#tax-calculation)
   - [Web Scraping](#web-scraping)
   - [Wallet Management](#wallet-management)
4. [Implementation Details](#implementation-details)
   - [Parameters](#parameters)
   - [Workflow](#workflow)
5. [Challenges and Solutions](#challenges-and-solutions)
6. [Future Enhancements](#future-enhancements)
7. [Installation and Setup](#installation-and-setup)
8. [Usage](#usage)
9. [Project Links](#project-links)

## Introduction
This project aims to automate cryptocurrency trading activities, including selling tokens, logging transactions, computing taxes, and managing wallets. The tool uses Python and Selenium for web scraping to provide real-time updates on cryptocurrency trends and prices, allowing for efficient and automated decision-making.

## Project Description
The system automates the entire process of cryptocurrency trading for an investor who performs actions manually. It handles:
- Selling tokens daily
- Logging sales transactions
- Computing taxes
- Managing wallets

The client receives new tokens daily and needs a system to automate selling them, logging transactions, and handling taxes based on a specified strategy.

## System Features

### Automated Trading
- Automatically sells a specified number of tokens daily.
- Logs transactions, including the number of tokens sold and the corresponding prices.

### Tax Calculation
- Computes taxes on sold tokens.
- Applies a specified tax rate (e.g., 20%).
- Handles FIFO (First-In-First-Out) for tax calculation:
  - Keeps track of token acquisition prices.
  - Computes capital gains based on the selling price and acquisition price.

### Web Scraping
- Uses Python and Selenium for web scraping.
- Provides real-time updates on cryptocurrency trends and prices.

### Wallet Management
- Manages multiple cryptocurrency wallets.
- Logs income and capital for received tokens.
- Ensures accurate tracking of tokens based on acquisition and selling prices.

## Implementation Details

### Parameters
- Daily token sale amount: e.g., sell 20 tokens daily.
- Tax rate: e.g., 20%.
- Token acquisition prices for FIFO calculations.

### Workflow
1. **Data Acquisition:** 
   - Use Selenium to scrape real-time cryptocurrency prices.
2. **Automated Trading:** 
   - Sell specified number of tokens daily.
   - Log sales transactions, including the number of tokens sold and selling prices.
3. **Tax Calculation:** 
   - Apply the specified tax rate to compute taxes on sold tokens.
   - Use FIFO to compute capital gains based on acquisition prices.
4. **Wallet Management:** 
   - Log income and capital for received tokens.
   - Ensure accurate tracking of tokens.

## Challenges and Solutions
- **Complex Tax Calculation:** 
  - Implemented FIFO method to accurately compute capital gains.
- **Real-Time Data Acquisition:** 
  - Used Selenium for efficient and reliable web scraping of cryptocurrency prices.
- **Accurate Wallet Management:** 
  - Developed a comprehensive logging system to track all transactions and token movements.

## Future Enhancements
- Integrate with more cryptocurrency exchanges for diversified trading.
- Implement machine learning algorithms for predictive trading strategies.
- Enhance the user interface for easier management and monitoring of automated trades.

## Installation and Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RevaLaxmi/Crypto-Web-Scraper.git
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Parameters:**
   - Set daily token sale amount, tax rate, and other parameters in the configuration file.

4. **Run the Application:**
   ```bash
   python main.py
   ```

## Usage
1. **Start the Application:** 
   - The system will begin scraping cryptocurrency prices and executing automated trades based on the configured parameters.
2. **Monitor Logs:** 
   - Check logs for transaction details, tax calculations, and wallet updates.


Feel free to reach out if you have any questions or need further clarification on the project.
