# Spider

## SimpleSpider
### Introduction
This is the simplest version of a spider in python. It request for the html and use the re module to search for the item wanted. Then, it downloads all the items. 

### Requirements
Python 3.6 and modules urllib & re

### How to use
Firstly, fill in the "" with the source page url. 
    i = img_list("") # source page
Then, find and fill in the expression for the item in the html file of the page
    reg = r'' # how to recognize the items
Finally, change the way to save the files as you want
    with open("%d" % n, "wb") as f: # filename
