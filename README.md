# Student Management REST API

A RESTful backend API built using **Flask** and **SQLite** to manage student records.  
This project follows **REST principles**, implements CRUD operations, and uses a **clean layered architecture** for maintainability and scalability.

---

## Features

- Add a new student  
- Retrieve all students  
- Retrieve a student by ID  
- Delete a student  
- Input validation with meaningful error messages  
- Proper HTTP status codes and global error handling  

---

## Tech Stack

- **Backend:** Python, Flask  
- **Database:** SQLite  
- **API Style:** REST  
- **Tools:** Git, GitHub, Postman / Thunder Client  

---

##  API Endpoints

| Method | Endpoint       | Description          |
|--------|----------------|----------------------|
| POST   | /students      | Add a new student    |
| GET    | /students      | Get all students     |
| GET    | /students/<id> | Get student by ID    |
| DELETE | /students/<id> | Delete student by ID |

---

## API Testing

All endpoints were tested using **Postman** and **Thunder Client** to ensure:
- Correct request validation  
- Proper HTTP status codes  
- Consistent JSON responses  
- Reliable error handling  

---

## Key Learnings

- Building RESTful APIs using Flask  
- Designing clean layered backend architecture  
- Working with SQLite and parameterized SQL queries  
- Handling errors using proper HTTP status codes  
- Testing APIs using Postman / Thunder Client  

---

## Future Improvements

- Update student details (PUT / PATCH)  
- Pagination and filtering  
- Authentication and authorization  

---
