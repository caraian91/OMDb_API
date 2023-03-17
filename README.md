# OMDb API #

This API allows you to obtain movie information from IMDb.\
The API is available at `https://www.omdbapi.com/`

📚
Automated tests using API\
First checked in **Postman** ->
you can check in the file that was exported OMDb.postman_collection.json

📝\
Errors were also found when returning the status code.\
Send all data requests to: `http://www.omdbapi.com/?apikey=[yourkey]&` \
### Parameters
Please note while both "idMovie" and "tTitleMovie" are optional at least one argument is required.\
* **idMovie**	-> 
  * Required: Optional; 
  * Default Value: empty;
  * Description: (e.g. tt1285016);
* **tTitleMovie** -> 
  * Required: Optional; 
  * Default Value: empty;
  * Description: Movie title to search for.


📝 
Commands in **Cmd** or **Terminal** file for **API**\
Libraries to install:
* pip install requests
* pip install pytest

💡 
HTTP methods:\
**GET** -> we ask for data from the server - generally 200\
**POST** -> we send data to the server - generally 201\
**PATCH** -> we update data by updating certain attributes of the object (eg: from user only the first name) - 2xx\
**PUT** -> we update data by overwriting the entire object (eg: the entire user - firstname, lastname, address) - 2xx\
**DELETE** -> we delete data - generally 204

💡
CRUD stands for: **create**, **read**, **update** and **delete**




Happy Testing!



\
⏩
To import project\
git clone (put the link before clone from click on Code->copy link)

⏩
Troubleshoot:\
a. If it doesn't work with pip, try the command:  
* py -m pip install requests

b. In the last instance, you create a new project, install what you need with pip and manually copy the necessary folders and files. 
