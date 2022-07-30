# Task

We will be displaying our shiny new pokemons on our website!

## Setup

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Django-M4-Views-and-URLs).
2. Create a `virtual environment` and activate it.
3. Install the requirements using `pip install -r dev-requirements.txt`.
4. Run migrations using `python manage.py migrate`.
5. Create an admin user using `python manage createsuperuser`.
6. Run the server using `python manage.py runserver`.
7. Go to the admin panel and create several pokemons.

## Detail View

1. Go to `views.py` and create a detail view for your pokemons.
   - Call the function `get_pokemon`.
   - The function will receive a `request` and a `pokemon_id`, and return an `HttpResponse`.
   - The function should use the `pokemon_id` received from the parameters to fetch the `Pokemon` from the database.
   - The `HttpResponse` should contain a [multi-line](https://www.programiz.com/python-programming/examples/multiline-string) string, which is also an [f-string](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python), which displays the details of our pokemon.
2. Go to `urls.py` and create a path for our pokemon detail view.
   - Import our `get_pokemon` view.
   - Add a `path` that starts with `pokemons/` and contains an id in it.
3. Go to `/pokemons/YOUR_ID/` on your web browser and verify that you can see your pokemon.
4. Commit and push your code.

## Detail Bonus

Make each line of your pokemon details show up as a separate line on the web browser (hint: use [`p` tags](https://www.w3schools.com/tags/tag_p.asp)).

## List View

1. Go to `views.py` and create a list view for all our pokemons.
   - Call the function `get_pokemons`.
   - The function will receive a `request` and return an `HttpResponse`.
   - The `HttpResponse` should contain a [joined](https://www.programiz.com/python-programming/methods/string/join) list of strings (separated by a new line) that displays the names of **all** our pokemons.
2. Go to `urls.py` and create a path for our pokemon detail view.
   - Import our `get_pokemons` view.
   - Add a `pokemons/` _`path`_.
3. Go to `pokemons/` and verify that you can see all of your pokemons.
4. Commit and push your code.

## List Bonus

1. Have each pokemon separated on your web browser by a new line (hint: use a [`ul` tag](https://www.w3schools.com/tags/tag_ul.asp) with `li` tags).
2. Link your list of pokemons to their respective detail pages.
