# Data Collector
#### The Data Collector is a Python class designed to generate sample data and provide methods for retrieving user data based on certain criteria. This code is particularly useful for scenarios where random sample data is needed for testing or simulation purposes.
##
## Features
### Random Data Generation: 
#### The generate_sample_data method generates random sample data for a specified number of records. It includes randomly generated usernames, passwords, birthdates, addresses, SSNs (Social Security Numbers), product purchases, and salesperson IDs.
### Data Retrieval: 
#### The class provides methods for retrieving user data based on state and salesperson. The get_user_by_state method allows users to retrieve data based on the state in which they reside, while the get_user_by_salesperson method retrieves data based on the salesperson handling the user.
##
## Usage
#### 1. Import the DataCollector class into your Python script.
#### 2. Instantiate the DataCollector class.
#### 3. Use the generate_sample_data method to generate the desired number of sample records.
#### 4. Utilize the provided methods (get_user_by_state and get_user_by_salesperson) to retrieve user data based on specific criteria.
##
## Requirements
#### Python 3
