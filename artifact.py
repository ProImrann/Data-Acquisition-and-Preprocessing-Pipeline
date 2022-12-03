'''Data Acquisition and transformation pipeline'''
def movie_scraper():
    groups = ["top_100","top_250","top_1000","bottom_100","bottom_250","bottom_1000&groups=oscar_winner",
     "emmy_winner","golden_globe_winner","oscar_nominee","emmy_nominee","golden_globe_nominee","best_picture_winner",
     "best_director_winner","oscar_best_picture_nominees","oscar_best_director_nominees",
     "national_film_preservation_board_winner","razzie_winner","razzie_nominee"]
    f = dict(zip(groups, list(range(0,len(groups)))))
    from pprint import pprint
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd 
    print('Possible groups\n\n', pprint(f))
    group_index = int(input('Enter the category to scrape: '))
    num = int(input('Number of movies to scrape: '))
    group = groups[group_index]
    url = 'https://www.imdb.com/search/title/?count='+str(num)+'&groups='+group+'&sort=user_rating'

    def get_page_contents(url):
        page = requests.get(url, headers={"Accept-Language": "en-US"})
        return BeautifulSoup(page.text, "html.parser")
    try:
        soup = get_page_contents(url)
        #extract data elements
        movies = soup.findAll('div', class_='lister-item-content')
        titles = []
        released = []
        ratings = []
        runtime = []
        genres = []
        imdbs = []
        votes = []
        revenue = []
        for movie in movies:
            #Get movie names
            title = movie.find('a').text
            titles.append(title)
            #Get release date
            rel = movie.find('span', class_='lister-item-year text-muted unbold').text 
            released.append(rel)
            #ratings
            rating = movie.find('span', class_='certificate')
            ratings.append(rating)
            #runtime
            run = movie.find('span', class_='runtime').text
            runtime.append(run)
            #Genre
            gen = movie.find('span', class_='genre').text.strip()
            genres.append(gen)
            #IMDB rating
            rat = movie.find('div', 'inline-block ratings-imdb-rating', text_attribute=False).text.strip()
            imdbs.append(rat)
            #Votes
            vote = movie.find('span', {'name' : 'nv'}, text_attribute=False, order=None).text
            votes.append(vote)
            #Revenue generated
            rev = movie.find('span', {'name' : 'nv'},[1], text_attribute=False).text
            revenue.append(rev)

        movies_dict = {'Title': titles, 'Release date': released, 'Audience Rating': ratings,
                   'Runtime': runtime, 'Genre': genres,
                   'Votes': votes, 'Box Office Earnings': revenue, 'IMDB Rating': imdbs}
        movie_data = pd.DataFrame(movies_dict)
        #Data transformation
        #convert rating to a float
        movie_data['IMDB Rating'] = [float(item) for item in movie_data['IMDB Rating']]
        #convert votes to a int
        movie_data['Votes'] = [int(item.replace(",", "")) for item in movie_data['Votes']]
        movie_data['Box Office Earnings'] = [int(item.replace(",", "")) for item in movie_data['Box Office Earnings']]
        #sort by rating
        movie_data = movie_data.sort_values('IMDB Rating', ascending = False)
        #Brief analysis
        print('===============================================================================================================================')
        print("Number of extracted movies:", len(movie_data))
        print('\n\nBest movie (highest rating) in the selected category:', movie_data['Title'].head(1)[0])
        print("Rating:", movie_data['IMDB Rating'].head(1)[0])
        print("Revenue:", movie_data['Box Office Earnings'].head(1)[0])
        print('===============================================================================================================================')

        print("\nTop 10 movies by revenue:")
        display(movie_data.sort_values('Box Office Earnings', ascending = False).head(10))
        print('===============================================================================================================================')
        print("\nTop 10 movies by ratings:")
        display(movie_data.sort_values('IMDB Rating', ascending = False).head(10))
        print('===============================================================================================================================')
        #wsave data to a mysql database
        #movie_data.to_sql(con=con, name=groups[group_index], if_exists='replace', flavor='mysql')
    except:
        print("The selected category does not have any movies")
        return movie_data
        
data = movie_scraper()
