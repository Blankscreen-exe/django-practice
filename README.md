# My Django Practice

Here I'm trying all sorts of things `Django` and `Django Rest Framework`. 

- Each attempt at something new will be present as a separte "*django app*" and most of the related contents specific to that app will always be present within the app folder. 
- However, some customizations call for having changes to `settings.py` file or outside of the app folder in general, therefore those changes will be recorded in the `README.md` present in the app folder as well.
- Each app folder will be named with a prefix of `app_` to reduce ambiguity.
- Similarly, the main project folder will be named as `myPracticeSite`.
- `settings.py` file will be divided into separate components which will then be imported byt the `settings.py` itself. The sub  modules of django settings will be present inside the `config/` folder.
- for simplicity's sake, I have used `sqlite3` as a makeshift database, for simple apps. But might shift towards more practical databases like 