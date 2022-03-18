# NationalIDValidator

## Steps to run the Validator API
1. After cloning the repository, lets create and activate a virtual environment in order to install libraries and packages **safely**:
   - First install Python virtual environment, if not already installed, using command: `pip install virtualenv`.
   - Lets create our virtual environment using `python -m venv env`  
3. To safely download requirements, use terminal and execute the following commands in the NationalIDValidator-Shahry directory:
   - Activate virtual environment using `env\Scripts\activate`. If activated correctly, a bracket including environment name will appear in the right most part.
   - Install requirements using: `pip install -r requirements.txt`

4. Last step is to run the localserver and test the endpoint using the following commands:
   - `cd IDValidator`
   - python manage.py runserver


### Testing the endpoint
In order to test the endpoint we can either use **Postman** or make use of **Django restframework developer tools**.
#### Postman testing
1. After installing Postman, import the [Query](https://github.com/adhamhassan99/NationalIDValidator/blob/master/Shahry%20test.postman_collection.json) included in this repo
2. After importing the query file, one can send requests right away as long as local server is running according to step 4 in the previous section.
   - ![Query Example](https://github.com/adhamhassan99/NationalIDValidator/blob/4af4f98c37c96c6966fb7eb5b774b26c0348f074/Screenshot%20(204).png)

#### Browser Testing
Run the local server as guided in step 4 in the first section then:
1. open browser and visit the endpoint `http://127.0.0.1:8000/home/`
2. In the *Content* box insert json data as follows `{"ID":29001011234567}`
3. Click post and the API should display returned value in the following format: `{
    "Gender": "Female",
    "Birth_Place": "Dakahlia",
    "Birth_Date": "1990-01-01"
}`


