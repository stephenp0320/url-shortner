import requests


def short_link(full_link, link_name):
    API_KEY = '2f42a52444bde4bb3a0c4330699efa368b972'
    BASE_URL = 'https://cutt.ly/api/api.php'
    payload = {'key': API_KEY, 'short': full_link, 'name': link_name}

    try:
        response = requests.get(BASE_URL, params=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()

        if data['url']['status'] == 7:  # Status 7 means the link is successfully shortened
            title = data['url']['title']
            shorten_link = data['url']['shortLink']
            print('Title: ', title)
            print('Shortened link: ', shorten_link)
        else:
            print('Error: ', data['url']['status'])

    except requests.exceptions.RequestException as e:
        print(f"HTTP error: {e}")
    except KeyError:
        print("Error: The API response structure is not as expected.")


if __name__ == "__main__":
    link = input("Enter a link: >> ")
    name = input("Give the link a name: >> ")

    short_link(link, name)
