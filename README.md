# IP-and-NUMBER_locator
This is a program to find the location of an IP and verification of a number this uses 2 API that are provided by IPSTACK and NUMVERIFY 

## 📍 ipandnum_locator
> A Python-based tool that leverages the power of ipstack and numverify APIs to provide detailed geolocation and phone number validation services.

## 🔧 Features
> - IP Geolocation: Retrieve detailed information about an IP address, including country, region, city, ZIP code, latitude, longitude, time zone, and more.
> - Phone Number Validation: Validate phone numbers, determine their line type (mobile, landline, VoIP), carrier, and country of origin.

## 📡 APIs Utilized
- ## ipstack
  ipstack offers real-time IP geolocation services, allowing you to pinpoint the location of any IP address.
  - ### Free Plan:
    > - Monthly Requests: 100
    > - Features: Basic geolocation data (country, region, city, ZIP code, latitude, longitude)
    > - SSL encryption support in the free tier
  - ### 💲Paid Plans:
      - #### Basic: $11.99/month
          > - Monthly Requests: 50,000
          > - Features: Includes SSL encryption, currency module, time zone module, and connection module
      - #### Professional: $52.99/month
          > - Monthly Requests: 500,000
          > - Features: Adds bulk endpoint support
      - #### Professional Plus: $84.99/month
          > - Monthly Requests: 2,000,000
          > - Features: Includes all modules, including the security module
        
  > Note: Overage fees apply if you exceed your monthly quota. Notifications are sent at 75%, 90%, and 100% of     your quota usage.

  - ## numverify
      numverify provides a simple REST API for global phone number validation and lookup.
    - ### Free Plan:
         > - Monthly Requests: 100
         > - Features: Basic phone number validation
    - ### 💲Paid Plans:
      - #### Basic: $14.99/month
          > - Monthly Requests: 5,000
          > - Features: Includes carrier and line type detection
      - ### Professional: $59.99/month
          > - Monthly Requests: 50,000
          > - Features: Enhanced support and features
      - ### Enterprise: $129.99/month
          > - Monthly Requests: 250,000
          > - Features: Priority support and advanced features

  > Note: Overage fees apply if you exceed your monthly quota. Notifications are sent at 75%, 90%, and 100% of your quota usage.

## 🚀 Getting Started
### Clone the repository:
  ```bash
    git clone https://github.com/Raihan93-coder/IP-and-NUMBER_locator.git
    cd IP-and_NUM_locator
  ```
### Install dependencies:
  ```bash
    pip install requests -y
    pip install pyfiglet -y
    pip install dotenv -y
    pip install json -y
    pip install logging -y 
  ```
### Set up your API keys:
  - Create a .env file in the project root directory and add your API keys:
    ```env
    IPSTACK_API_KEY=your_ipstack_api_key
    NUMVERIFY_API_KEY=your_numverify_api_key
    ```
### Run the application:
  ```bash
    python3 main.py
  ```

