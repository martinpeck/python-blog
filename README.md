# Python Blog using Flask

This is a blog, written in Python, that uses the Flask web framework.

## Installation and Setup

1. Create a Python 3 virtual environment

    `python3 -m venv venv`

2. Activate the virtual environment

    `source venv/bin/activate`

3. Install Python packages

    `pip install -r requirements.txt`

4. Create the required database and tables by performing the DB migrations:

    `flask db upgrade`

    > Note: this will create an app.db file on your local machine, and use sqlite as a database engine.

5. [optional] Create a .env file and specify how you want flask to be run. For example, to run the local server in development mode:

    ``` env
    FLASK_ENV=development
    SECRET=some-secret-value-that-you-should-never-commit-to-git
    ```
    Other Flask environment variables can be found here:

    <http://flask.pocoo.org/docs/1.0/config/#builtin-configuration-values>

6. Start a local flask server

    `flask run`

    At this point, you should have a local running webserver, and should have seen something like the following in your terminal window:

    ``` shell
    $ flask run
    * Serving Flask app "microblog.py" (lazy loading)
    * Environment: development
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 123-456-789
    ```

7. Launch your browser, and open the url from the previous step

## License

Licensed under the MIT License.
See the file [LICENSE](LICENSE) for details