### Goal:
The aim of this task is to create a working REST service with just one endpoint.
To implement the API, you can use FastAPI or Django REST Framework instead of creating it from scratch.

### Task description:
We have created large file containing sorted numbers from 0 to 1000000, for example:

```
Value: 0 10 20 100 … 1000000
Index: 0 1  2  3   … 50000
```

We would like to be able to call the designed endpoint with HTTP `GET` method and send a `value` that should be found in the input file.
As a response we should get the `index` number for given value and the corresponding value and optional message.

For example, we are sending GET for `/endpoint/100` and as result we should receive 3.

Requirement: We want to load that file into a Python `list` once when the service starts.
So all search operations should be optimized for that particular list.

- In case you're not able to find an `index` for the given value, you can return an `index` for any other existing value, assuming that confirmation is at `10% level` (for example, you were looking for `index` for value = `1150`, but in input file you have `1100` and `1200`, so in that case you can return index for `1100` or `1200`).

- In case you were not able to find valid `index` number, an `error message` should be added into response.

`To summarize`:
- Design API for http `GET` method
- Implement functionality for searching `index` for `given` value (it should be the most efficient algorithm) 
- Add logging
- Add possibility to use configuration file where you can specify service port and log level (you should be able to choose between Info, Debug, Error)
- Add `unit tests` for created components
- Add `README.md` to describe your service
- Automate running tests with `make` file
- Remember that code structure matters
- Upload solution into `GitHub` account and share the link

Sample input file is added as `input.txt` file.