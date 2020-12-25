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
   |  end_date | end date of the poll  |  
     
**/api/poll/<int:pk>/**
  *GET* Returns specific poll by ID.
  *POST* Updates the existed poll by ID
  
