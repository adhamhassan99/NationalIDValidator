# NationalIDValidator

## Steps to run the Validator API
1. After cloning the repository, lets create and activate a virtual environment in order to install libraries and packages safely:
   - First install Python virtual environment, if not already installed, using command: `pip install virtualenv`.
   - Lets create our virtual environment using `python -m venv env`  
3. To safely download requirements, use terminal and execute the following commands in the NationalIDValidator-Shahry directory:
   - Activate virtual environment using `env\Scripts\activate`. If activated correctly, a bracket including environment name will appear in the right most part.
   - Install requirements using: `pip install -r requirements.txt`

4. Last step is to run the localserver and test the endpoint using the following command:
   - python manage.py runserver


### Testing the endpoint
In order to test the endpoint we can either use postman or make use of django restframework developer tools.
#### Postman testing
1. After installing Postman, import the [Query](./q) included in this repo

