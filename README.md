
# Generative AI Prompt Creator

## Overview

The **Generative AI Prompt Creator** is a Python-based desktop application that allows users to dynamically generate prompts for AI generative models. The application features a customizable GUI where users can select or input various options such as the main subject, secondary subject, action or scene, background, environment, mood, and many more. These selections are then used to generate a detailed prompt suitable for AI art or text generation models.

## Features

- **Dynamic GUI:** User-friendly interface built with PyQt that allows easy customization of prompts.
- **Multiple Categories:** Options include actions, scenes, background, environment, mood, image style, text style, color schemes, visual effects, and more.
- **Custom Inputs:** Users can input custom details or select predefined options for comprehensive control over the generated prompts.
- **Save and Load Configurations:** Ability to save and load custom configurations to and from JSON files for reusability.
- **Real-time Prompt Generation:** See the generated prompt in real-time as you make selections.
- **Negative Prompting:** Option to exclude certain elements from the final generated prompt.
- **Flexible Output:** Generates prompts suitable for a variety of AI models and uses, including image generation, text-based AI, and more.

## Installation

### Prerequisites

- Python 3.x
- `PyQt5` library
- `json` (part of the Python standard library)

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MoshikoKar/Generative-AI-Prompt-Creator
   cd Generative-AI-Prompt-Creator
   ```

2. **Install Required Libraries:**
   Install the necessary Python libraries using `pip`:
   ```bash
   pip install PyQt5
   ```

3. **Run the Application:**
   Execute the following command to start the application:
   ```bash
   python prompt-generator.py
   ```

## Usage

1. **Main Subject & Secondary Subject:**
   - Define the main focus and an optional secondary element for your prompt.
   
2. **Action or Scene:**
   - Choose an action or scene to describe what the subject is doing or where it is situated.

3. **Appearance and Details:**
   - Add specific details regarding the appearance of the subject(s).

4. **Background and Environment:**
   - Select or define the setting or environment where the scene is taking place.

5. **Mood or Atmosphere:**
   - Set the tone or mood for the scene.

6. **Styles and Effects:**
   - Choose from various image and text styles, visual effects, and color schemes to define the artistic style of the output.

7. **Text or Typography:**
   - Add text or typography elements that should be included in the prompt.

8. **Special Options:**
   - Choose special formats like posters, album covers, or logos.

9. **Negative Prompts:**
   - Exclude unwanted elements from the generated prompt.

10. **Save and Load:**
    - Save your settings to a JSON file for later use or load previously saved configurations.

11. **Generate Prompt:**
    - Click the 'Generate Prompt' button to see the resulting prompt, which will be displayed in the output box at the bottom.

## Example Prompts

Here are some example prompts that can be generated using this application:

- "A vibrant, abstract painting of a mystical forest, with glowing trees and surreal effects. The scene is set in a futuristic city skyline at dusk. Colors are vivid and bold, and the mood is whimsical and dreamlike."
  
- "A realistic close-up of a golden retriever wearing a superhero cape, sitting on a busy city street at night. The scene is cinematic, with dynamic lighting and rain effects. The text 'Hero Dog' is written in bold, 3D typography with a glowing effect."

## Customization

You can customize the application by editing the Python code to include additional options or modify existing ones. The `prompt-generator.py` file is where most of the logic resides. You can also modify the GUI layout in the `PromptGenerator` class.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure your code follows the project's coding standards and includes proper documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, please feel free to open an issue or contact me at 
