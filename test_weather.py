import pytest
import requests
#Метод, который возвращает координаты города по названию
def get_object_coordinates(object_address):
    params = {"q":object_address, "format":"geojson"}
    response = requests.get("https://nominatim.openstreetmap.org/search",
                        headers={"User-Agent":"PostmanRuntime/7.37.3", "Accept":"*/*"},
                        params=params).json() #Открытый API для получения координат по названию
    return response["features"][0]["geometry"]["coordinates"]
#Входные параметры - название города и ожидамое значение температуры в нем
@pytest.mark.parametrize("city, true_temp", [("Наро-Фоминск", 24), ("Paris, France", 16)])
def test_get_weather(city,true_temp):
    coordinates = get_object_coordinates(city)
    params = {"lat":coordinates[1],"lon":coordinates[0],"lang":"ru_RU"}
    response = requests.get("https://api.weather.yandex.ru/v2/informers",
                            headers = {"User-Agent":"PostmanRuntime/7.37.3",
                                       "Accept":"*/*",
                                       "X-Yandex-API-Key":"----------"
                                       }, # Запрос к Яндекс Погода с координатами города для получения температуры воздухарп
                            params = params).json()
    temp_now = response["fact"]["temp"]
    assert temp_now == true_temp

