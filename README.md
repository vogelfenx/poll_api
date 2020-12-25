# poll_api first steps & testing
1. Clone the repository 
`git clone https://github.com/vogelfenx/poll_api.git`

2. Go to the cloned project directory and run the `devenv_setup.bat` Script

3. run the dev server: `runserver.bat`

# Testing
Use pre-defined postman collections (postman/api-collection.json) to test the api.

# Api endpoints

**/api/poll/**

  *GET* Lists all polls if the request.user is admin, otherwise returns only active polls  
  
  *POST* Adds new poll if the user is authenticated & admin   
     
  **required body parameters**: 
   | Param  | desc  |
   |--------|-------|
   | title  | title of the poll, max 100 charachters  |
   |  description | description of the poll, max 500 charachters  |
   |  end_date | end date of the poll, use YYYY-MM-DDThh:mm  |  
     
**/api/poll/<int:pk>/**  
  *GET* Returns specific poll by ID.  
  
  *PUT* Updates the existed poll by ID
  
  **required body parameters**: 
   | Param  | desc  |
   |--------|-------|
   | title  | title of the poll, max 100 charachters  |
   |  description | description of the poll, max 500 charachters  |
   |  end_date | end date of the poll, use YYYY-MM-DDThh:mm  |

**api/poll/list_user_polls_detail/**  
   *GET* Returns polls with selected choiches by the user  
   
**api/question/**
   *GET* Returns questions.  
   
   *POST* Adds new question.
   
  **required body parameters**: 
   | Param  | desc  |
   |--------|-------|
   | poll_id  | the poll the question refers  |
   |  question_type | Type of the question, possible int values: `1` for Text, `2` for one_choice, `3` for multi_choice question  |
   |  question | question text  |  
   

**api/question/<int:pk>**  
   *GET* Returns specific question by ID.  
   
   *PUT* Updates new question by ID.
   
  **required body parameters**: 
   | Param  | desc  |
   |--------|-------|
   | poll_id  | the poll the question refers  |
   |  question_type | Type of the question, possible int values: `1` for Text, `2` for one_choice, `3` for multi_choice question  |
   |  question | question text  |  
   
**/api/answer/**

  *GET* Lists all question's answers 
  
  *POST* Adds answers to the question  
     
  **required body parameters**: 
   | Param  | desc  |
   |--------|-------|
   | answer  | text of answer  |
   |  question_id | the question the answer refers  |  
   
**/api/answer/<int:pk>**

  *GET* Returns specific answer 
  
  *PUT* Updates answer on the question  
     
  **required body parameters**: 
   | Param  | desc  |
   |--------|-------|
   | answer  | text of answer  |
   |  question_id | the question the answer refers  |  
   
   
