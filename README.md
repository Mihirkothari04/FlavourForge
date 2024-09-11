# FlavorForge

FlavorForge is an innovative online chef application that leverages generative AI and computer vision to revolutionize your cooking experience. Upload an image of your ingredients, and FlavorForge will generate personalized recipes tailored to your preferences and available resources.

## Features

- 🥕 Ingredient Recognition: Automatically identify ingredients from uploaded images
- 🍽️ User Customization: Specify meal type, kitchen tools, cooking time, and expertise level
- ⏱️ Instant Recipe Generation: Receive customized recipes with detailed instructions in seconds
- 🔄 Dynamic Updates: Real-time recipe adjustments based on input changes
- 💻 Interactive UI: Seamless user experience built with Streamlit

## Technical Stack

- Python 3.x
- Streamlit
- Google Generative AI (Gemini API)
- Pillow (PIL)
- python-dotenv

## Prerequisites

Before running FlavorForge, you need to obtain a Google Gemini API key:

1. Visit the [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click on "Create API key" in the API keys section
4. Copy the generated API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/flavorforge.git
   cd flavorforge
   ```

2. Install required packages:
   ```
   pip install streamlit google-generativeai Pillow python-dotenv
   ```

3. Create a `.env` file in the project root and add your Google Gemini API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`)

3. Use the application:
   - Upload an image of your ingredients
   - Select meal type, kitchen tools, cooking time, and expertise level
   - View the generated recipe and instructions

## How It Works

1. **Image Upload**: The user uploads an image of ingredients using Streamlit's `file_uploader`.

2. **Ingredient Recognition**: The uploaded image is processed using the Gemini 1.5 Flash model to identify ingredients.

3. **User Input**: The application collects user preferences through various Streamlit input widgets.

4. **Recipe Generation**: Using the Gemini Pro model, FlavorForge generates a customized recipe based on the identified ingredients and user inputs.

5. **Display**: The generated recipe and instructions are displayed to the user through the Streamlit interface.

## Customization

You can modify the `main.py` file to adjust various aspects of the application, such as:

- Available meal types
- Kitchen tool options
- Cooking time range
- Expertise levels
- Prompt engineering for recipe generation

## Limitations

- The accuracy of ingredient recognition depends on the quality of the uploaded image and the capabilities of the Gemini 1.5 Flash model.
- Recipe generation is based on the Gemini Pro model and may not always produce perfect results.

## Future Improvements

- Implement error handling for API failures or timeouts
- Add support for multiple languages
- Integrate nutritional information for generated recipes
- Implement user accounts for saving favorite recipes

## Contributing

Contributions to FlavorForge are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
