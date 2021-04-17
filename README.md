# Blindfolded Puzzles backend
This is the backend repository for [blindfoldedpuzzles.xyz](https://blindfoldedpuzzles.xyz).

## Populate the database
To populate the database, first download the csv file at [database.lichess.org/#puzzles](https://database.lichess.org/#puzzles). Then run 
```
python manage.py populate <csv_filepath>
python manage.py setids
```

