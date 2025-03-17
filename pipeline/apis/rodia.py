import requests

species_url = "https://swapi-api.alx-tools.com/api/species/"
while species_url:
    res = requests.get(species_url)
    species_data = res.json()

    for species in species_data.get('results', []):
        name = species.get('name')
        designation = species.get('designation')
        homeworld = species.get('homeworld')

        if "rodian" in name.lower():
            print(f"Name: {name}")
            print(f"Designation: {designation}")
            print(f"Homeworld: {homeworld}")

    species_url = species_data.get('next')
