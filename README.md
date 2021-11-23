# Information Retrival Project - Male crcketers Search App 

This is a repository which contain sourcode for male cricketers search engine create using elastic search and python.

## File Stucture

* Corpus
    * cricketers_En.txt : contain the data set in English language
    * cricketers_link.csv : contain the link of cricketers data
    * cricketers_Si.txt : contain the data set in Sinhala language
    * cricketers.json : contain the final data set
* template
    * search.html : contain the source code of UI
* app.py : Backend of the web app created using Flask
* createIndex.py : source code for create index
* scraper.py : Source code for the data scraper 
* search.py : elasticsearch quaries

## Starting the application

### Insalling elaticsearch 
You can install the elasticsearch locally.
After instll the elasticsearch, start elasticsearch cluster on port 9200

### Creating index

* Run ***createindex.py*** file to create index of the crickters

### Runing the web application

* Run ***app.py*** file and it will open the GUI window
* Enter the search query in the search box

## Data Fields

1. Name in English
2. Name in Sinhala
3. Full Name
4. Country
5. Date of Birth
6. Playing role
7. Bating style
8. Bowling style
9. Teams
10. Profile

## Data scrping process

In the scrapping process used BeautifulSoup library to scrap the data from HTML file. After srapping the data, It pass throught the text preproccing unit. To translate the data to englsh language used google translater API.After the post processing translated data create the final data set which in the cricketers.json file.

## Searching process

### Indaxing
For indexing the data  Elasticsearch is used and I have used the standard indexing methods provided in the Elasticsearch.

### Querying 
* Used two types of queries.
    * Multi-match queries
    * Wildcard queries
* In mutli-match queries search will done in more than one field. Before done the searching part it preprocesses using some replacement and this give the best search for the query.
* In wildcard query search will done for more than one fields and by giving uncomplete word and * it gives the best search.
* Aggregation was integrated with queries to get aggregated data with the search result.

### Advanced Features and Functionalities 

* Search can be done using any number of field like cricketer name, batting style, etc and the result shows the best match- පිතිකරුවන්, තිලකරත්න ඩිල්ෂාන්
* Search can be done using any number of fields like cricketer name, batting style, etc and the result shows the best match - බටහිර ඉන්දීය කොදෙව් වම්මත් පිතිකරු
* Search can be done for the phases. - ශ්‍රී ලංකා දකුණත් පිතිකරුවන්
* Cricketer’s name can be searched in both Sinhala and English – Dinesh Chandimal, දිනේෂ් චන්දිමාල්
* Search can be done like this ශ්‍රී ල* (wildcard queries)
