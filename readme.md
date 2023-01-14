# Flask Template
Minimal starter for simple Flask project.  

<br/>

## Specifications
- Python == 3.8

<br/>

## Setup
1. Install dependencies
   ```
   pip install -r requirements.txt
   ```

2. Run Flask  
   ```
   flask run
   ```

<br/>

## Additional Notes
- The environment is in .flaskenv
- The configuration is in config.py
- It has Pony ORM installed
- It has user models in app/auth/models.py


## Tips
- Flask have default directories, templates for html and static for css, js, images and etc.
- Flask has multiple libraries that support it like sqlalchemy, migration, forms, boostrap etc.
- Flask didn't restrict your choices, flask encourage developer preferences instead.
- As above said, you can combine Flask with different frameworks like VueJS.
- It is a good practice to split your application style and logic.
- Whenever you think your project is got bigger, consider using flask blueprint.