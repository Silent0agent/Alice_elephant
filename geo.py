import requests


def get_country_by_city_name(city_name):
    try:
        url = "https://geocode-maps.yandex.ru/1.x/"
        params = {
            "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
            'geocode': city_name,
            'format': 'json'
        }
        data = requests.get(url, params).json()
        # все отличие тут, мы получаем имя страны
        return data['response']['GeoObjectCollection'][
            'featureMember'][0]['GeoObject']['metaDataProperty'][
            'GeocoderMetaData']['AddressDetails']['Country']['CountryName']
    except Exception as e:
        return e