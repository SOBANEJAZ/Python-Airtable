# Airtable CRUD Operations

This project demonstrates basic Create, Read, and Update (CRUD) operations with [Airtable](https://airtable.com/) using the Python library `pyairtable`. The script uses environment variables to store API credentials and defines functions to interact with Airtable.

## Features

- **Create Record**: Add a new record to a specified Airtable table.
- **Get Record**: Fetch records from a table based on filter conditions.
- **Update Record**: Update an existing record in a table.

## Prerequisites

Make sure you have the following set up before using this code:

- An Airtable account and an API token.
- The base ID of your Airtable project.
- A table with which you want to interact.

## Installation

1. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    ./venv/bin/activate  # On Mac and Linux Systems use `source venv/bin/activate`
    cd venv
    ```

2. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/airtable-crud.git
    cd airtable-crud
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. add your Airtable API key and Base ID in `.env` file :

    ```bash
    AIRTABLE_TOKEN=your_airtable_token
    BASE_ID=your_base_id
    ```
