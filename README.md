## Data-Acquisition-and-Preprocessing-Pipeline

The  pipeline  design  involved  three  main  processes  including  data  scraping,  data processing and data analysis. 

#### Data acquisition Data  acquisition

involves  using  select  techniques  in  Beautifulsoup and  Requests  to extract data from the target repository. In this step, data is collected from the imdb repository and stored locally as a list using the movie_scraper function.

The scraper function contains a helper function get_html_data which parses the supplied https://www.imdb.com/ URL. Ideally, the objective is to extract information such  as  Title,  Release  date,  Audience  Rating,  Runtime,  Genre,  Votes,  Box  Office Earnings,  and  IMDB  Rating  from  movies.  Each  of  these  elements  is  subsequently extracted from the soup element that was obtained from get_html_data:

![image](https://user-images.githubusercontent.com/118980393/205435605-04462569-7a2f-4eb4-943e-7849e9fdd9b1.png)

### User Interaction 

The movie_scraper function allows a user to supply two inputs, i.e., the movie group and number of movies to scrape. All the available groups are presented to the user from which the index of the desired movie group is selected. The available movie groups include top 100, top 250, top 1000, bottom 100, bottom 250, bottom 1000, oscar winner, emmy  winner,  golden  globe  winner,  oscar  nominee,  emmy  nominee,  golden  globe nominee, best picture winner, best director winner, oscar best picture nominees, oscar  best director nominees, national film preservation board winner, razzie winner, and razzie nominee.

![image](https://user-images.githubusercontent.com/118980393/205435774-a7579c04-6fdc-4e6b-9c96-d6f7c71dfb0e.png)

