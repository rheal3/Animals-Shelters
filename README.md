Website shows info about animal shelters
shelters -> id, name, email, phone, address, city
animals -> id, name, kind, breed, age

1 shelter many animals
1 animal 1 shelter
== 1 to many


MVC
1. models
    - database info
        - what columns are in the table 
        - what data type for each column
    - imports db from main
2. controllers
    - routes to get different info
    - imports blueprint for each (url_prefix)
    - imports schema, db, & model
3. schemas
    - used to turn data into json
    - imports marshmallow & model

