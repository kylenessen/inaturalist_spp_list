#%%
import requests
# %%
def get_species_list(latitude, longitude, radius, max_results=50):
    base_url = "https://api.inaturalist.org/v1/observations/species_counts"
    params = {
        "lat": latitude,
        "lng": longitude,
        "radius": radius,
        "per_page": max_results,
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        species_list = []
        for result in data["results"]:
            common_name = result["taxon"].get("preferred_common_name", "Unknown")
            species = {
                "id": result["taxon"]["id"],
                "name": result["taxon"]["name"],
                "common_name": common_name,
                "count": result["count"],
            }
            species_list.append(species)
        return species_list
    else:
        print(f"Error: {response.status_code}")
        return None
#%%
# Example usage:
latitude = 34.052235
longitude = -118.243683
radius = .1  # in km
species_list = get_species_list(latitude, longitude, radius)

if species_list:
    for species in species_list:
        print(f"{species['common_name']} ({species['name']}) - Count: {species['count']}")
else:
    print("Failed to get species list")


# %%
