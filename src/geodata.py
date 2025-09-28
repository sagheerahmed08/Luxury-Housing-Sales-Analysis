import pandas as pd
from geopy.geocoders import Nominatim
import time

places = [
    "Bannerghatta Road, Bangalore",
    "Bellary Road, Bangalore",
    "Domlur, Bangalore",
    "Electronic City, Bangalore",
    "Hebbal, Bangalore",
    "Hennur Road, Bangalore",
    "Indiranagar, Bangalore",
    "Jayanagar, Bangalore",
    "JP Nagar, Bangalore",
    "Kanakapura, Bangalore",
    "Koramangala, Bangalore",
    "MG Road, Bangalore",
    "Rajajinagar, Bangalore",
    "Sarjapur Road, Bangalore",
    "Whitefield, Bangalore",
    "Yelahanka, Bangalore"
]

# Initialize geolocator
geolocator = Nominatim(user_agent="luxury_housing_analysis")

# Collect results
results = []
for place in places:
    try:
        location = geolocator.geocode(place)
        if location:
            results.append({
                "Place": place,
                "Latitude": location.latitude,
                "Longitude": location.longitude
            })
        else:
            results.append({"Place": place, "Latitude": None, "Longitude": None})
    except Exception as e:
        results.append({"Place": place, "Latitude": None, "Longitude": None})
    time.sleep(1) 

# Save to DataFrame
geo_df = pd.DataFrame(results)
print(geo_df)
geo_df.to_csv("./Dataset/coordinates/bangalore_places_latlong.csv", index=False)