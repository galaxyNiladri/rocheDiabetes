**Description**
The fizzbuzz API server works with fizzbuzz logic. It has three API endpoints currently. Each of them support only GET requests currently.

**GET**
/<none> : When the API is hit with no argument and endpoint name, it returns the default page with message "Welcome to FizzBuzz!"

/stat :   This endpoint returns the API statistics which means how many requests has been made to the API. With that, which requests has been made most frequently with the parameter 
details as well as hit count.

/fizzbuzz?int1=<value>&int2=<value>&limit=<value>&str1=<value>&str2=<value> : This endpoint returns a list of strings with members replaced by strings supplied in the arguments if they are
multiple of int1 or int2 or both.
