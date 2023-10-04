# CMPE272_Project
Your team works for a company that wants to create an enterprise HR Portal application.
Your manager has provided a backup of the company’s enterprise database
and asks that you use it to demonstrate a Proof of Concept application 
- company's enterprise database link: [https://github.com/datacharmer/test_db](https://github.com/datacharmer/test_db)
## including:
- Single Sign on (SSO) / AD authentication with SSL/TLS encryption
- Application / Web portal for viewing/browsing (sample) enterprise employee data (with SSO roles)
- Github (or other repo) integrated into SSO (optional)
- Jenkins, integrated into SSO and Github repo;
- Additional integrations / features / capabilities for higher grade (layered security, social media integration, document repository, Salesforce integration, etc..)
## Project Deliverables:
- Project Plan in .docx format. There’s a template in Canvas, or you can make your own
- Project Presentation in .pptx format
- Project Report: .docx format, including design patterns, diagrams, use/test cases, screenshots, etc. There is a template in Canvas
- 15 minute live project presentation, where each team member MUST present/speak for a portion
- Code (checked into github , with references in Project Report: [https://github.com/sjsu-cmpe272](https://github.com/sjsu-cmpe272)
## Sample project provided by prof: [https://github.com/sjsu-cmpe282/the-elite](https://github.com/sjsu-cmpe282/the-elite)

## Backend Project Layout
```
backend/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   ├── index.html
│   ├── static/
│   │   ├── css/
│   │   ├── img/
├── requirements.txt
├── app.py
```

## How to run our Python Flask Back-end:
- Make sure you installed your interpreter with a virtual environment '<your path>\teamproject-team-alpha-1\Backend' (venv)
```
python -m venv myenv
```
- make sure the path is '<your path>\teamproject-team-alpha-1\Backend', activate your venv first with this command:
```
venv\Scripts\activate
```
- then run:
```
 pip install -r requirements.txt
```
- Now you can start your backend locally with:
```
python app.py
```
- when you finsih the session of programming. deactivate the virtual environemnt:
```
deactivate
```
#### Useful commands for backend:
- when you installed some library in your virtual environment, and you want to include it into requirements.txt. this command automatically detects the library or dependencies in your environment and add it to requirements.txt
```
pip freeze > requirements.txt
```

## Frontend Project Layout
```
myapp/
├── public/
│   ├── index.html
│   ├── favicon.ico
├── src/
│   ├── index.js
│   ├── App.js
│   ├── components/
│   │   ├── Header.js
│   ├── pages/
│   │   ├── Home.js
│   │   ├── Auth/
│   │   │   ├──log-in.js
│   │   │   ├──sign-up.js
│   ├── index.js
├── package.json
├── package-lock.json
├── README.md
```
  
#### How to run our React Front-end:
- install node.js. https://nodejs.org/en
- after installation of node.js. run the following command to install the dependencies and neccessary files for this project.
```
npm install
```
- Now you can start your frontend locally with:
```
npm start
``` 
## Front-end routing

## How to run our React Front-end:
- install node.js. https://nodejs.org/en
- after installation of node.js. run the following command to install the dependencies and neccessary files for this project.
```
npm install
```
- Now you can start your frontend locally with:
```
npm start
``` 

