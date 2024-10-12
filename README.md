# 🌍 **Trip Planner with Azure OpenAI and Bing Image Search**

The Trip Planner is a Python Flask application that allows users to generate personalized trip itineraries based on natural language inputs. It leverages the Azure OpenAI API to provide detailed travel suggestions and the Bing Image Search API to retrieve relevant images for each recommendation.

This project helps users plan trips in an intuitive way by simply inputting their desired destination, travel dates, and preferences. The app generates an itinerary and provides images related to the suggested activities or locations.

# 🌟 **Features**

**Flask API:** Built with Flask to create a web application for generating trip plans.

**Azure OpenAI Integration:** Utilizes Azure OpenAI to interpret user prompts and generate detailed trip plans.

**Bing Image Search Integration:** Uses the Bing Image Search API to fetch relevant images for each travel recommendation.

**User-Friendly Interface:** Allows users to input destination, dates, and preferences for a personalized experience.

**Image Retrieval:** Displays travel suggestions along with matching images to enhance trip planning.
# **🛠️ Installation**

# **Clone the repository:** 

```
git clone https://github.com/your-username/Trip-Planner-App.git

cd Trip-Planner-App
```

# Install dependencies:

```
pip install -r requirements.txt
```
# Configure Azure OpenAI and Bing Search API keys:

**Create a .env file in the project root directory and add your API keys:**

```
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
BING_SEARCH_API_KEY=your_bing_search_api_key
```

# **🖥️ Usage**

**Run the Flask application:**

```
python app.py
```

Access the application via http://localhost:5000.

**Demo:**

**Watch a Demo Video:**
[Watch the demo on YouTube]https://youtu.be/DqqCbHC9MtA

# **How to use:**

Enter the destination, start date, end date, and preferences into the form on the homepage.
Submit the form to generate a personalized trip itinerary.
The application will display the trip plan along with relevant images for each suggestion.

**Example**

**Input:**

```
Destination: Norway
Start Date: 2024-10-12
End Date: 2024-10-14
Preferences: Northern Lights, nature, adventure
```
**Output:** 
```
Day 1: October 12, 2024 - Arrival in Tromsø
- Flight to Tromsø, the "Gateway to the Arctic."
- Check-in at a local hotel.
- Evening Northern Lights tour.

Day 2: October 13, 2024 - Explore Tromsø
- Morning hike in the Lyngen Alps.
- Afternoon visit to the Arctic Cathedral.
- Evening reindeer sledding experience.
...
```

The application will also display images related to each suggestion, such as pictures of Tromsø, the Northern Lights, and local adventures.
# **👥 Contributing**

Contributions to the Trip Planner App are welcome! To contribute, please follow these steps:

**Fork the repository**

Create a new branch for your feature or bug fix.

Make your changes and commit them.

Push your changes to your forked repository.

Submit a pull request to the main repository.

# **📜 License**

The Trip Planner App is released under the MIT License.
