import requests


def main():

    api_key = "998861d13c2d44ceb37998ac8f558491"

    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"

    response = requests.get(url)

    data = response.json()

    valute = data["rates"]

    return valute


if __name__ == "__main__":
    main()