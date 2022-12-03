## Data-Acquisition-and-Preprocessing-Pipeline

The  pipeline  design  involved  three  main  processes  including  data  scraping,  data processing and data analysis. 

#### Data acquisition 
Data  acquisition involves  using  select  techniques  in  Beautifulsoup and  Requests  to extract data from the target repository. In this step, data is collected from the imdb repository and stored locally as a list using the movie_scraper function.

The scraper function contains a helper function get_html_data which parses the supplied https://www.imdb.com/ URL. Ideally, the objective is to extract information such  as  Title,  Release  date,  Audience  Rating,  Runtime,  Genre,  Votes,  Box  Office Earnings,  and  IMDB  Rating  from  movies.  Each  of  these  elements  is  subsequently extracted from the soup element that was obtained from get_page_contents:

![image](https://user-images.githubusercontent.com/118980393/205435605-04462569-7a2f-4eb4-943e-7849e9fdd9b1.png)

### User Interaction 

The movie_scraper function allows a user to supply two inputs, i.e., the movie group and number of movies to scrape. All the available groups are presented to the user from which the index of the desired movie group is selected. The available movie groups include top 100, top 250, top 1000, bottom 100, bottom 250, bottom 1000, oscar winner, emmy  winner,  golden  globe  winner,  oscar  nominee,  emmy  nominee,  golden  globe nominee, best picture winner, best director winner, oscar best picture nominees, oscar  best director nominees, national film preservation board winner, razzie winner, and razzie nominee.

![image](https://user-images.githubusercontent.com/118980393/205435839-e2551c3d-b007-48ab-ac7d-e7d3ab56a6fb.png)

### Data Scraping
After obtaining the user input, a url is specified which incorporates the user input as paramaters for the group and count of items to be scrapped.

![image](https://user-images.githubusercontent.com/118980393/205435893-b4e16601-7c79-4d72-9bf4-73832fdecb22.png)

The resulting URL is passed to the get_page_contents(url) function which returns a soup element. Data from the soup element is then saved into separate lists.

![image](https://user-images.githubusercontent.com/118980393/205436073-c8b1e0c7-3b51-4c6b-9f8e-0f9948ec1dd4.png)

### Data Storage
The collected data is transformed into the correct data types:
![image](https://user-images.githubusercontent.com/118980393/205436208-8ba1bf2f-2b9a-4e6b-8a42-764f33717372.png)

### Data Analysis

The  last  component  of  the  pipeline  is  analysis  which  involved  generating  general information regarding the data that was acquired. The information include: i. Best movie (highest rating) in the selected category
ii. Rating of the movie
iii. Revenue by the movie
iv. Top 10 movies by revenue
v. Top 10 movies by ratings

The figure below shows a sample overview of the output of data scraping, processing, and analysis.

![image](https://user-images.githubusercontent.com/118980393/205436279-faf84214-7014-46d0-8b53-1a1c9bfed1d7.png)


