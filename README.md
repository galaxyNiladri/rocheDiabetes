**Project Description**

This is a coding competition by Roche to implement FizzBuzz REST Server. The server should expose a REST API endpoint, with the additional feature of a statistical endpoint.
Fizz-Buzz Logic
The Fizz-Buzz algorithm involves replacing all multiples of 3 with "fizz", all multiples of 5 with "buzz" and all multiples of 15 with "fizzbuzz". Your output should look like this:

Example: “1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz,16,..."

**Installation and Usage**
1. Clone the repository by typing "git clone https://github.com/galaxyNiladri/rocheDiabetes.git/'"
2. cd rocheDiabetes
3. cd roche
4. Run python main.py
5. Open the url "https://localhost:8000" in your local browser

**Testing**
1. cd rocheDiabetes
2. cd roche
3. Run pytest
4. You will get the test pass results

**External Libraries**
1. uvicorn : Uvicorn is ASGI Python webframework. ASGI is used because it follows asynchronous concurrency model which helps in lightweight background tasks. This in turn can be helpful for slow HTTP requests. It is used to run the API server developed with fastapi.
2. fastapi: FastAPI is a python webframework for building APIs in python in par with Go and NodeJS in minimal time.
3. pytest: Pytest is a testing framework for Python to support small unit tests as well as complex functional tests for applications as well as APIs.
4. httpx: httpx is a fully featured HTTP client library in Python. It supports both synchronous and asynchronous APIs.
5. trio: This library is used to produce a production quality code async/await I/O libary in Python.
