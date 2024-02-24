# Export Kindle Clippings

This is a simple programm to exporte Kindle Clippings from the file `My Clippings.txt` to a directory.  
It's very useful for those who read external file from amazon library.

the programm has these feature:

- Will be created a single file for every single books read
- Duplicate note will not be copied
- File could be modify without be overwritten

## Parameters
_DestinationPath_ = Path to the directory where you want to generate the books files
_MyClippingPath_  = Path to the file `My Clippings.txt`
_toIgnore_        = List of titles to ignore 
_dizMonths_       = Diz of months to convert written date in numerical date to confront date notes, now it's in italian. For some one could be useful translate it in english or other leanguages

## Features
### Files of book
The structure of the kindle highlights file is 

```
﻿{{title}} ({{author}})
- {{metadata}}
{{content}}
==========
```

This program make a file  for every title found in the file and append the notes to that

### Duplicate note
If the content of a note is inside in the content of the nextone (or viceversa) only the latest one will keept. This is made because if you modify an already taken note on kindle it doesn't remove the old one but just add the newer.

### Modify a file
You could modify a file, for example delete a note or add a comment, and it will not be overwritten the next time you run the programm. This is very useful if you had to modify the structure. For example if you use this inside an app like Obsidian you'd like to append link in a file.

To do this the progra use an hidden file with the date of the last note append. The file will be created in the destination directory if doesn't found and it's named `.support.txt`
