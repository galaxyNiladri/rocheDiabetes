import pytest
from httpx import AsyncClient
from main import *


@pytest.mark.anyio
async def test_base():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to FizzBuzz!"


@pytest.mark.anyio
async def test_fuzzbizz1():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/fizzbuzz?int1=3&int2=5&limit=100&str1=fizz&str2=buzz")
    assert response.status_code == 200
    assert response.json() == [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz",
                               16, 17, "fizz", 19,
                               "buzz", "fizz", 22, 23, "fizz", "buzz", 26, "fizz", 28, 29, "fizzbuzz", 31, 32, "fizz",
                               34, "buzz", "fizz", 37,
                               38, "fizz", "buzz", 41, "fizz", 43, 44, "fizzbuzz", 46, 47, "fizz", 49, "buzz", "fizz",
                               52, 53, "fizz", "buzz",
                               56, "fizz", 58, 59, "fizzbuzz", 61, 62, "fizz", 64, "buzz", "fizz", 67, 68, "fizz",
                               "buzz", 71, "fizz", 73, 74,
                               "fizzbuzz", 76, 77, "fizz", 79, "buzz", "fizz", 82, 83, "fizz", "buzz", 86, "fizz", 88,
                               89, "fizzbuzz", 91, 92,
                               "fizz", 94, "buzz", "fizz", 97, 98, "fizz"]


@pytest.mark.anyio
async def test_fuzzbizz2():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/fizzbuzz?int1=4&int2=6&limit=100&str1=fizz&str2=buzz")
    assert response.status_code == 200
    assert response.json() == [1, 2, 3, "fizz", 5, "buzz", 7, "fizz", 9, 10, 11, "fizzbuzz", 13, 14, 15, "fizz", 17,
                               "buzz", 19, "fizz", 21, 22, 23, "fizzbuzz", 25, 26, 27, "fizz", 29, "buzz", 31, "fizz",
                               33, 34, 35, "fizzbuzz", 37, 38, 39, "fizz", 41, "buzz", 43, "fizz", 45, 46, 47,
                               "fizzbuzz", 49, 50, 51, "fizz", 53, "buzz", 55, "fizz", 57, 58, 59, "fizzbuzz", 61, 62,
                               63, "fizz", 65, "buzz", 67, "fizz", 69, 70, 71, "fizzbuzz", 73, 74, 75, "fizz", 77,
                               "buzz", 79, "fizz", 81, 82, 83, "fizzbuzz", 85, 86, 87, "fizz", 89, "buzz", 91, "fizz",
                               93, 94, 95, "fizzbuzz", 97, 98, 99]


@pytest.mark.anyio
async def test_stat():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/stat")
    if stat_dict is None:
        assert response.status_code == 200
        assert response.json() == {}
    else:
        assert response.status_code == 200
        assert response.json() == f"Total number of requests {counter}. Most frequent request parameters  {list(stat_dict.keys())[0]} with " \
                                  f"hits {list(stat_dict.values())[0]}"


############# Testing Error Scenarios #####################
@pytest.mark.anyio
async def test_error1():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/fizzbuzz?int1=3&int2=-5&limit=15&str1=fizz&str2=buzz")
    assert response.status_code == 200
    assert response.json() == "Wrong input parameters!"


@pytest.mark.anyio
async def test_error2():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/fizzbuzz?int1=4&int2=5&limit=15&str1=&str2=")
    assert response.status_code == 200
    assert response.json() == "Wrong input parameters!"
