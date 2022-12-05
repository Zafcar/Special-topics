## Scheduler folder
### There are 3 main parts in the scheduler that we are using to schedule the mail, the timing, and the excel sheet of data.

* Excel Creator-  Creates excel sheet using the library `xlsxwriter`. It uses the `rangefilter` library from the admin.py to extract the data from the database. There are multiple columns that will store the data in an ordered manner in the excel sheet.

* Job Scheduler- It schedules a job to run at a particular time. We create a trigger time for the job to run the APIs at that particular time. We have used `apscheduler` for scheduling, `excel_creator.py` and `mail_creator.py` to generate the excel sheet and the template mail to attach the files with it.

* Mail Creator- Automatically sends emails to the provided address including attachments. We have used `smtplib` and `email.mime` to connect to the email servers and generate the mail and to include the attachments with it. The service requires both the sender's email address and passcode as well as the receiver's email address. The sender's email provider must be configured with "less secure app access" so that the libraries can send the email through the provided address.

## Special Topic folder

* admin.py - It basically stores all the models of the website, database and its workings. `rangefiler` library is used to filter the data based on date of creation. It displays all the student information and lists them out orderly. A resource model (class- `System_databaseResource`) is created for the ease of creating an excel sheet(using `excel_creator.py`) of data from the `System_database`.

#### Will be updating this file as things are progressed.
