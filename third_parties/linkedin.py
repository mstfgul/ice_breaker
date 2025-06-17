import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/mstfgul/412a4ea4ea1df73c7a8c2a50e96d69a9/raw/fa35ef6e5f1a0ef723107baddcb91cb2600ead89/mustafa-gul-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        # ENROLL WITH COUPON CODE: EDENMARCO
        # For 20% Discount on all pricing
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )

    data = response.json().get("person")
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifications"]
    }

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/mustafa-gul00/"
        ),
    )