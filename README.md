# Lektion 3

# Deletion of __name__ - Why?

## Servlet Container
* Hosting of Application (locally)
* FastAPI introduces this new concept
* Removes traditional 'play/start' button
* Requires FastAPI - start command (to run app)

## Fast API
* Install: $ pip install "fastapi[standard]
* Verify installation through .venv package
    * 
    * BONUS: uv alternative for performance
    * BONUS: CONTROL + F (filter for 'Success')
    * 

## Endpoint
* API & URL related
* Consists of a path: "/example"
* Accompanied by an HHTP-Method (GET, POST, PUT, DELETE)

## Decorator
* Refers to the @ symbol
* Difference in how functions executes
* Runs logic from external decorator function
    * Function over function


## URL
Example URL: #
* In this example we see a dynamic parameter
    

## Pydantic
* Uses Schema to define Logical data type structure
* class based
* Is used for Data Validation
* Facilitates conversion of JSON -> Python objects
* Best practice - separated from its own package




# Lektion 5

# postgresql & fastapi

## installation
(Use uv if that's your relevant tech)
* `$ pip install "fastapi[standard]"`
* `$ pip install "psycopg[binary]"`
* `$ pip install "psycopg[pool]"`

# Run App
* `$ fastpi dev main.py`

## Storing data - philosophy

* What's the purpose of our data?
  * Bulk uploading
  * JSON data storage
  * Unorganized data
  * PostgreSQL database
* What's the datatype of said data?
  * Unorganized 
  * unstructured
  * Json

## Database - PostgreSQL
A newly created database does NOT contain any TABLES by default.

Step #1 - Create new Table (products)
```postgresql
CREATE TABLE IF NOT EXISTS products_raw (
id BIGSERIAL PRIMARY KEY,
created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
product JSONB NOT NULL
);
```

Step #2 - Implement function for Insert (fastAPI)

## TODO : Difference between: uvicorn vs fastapi dev main.py 