from csv import writer
from files_function import *
from function import *
import pandas as pd

count = 0
page = 1

file = 'texting.xlsx'

param = [
    [100000,    200000],    #Audi
    [250000,    300000],    #BMW
    [100000,    230000],    #Chery
    [1000000,   1200000],   #Exeed
    [200000,    220000],    #Ford
    [180000,    400000],    #Geely
    [200000,    500000],    #Hyundai
    [110000,    220000],    #Kia
    [0,         1000000],   #LandRover
    [300000,    500000],    #Mazda
    [1000000,    5000000],  #Mersedes-Benz
    [100000,    200000],    #Mitsubishi
    [200000,    250000],    #Nissan
    [200000,    800000],    #Renaut
    [400000,    500000],    #Skoda
    [255000,    720000],    #Toyota
    [500000,    1000000],   #Volkswagen
    [1000000,   3000000],   #Volvo
    [100000,    500000]     #Lada
]
i = 0
arr_counts = []
arr_marks = []
arr_min = []
arr_max = []
arr_ese = []

if __name__ == "__main__":
    response = html_response("https://drom.ru")
    soup = parse_soup(response.text)
    brends = search_class(soup, 'a', "css-1q66we5 e4ojbx43")


    for brend in brends:

        url = get_one_href(brend)
        brend_response = html_response(url)
        brend_soup = parse_soup(brend_response.text)
        marks = search_class(brend_soup, 'a', "css-1q66we5 e4ojbx43")

        for marka in marks:
            page_url = create_url_request(get_one_href(marka), page, param[i][0], param[i][1])
            marka_response = html_response(page_url)
            marka_soup = parse_soup(marka_response.text)
            
            search = marka_soup.find_all("a", "css-xb5nz8 ewrty961")
            
            while search != []:
                for s in search:
                    count += 1
                page += 1
                page_url = create_url_request(get_one_href(marka), page, param[i][0], param[i][1])
                marka_response = html_response(page_url)
                marka_soup = parse_soup(marka_response.text)
                search = None
                search = marka_soup.find_all("a", "css-xb5nz8 ewrty961")
            
            arr_counts.append(count)
            m = brend.text + " " + marka.text
            arr_marks.append(m)
            arr_min.append(param[i][0])
            arr_max.append(param[i][1])
            arr_ese.append('ЭСЕ {} с пробегом в ценовом диапазоне от {}р. до {}р.'.format(m, param[i][0], param[i][1]))

            print(brend.text)
            print(marka.text)
            print(count)
            count = 0
            page = 1
        i += 1


    data = pd.DataFrame({'ЭСЕ': arr_marks, 'Параметр' : arr_counts, 'Краткое словесное описание ИО' : arr_ese})
    data.to_excel(file)