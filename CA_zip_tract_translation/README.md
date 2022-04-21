# Zip to tract and vice versa translation

this folder contains two files, each with a single dictionary.

to save these as variables in a notebook, import with json. You'll have to change `file_path` first.
```python
import json

file_path = '../path/to/CA_zip_tract_translation/'

tract_to_zip_filepath = file_path + 'tract_to_zip.json'
with open (tract_to_zip_dict_filepath, 'r') as my_ttz_file:
    tract_to_zip = json.load(my_ttz_file)

zip_to_tract_filepath = file_path + 'zip_to_tract.json'
with open (zip_to_tract_filepath, 'r') as my_ztt_file:
    zip_to_tract = json.load(my_ztt_file)
```


tract_to_zip.json holds a dictionary with census tracts (from CAES 3 and 4) for keys and their encompassing zip codes as values. Use it to find the zip code a census tract is in.
```python
>>> tract_to_zip['6037141700']
'90210'
```

zip_to_tract.json holds a dictionary with zip codes as keys and a list of their contained census tracts as values. Use it to find the census tracts when you know the zip code.
```python
>>> zip_to_tract['90210']
[[6037700801,
   6037700700,
   6037141700,
   6037261101,
   6037700600,
   6037261102]]
```

you won't be able to take values directly out of the dataframes and put them in as keys, since they're integers. cast as a string if you want to use them in the dict.
```python
>>> this_zip_code = str(90210)
>>> zip_to_tract[this_zip_code]
[[6037700801,
   6037700700,
   6037141700,
   6037261101,
   6037700600,
   6037261102]]
```

cast as ints if you need them in the same form they come in a dataframe.
```python
>>> int('90210')
90210
```