from flask import Flask, request, jsonify, render_template
import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Load Azure OpenAI and Bing Search API credentials from environment variables
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv(
    "AZURE_OPENAI_ENDPOINT"
)  # Example: https://your-resource-name.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv(
    "AZURE_OPENAI_DEPLOYMENT_NAME"
)  # The deployment name for GPT-4
BING_SEARCH_API_KEY = os.getenv("BING_SEARCH_API_KEY")  # Bing Image Search API Key


# Route to render the HTML form
@app.route("/")
def index():
    return render_template("index.html")


# Route to handle form submission and return the trip plan with images
@app.route("/plan_trip", methods=["POST"])
def plan_trip():
    # Get user inputs from the form
    destination = request.form["destination"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    preferences = request.form["preferences"]

    # Create the payload for Azure OpenAI
    payload = {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant specialized in trip planning.",
            },
            {
                "role": "user",
                "content": f"Plan a trip to {destination} from {start_date} to {end_date}. "
                f"I prefer {preferences}. Can you suggest an itinerary?",
            },
        ]
    }

    # Set up headers for the API request
    headers = {"Content-Type": "application/json", "api-key": AZURE_OPENAI_API_KEY}

    # The Azure OpenAI API URL
    url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_OPENAI_DEPLOYMENT_NAME}/chat/completions?api-version=2023-05-15"

    try:
        # Send a POST request to the Azure OpenAI API
        response = requests.post(url, headers=headers, json=payload)

        # Raise an error if the response was unsuccessful
        response.raise_for_status()

        # Extract the response from Azure OpenAI
        completion = response.json()
        trip_plan = completion["choices"][0]["message"]["content"]

        # Split trip plan into individual suggestions (assuming each suggestion is in a new line)
        suggestions = trip_plan.split("\n")

        # Generate images for each suggestion using Bing Image Search API
        images = []
        for suggestion in suggestions:
            if suggestion.strip():  # Skip empty lines
                image_url = generate_image(suggestion)
                images.append({"suggestion": suggestion, "image_url": image_url})

        # Render the trip plan with the corresponding images in the template
        return render_template("trip_plan.html", suggestions_with_images=images)

    except Exception as e:
        return jsonify({"error": str(e)})


# Function to generate images using Azure Bing Image Search API
def generate_image(suggestion):
    bing_image_search_url = "https://api.bing.microsoft.com/v7.0/images/search"

    headers = {"Ocp-Apim-Subscription-Key": BING_SEARCH_API_KEY}  # Bing Search API key

    params = {
        "q": suggestion,  # Query (the suggestion text)
        "count": 1,  # We only need one image
        "imageType": "photo",
        "size": "large",
    }

    try:
        # Send a GET request to Bing Image Search API
        response = requests.get(bing_image_search_url, headers=headers, params=params)
        response.raise_for_status()

        # Parse the first image result
        search_results = response.json()
        if "value" in search_results and len(search_results["value"]) > 0:
            image_url = search_results["value"][0]["contentUrl"]
            return image_url
        else:
            return None

    except Exception as e:
        print(f"Error retrieving image from Bing: {e}")
        return None


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
