# BeyondChats Assignment 

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Run](#run)
- [Configuration](#configuration)
- [Contact](#contact)

## Introduction

API endpoint: https://devapi.beyondchats.com/api/get_message_with_sources

Above is a paginated GET API which returns an array of objects where each object contains a response text and a corresponding array of sources. Source is a JSON array. Each object of the array consists of an id, context, and an optional link.

Your task is to develop a Python program that does the following:

- Fetch the data from the pages of the API above.
- Identify whether the response for each response-sources pair came from any of the sources.
- List down the sources from which the response was formed. Returns an empty array if the response did not come from any source. The shortlisted sources will be called citations.
- Return the citations for all objects coming from the API. 
- Extra points if you can present your solution through a user-friendly UI.

## Prerequisites

efore running this project, ensure you have Python and pip installed on your system. You'll also need to create a virtual environment to install the required libraries. Follow these steps to set up your environment:

1. **Install Python**: If you don't have Python installed, download and install it from the [official Python website](https://www.python.org/).

2. **Create a Virtual Environment**: Open a terminal or command prompt and navigate to your project directory. Then, run the following commands to create a virtual environment named `venv`:

    ```bash
    python -m venv venv
    ```

    This will create a folder named `venv` in your project directory containing the virtual environment.

3. **Activate the Virtual Environment**: Activate the virtual environment by running the appropriate command for your operating system:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

    Once activated, your command prompt or terminal should show the name of the virtual environment (`(venv)` for example).

4. **Install Dependencies**: With the virtual environment activated, install the required libraries using the following command:

    ```bash
    pip install -r requirements.txt
    ```

    This will install all the necessary dependencies for the project within the virtual environment.

Now, you're ready to run the project in the virtual environment!


## Run

2. Navigate to the project directory:

    ```bash
    cd project_directory
    ```

3. Install dependencies:

    ```bash
    python main.py
    ```
## Screenshot

![Screenshot](https://github.com/SarkarPriyanshu/BeyChatsAssignment/blob/main/Screenshot%202024-05-18%20154755.png)

## Contact

- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/priyanshu-sarkars-d07m08y1995/)
- GitHub: [Your GitHub Profile](https://github.com/SarkarPriyanshu)
- CodeSandbox: [Your CodeSandbox Profile](https://codesandbox.io/u/SarkarPriyanshu)
