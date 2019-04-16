## :godmode: Welcome To My Random Scripts :godmode:

These are some of my works, either answers to Stack Overflow or my own personal creations. :suspect:


### SQL
##### [postgres_master_everything_reset_script.sql](https://github.com/JayRizzo/Random_Scripts/blob/master/postgres_master_everything_reset_script.sql)

- This Script SETS / RESETS:
- [x] PERMISSIONS
- [x] CONSTRAINTS
- [x] PRIMARY KEYS
- [x] INDEXES OR INDICES
- [x] ADDED REINDEX ON THE DATABASE
- [x] REORDERED THE QUERIES USING THE ORDER BY REPLACE THIS IS MANDITORY

SQL Reset Script that is Dynamic & Static that builds queries that are designed to Standardize Permissions & Improve Performance.  This is highly customizable and effective in making sure your database permissions do not get in the way when dealing with mulitiple users & or Groups with multi standardized structures.

### PHP
##### [shopify_to_csv.php](https://github.com/JayRizzo/Random_Scripts/blob/master/shopify_to_csv.php)
This Module was Built to Clean your data upon import Converting all Symbols (ASCII) to HTML References to help prevent issues when trying to create a clean "Encapsulated","CSV","FILE"

1. This module uses the following
  1. Mandatory
    1. shopify_key
    1. shopify_password
    1. shopify_store 
  1. Optional
    1. shopify_collection_id

Script Ability:

- [x] Download your Shopify Store Product Data in a "Clean","Data Set"
- [x] Download your Shopify Store Product Variant Data in a "Clean","Data Set"
- [x] Clean the imported data from data that may crash the `bash`, `PHP` or importing your data into `sql`. as the symbols have been converted to HTML References __&trade;__ turns into `&trade;`
- [x] Can be used for `CRONJOBS`
- [x] Has custom restrictions with proper notificiations
- [x] Can be used to notify you for failures &/ Sucesses if desired & customized

Script Note:

- [x] This is a Personal Creation of this Monstrosity

##### [html_ascii_to_html.php](https://github.com/JayRizzo/Random_Scripts/blob/master/html_ascii_to_html.php)
This Module is a subset of the __shopify_to_csv.php__


### Python
#####  [char_to_html.py](https://github.com/JayRizzo/Random_Scripts/blob/master/char_to_html.py)
Is a version of replacing non-ASCII characters with printable ASCII & Using HTML entities when possible.

#####  [custom_header.py](https://github.com/JayRizzo/Random_Scripts/blob/master/custom_header.py)
This Module was Built to showcase Examples Of Custom Headers, printing upon execution of your script.
* Answer to Stack Overflow Question: [Python: What is a header?](https://stackoverflow.com/a/51914806/1896134)

#####  [FizzBuzz.py](https://github.com/JayRizzo/Random_Scripts/blob/master/FizzBuzz.py)
Is my Python Version of fizzbuzz I wrote myself for fun.

#####  [organize_files.py](https://github.com/JayRizzo/Random_Scripts/blob/master/organize_files.py)
The Module Has Been Build for keeping your files organized by specific file types.
* Answer to Stack Overflow Question: [Moving specific file types with Python](https://stackoverflow.com/a/50344578/1896134)

#####  [pyodbc_mssqldbtest.py](https://github.com/JayRizzo/Random_Scripts/blob/master/pyodbc_mssqldbtest.py)
The Module Has Been Build for Interaction with MSSQL DBs To Test the console for `pyodbc`.
* Answer to Stack Overflow Question: [Connect Python with SQL Server Database](https://stackoverflow.com/a/51627907/1896134)

#####  [regex_match.py](https://github.com/JayRizzo/Random_Scripts/blob/master/regex_match.py)
The Module Has Been Build for trying to find variations of emails in batches of text.

#####  [relativedelta.py](https://github.com/JayRizzo/Random_Scripts/blob/master/relativedelta.py)
The Module Has Been Build for trying to decipyer measurements between dates. The Stack Overflow User was dealing with arbitrary dates, so my answer was not acceptible.
* Was an __attempt__ to Answer a Stack Overflow Question: [Calculating number of years between two dates, but rounded in the standard way](https://stackoverflow.com/q/52290952/1896134)

#####  [sendgmail.py](https://github.com/JayRizzo/Random_Scripts/blob/master/sendgmail.py)
The Python Module Has Been Build for Sending Emails from your Gmail Account, bypassing the 2FA.
* Answer to Stack Overflow Question: [How to send an email with Gmail as provider using Python?](https://stackoverflow.com/a/51664129/1896134)

#####  [testy_class_init.py](https://github.com/JayRizzo/Random_Scripts/blob/master/testy_class_init.py)
The Module Has Been Build to help a user fix their code.
* Answer to Stack Overflow Question: [AttributeError: 'str' object has no attribute 'name' while defining a class & calling it](https://stackoverflow.com/a/52360707/1896134)

##### [uuid_testing.py](https://github.com/JayRizzo/Random_Scripts/blob/master/uuid_testing.py)
A fix
> "for attempting to read in CSV data and map it to the following XML structure".
* Answer to Stack Overflow Question: [Python string formatting and UUID](https://stackoverflow.com/a/52290812/1896134)

### Shell
##### [clean_mac.sh](https://github.com/JayRizzo/Random_Scripts/blob/master/clean_mac.sh)
This Module was Built to Clean your ~/Documents Folder from any "Truly" empty folders that may only contain some hidden/ZERO byte files.
* Answer to Stack Overflow Question: [How can I delete empty folders in Mac OS X?](https://superuser.com/a/1322425/247728)

:godmode: Thank You For Visiting! :godmode:
