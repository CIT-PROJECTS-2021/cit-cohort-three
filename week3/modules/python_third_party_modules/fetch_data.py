# In this program, we are going to learn how to use thirdpaty modules in python
import requests



def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)

    return response.text


def main():
    url = "https://jsonplaceholder.typicode.com/todos"
    print(fetch_data(url))


if __name__ == "__main__":
    main()
