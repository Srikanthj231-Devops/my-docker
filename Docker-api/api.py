# cat_facts.py

import requests

def get_random_cat_fact():
    url = "https://catfact.ninja/fact"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad status codes

        data = response.json()
        fact = data.get("fact")

        if fact:
            print("🐱 Random Cat Fact:")
            print(f"→ {fact}")
        else:
            print("No fact found in the response.")

    except requests.RequestException as e:
        print(f"Error fetching cat fact: {e}")

if __name__ == "__main__":
    get_random_cat_fact()
