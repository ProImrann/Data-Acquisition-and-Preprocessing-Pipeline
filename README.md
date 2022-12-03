## Data-Acquisition-and-Preprocessing-Pipeline

The  pipeline  design  involved  three  main  processes  including  data  scraping,  data processing and data analysis. 

#### Data acquisition Data  acquisition

involves  using  select  techniques  in  Beautifulsoup and  Requests  to extract data from the target repository. In this step, data is collected from the imdb repository and stored locally as a list using the movie_scraper function.

The scraper function contains a helper function get_html_data which parses the supplied https://www.imdb.com/ URL. Ideally, the objective is to extract information such  as  Title,  Release  date,  Audience  Rating,  Runtime,  Genre,  Votes,  Box  Office Earnings,  and  IMDB  Rating  from  movies.  Each  of  these  elements  is  subsequently extracted from the soup element that was obtained from get_html_data:

![image](https://user-images.githubusercontent.com/118980393/205435532-50f83d2a-695c-4f9b-96ca-a931f09ce780.png)
