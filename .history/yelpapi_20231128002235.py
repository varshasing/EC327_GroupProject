import requests

def search_yelp(api_key, term, latitude, longitude, radius=10000):
    # Yelp API endpoint for business search
    endpoint = "https://api.yelp.com/v3/businesses/search"

    # Set up the request headers with your API key
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Set up the parameters for the search
    params = {
        "term": term,
        "latitude": latitude,
        "longitude": longitude,
        "radius": radius
    }

    # Make the API call
    response = requests.get(endpoint, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Print the business information
        for business in data["businesses"]:
            print(f"Name: {business['name']}")
            print(f"Rating: {business['rating']}")
            print(f"Address: {', '.join(business['location']['display_address'])}")
            print("\n")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual Yelp API key
    api_key = "YOUR_API_KEY"

    # Define your search term and coordinates
    search_term = "restaurants"
    latitude = 37.7749  # Replace with the desired latitude
    longitude = -122.4194  # Replace with the desired longitude

    # Perform the Yelp API search
    search_yelp(api_key, search_term, latitude, longitude)
