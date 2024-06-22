from bs4 import BeautifulSoup
import requests



def get_info_films(name_film: str, data_dict: dict, list_names_films: list):
    URL = 'https://www.kinoafisha.info/search/'
    data_test = {'q': name_film}
    site = requests.get(URL, params=data_test)
    soup = BeautifulSoup(site.text, 'lxml')
    films = soup.find_all('div', class_='shortList_content')
    number = 1

    for film_element in films:
        film_name = film_element.find('span', class_='shortList_name')
        film_info = film_name.find_next()
        film_info2 = film_info.find_next()
        if film_name.text not in list_names_films:
            list_names_films.append(film_name.text)
            data_dict[film_name.text] = [film_name.text, film_info.text, film_info2.text] 
        else:
            list_names_films.append(f'{film_name.text}_{number}')
            new_film_name = f'{film_name.text}_{number}'
            number+=1
            data_dict[new_film_name] = [film_name.text, film_info.text, film_info2.text] 