from fastapi import FastAPI
import uvicorn as uv
import asyncio

counter = 0  # counter to count API requests
lock = asyncio.Lock()  # safe lock is used to get the actual count not modified by other requests
app = FastAPI()
request, stat_dict = dict(), None  # global dictionary to hold request parameters and its number of call


@app.get("/stat")
async def apiStat():
    """
    This function is called by API statistics end point to return the API statistics
    :return: API Statistics
    """
    global stat_dict
    stat_dict = dict(sorted(request.items(), key=lambda x: x[1], reverse=True))
    # If no API requests made, then result will be empty.
    if len(stat_dict) > 0:
        return f"Total number of requests {counter}. Most frequent request parameters  {list(stat_dict.keys())[0]} with " \
               f"hits {list(stat_dict.values())[0]}"
    else:
        return {}


@app.get("/")
async def start():
    """
    This function is called by the default endpoint
    :return: Returns a welcome message
    """
    global counter
    async with lock:
        counter = counter + 1
    return "Welcome to FizzBuzz!"


@app.get("/fizzbuzz")
async def fizzBuzz(int1, int2, limit, str1, str2):
    """
    This is the actual fizzBuzz function which is being called by API endpoint fizzbuzz.
    :param int1: The first number
    :param int2: The second number
    :param limit: The limit value i.e.; till which the values will be shown
    :param str1: The string which can replace the number which is the multiple of int1
    :param str2: The string which can replace the number which is the multiple of int2
    :return: Returns the list of strings resulted by different number replacements with input strings
    """
    if int(int1) < 0 or int(int2) < 0 or int(limit) < 0 or not str1 or not str2:
        return "Wrong input parameters!"
    result = []
    global counter
    async with lock:
        counter = counter + 1
    # storing the input parameters for API statistics
    parameters = "param1: " + int1 + " " + "param2: " + int2 + " " + "param3: " + limit + " " + "param4: " + str1 + " " + "param5: " + str2
    p_count = 1  # variable to store existing parameters count
    global request
    if parameters in request.keys():
        request.update(((parameters, p_count + 1),))
    else:
        request.update(((parameters, 1),))
    for num in range(1, int(limit)):
        if num % int(int1) == 0 and num % int(int2) == 0:
            result.append(str1 + str2)
        elif num % int(int1) == 0:
            result.append(str1)
        elif num % int(int2) == 0:
            result.append(str2)
        else:
            result.append(num)
    return result


if __name__ == '__main__':
    # Run the server on the available port in any local system
    uv.run(app)
