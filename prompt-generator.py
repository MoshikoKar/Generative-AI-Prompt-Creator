import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox, QListWidget, QListWidgetItem, QGridLayout, QFileDialog, QMessageBox, QToolTip, QCheckBox
import json

class PromptGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main grid layout
        grid = QGridLayout()
        self.setLayout(grid)

        # Main Subject
        grid.addWidget(QLabel("Main subject:"), 0, 0)
        self.main_subject = QLineEdit(self)
        grid.addWidget(self.main_subject, 0, 1, 1, 2)
        QToolTip.setFont(self.main_subject.font())
        self.main_subject.setToolTip("Enter the main subject of your artwork (e.g., 'A mystical owl').")

        # Secondary Subject
        grid.addWidget(QLabel("Secondary subject:"), 1, 0)
        self.secondary_subject = QLineEdit(self)
        grid.addWidget(self.secondary_subject, 1, 1, 1, 2)
        QToolTip.setFont(self.secondary_subject.font())
        self.secondary_subject.setToolTip("Enter a secondary subject if applicable (e.g., 'with a moonlit background').")

        # Action or Scene
        grid.addWidget(QLabel("Action or scene:"), 2, 0)
        self.action_scene = QComboBox(self)
        actions = sorted([
            "None", "Dancing", "Depressed expression", "Fighting", "Flying", 
            "Gaming", "Graffitiing", "Holding an object", "Holding a sign", "Jumping", 
            "Made of LEGO", "Offering money", "Playing video games", 
            "Pointing", "Posing", "Reading", "Running", "Sitting", "Singing", 
            "Smiling", "Spraying graffiti", "Standing still", "Swimming", 
            "Text in motion", "Walking", "Writing", "Custom..."
        ])
        self.action_scene.addItems(actions)
        grid.addWidget(self.action_scene, 2, 1)
        self.custom_action_scene = QLineEdit(self)
        grid.addWidget(self.custom_action_scene, 2, 2)
        self.action_scene.setToolTip("Select an action or scene that the subject is involved in (e.g., 'Dancing' or 'Playing video games').")

        # Appearance and Details
        grid.addWidget(QLabel("Appearance and details:"), 3, 0)
        self.appearance_details = QLineEdit(self)
        grid.addWidget(self.appearance_details, 3, 1, 1, 2)
        self.appearance_details.setToolTip("Describe specific appearance details (e.g., 'Wearing a red hat and sunglasses').")

        # Background and Environment
        grid.addWidget(QLabel("Background and environment:"), 4, 0)
        self.background_env = QComboBox(self)
        backgrounds = sorted([
            "None", "Abstract art background", "Ancient ruins", "Art gallery scene", "Beach", 
            "Cinematic scene", "City skyline", "Conceptual background", "Dark urban street", 
            "Desert landscape with ruins", "Futuristic city", "Gaming room", 
            "Graffiti wall", "Industrial", "Market scene", "Mountain landscape", 
            "Mystical forest", "Outer space", "Red and blue tones", 
            "Solid vibrant color", "Sunlit sky with rainbow", "Underwater scene", 
            "Urban cityscape", "Vintage background", "Vintage computing setup", 
            "Text on canvas", "Text with shadow effects", "Custom..."
        ])
        self.background_env.addItems(backgrounds)
        grid.addWidget(self.background_env, 4, 1)
        self.custom_background_env = QLineEdit(self)
        grid.addWidget(self.custom_background_env, 4, 2)
        self.background_env.setToolTip("Choose a background or environment (e.g., 'Urban cityscape' or 'Futuristic city').")

        # Mood or Atmosphere
        grid.addWidget(QLabel("Mood or atmosphere:"), 5, 0)
        self.mood_atmosphere = QComboBox(self)
        moods = sorted([
            "None", "Abstract", "Arcane", "Bored", "Cinematic", "Comical", 
            "Conceptual", "Dark", "Dramatic", "Elegant", "Energetic", 
            "Fantasy", "Inspiring", "Joyful", "Light-hearted", "Modern", 
            "Moody", "Mysterious", "Nostalgic", "Peaceful", "Playful", 
            "Romantic", "Sinister", "Striking", "Surreal", "Vibrant", 
            "Whimsical", "Text-based emotion", "Textured mood", "Custom..."
        ])
        self.mood_atmosphere.addItems(moods)
        grid.addWidget(self.mood_atmosphere, 5, 1)
        self.custom_mood_atmosphere = QLineEdit(self)
        grid.addWidget(self.custom_mood_atmosphere, 5, 2)
        self.mood_atmosphere.setToolTip("Select the overall mood or atmosphere you want to convey (e.g., 'Mysterious' or 'Joyful').")

        # Image Style or Art Form
        grid.addWidget(QLabel("Image style or art form:"), 6, 0)
        self.image_style_list = QListWidget(self)
        self.image_style_list.setSelectionMode(QListWidget.MultiSelection)
        image_styles = sorted([
            "3D Render", "Abstract", "Album Cover", "Anime", "Analog Film",
            "Baroque", "Caricature", "Clay Model", "Comic Book",
            "Colored Pencil", "Craft Clay", "Cyberpunk", "Doodle Art",
            "Epic Fantasy Art", "Fashion", "Futurism", "Game GTA",
            "Graffiti", "Impressionism", "Ink Art", "Line Art",
            "Papercraft", "Photograph", "Pixel Art", "Rococo",
            "Sketch", "Sticker Design", "Sticker Decal", "Tattoo Art",
            "Vector Art", "Wildlife Photography", "Surrealism",
            "Cinematic", "Photographic"
        ])
        for style in image_styles:
            item = QListWidgetItem(style)
            self.image_style_list.addItem(item)
        grid.addWidget(self.image_style_list, 6, 1, 2, 2)
        self.image_style_list.setToolTip("Select the artistic style or form you want to use for the image (e.g., '3D Render' or 'Anime').")

        # Text Style or Art Form
        grid.addWidget(QLabel("Text style or art form:"), 8, 0)
        self.text_style_list = QListWidget(self)
        self.text_style_list.setSelectionMode(QListWidget.MultiSelection)
        text_styles = sorted([
            "None", "Balloon Text", "Graffiti Text", "Bubble Letters", "Handwritten",
            "Vintage", "Cursive", "Block Letters", "Comic Style",
            "Neon Lights", "Stencil", "Chalkboard", "Retro", 
            "3D Text", "Textured Text", "Custom..."
        ])
        for style in text_styles:
            item = QListWidgetItem(style)
            self.text_style_list.addItem(item)
        grid.addWidget(self.text_style_list, 8, 1, 1, 2)
        self.text_style_list.setToolTip("Select the artistic style or form you want to use for the text (e.g., 'Balloon Text' or 'Graffiti Text').")

        # Tattoo Styles
        grid.addWidget(QLabel("Tattoo style:"), 9, 0)
        self.tattoo_style = QListWidget(self)
        self.tattoo_style.setSelectionMode(QListWidget.MultiSelection)
        tattoo_styles = sorted([
            "None", "Blackwork", "Dotwork", "Geometric", "Japanese", 
            "Line Art", "Minimalist", "Neo-Traditional", "Old School", 
            "Realism", "Script", "Surrealism", "Traditional", 
            "Watercolor", "Custom..."
        ])
        for style in tattoo_styles:
            item = QListWidgetItem(style)
            self.tattoo_style.addItem(item)
        grid.addWidget(self.tattoo_style, 9, 1, 1, 2)
        self.tattoo_style.setToolTip("Select the tattoo style (e.g., 'Blackwork' or 'Watercolor').")
        self.tattoo_style.setCurrentRow(0)  # Set default to "None"

        # Tattoo Placement
        grid.addWidget(QLabel("Tattoo placement:"), 10, 0)
        self.tattoo_placement = QComboBox(self)
        tattoo_placements = sorted([
            "None", "Arm", "Back", "Chest", "Forearm", 
            "Hand", "Leg", "Neck", "Ribs", 
            "Shoulder", "Thigh", "Wrist", "Custom..."
        ])
        self.tattoo_placement.addItems(tattoo_placements)
        grid.addWidget(self.tattoo_placement, 10, 1, 1, 2)
        self.tattoo_placement.setToolTip("Select the placement of the tattoo on the body (e.g., 'Arm' or 'Back').")
        self.tattoo_placement.setCurrentIndex(0)  # Set default to "None"

        # Color Scheme
        grid.addWidget(QLabel("Color scheme:"), 11, 0)
        self.color_scheme = QComboBox(self)
        colors = sorted([
            "None", "Black and red", "Black and white", "Bold primary colors", "Cool colors", 
            "Dark theme", "Fluorescent", "Gold and fiery red", "Gradient", 
            "High contrast", "Light pastels", "Moody blue and purple", 
            "Monochrome", "Multicolored", "Neon", "Pastel", 
            "Vibrant", "Warm colors", "Vivid colors", "Custom..."
        ])
        self.color_scheme.addItems(colors)
        grid.addWidget(self.color_scheme, 11, 1)
        self.custom_color_scheme = QLineEdit(self)
        grid.addWidget(self.custom_color_scheme, 11, 2)
        self.color_scheme.setToolTip("Choose a color scheme for the artwork (e.g., 'Vibrant' or 'Monochrome').")

        # Visual Effects
        grid.addWidget(QLabel("Visual effects:"), 12, 0)
        self.effects_list = QListWidget(self)
        self.effects_list.setSelectionMode(QListWidget.MultiSelection)
        effects = sorted([
            "None", "3D Effect", "4D", "Cinematic", "Dripping paint", 
            "Dynamic lighting", "Enchanted atmosphere", "Fire effects", "Fluffy textures", 
            "Glowing", "Glossy finish", "Gradient backgrounds", "HDR", 
            "Halftone Dots", "Hyperrealistic", "Light Rays", "Matte finish", 
            "Natural light", "Paint Drips", "Rain effects", "Realistic close-up", 
            "Sparkles", "Surreal effects", "Texture effects", "Ultra detailed"
        ])
        for effect in effects:
            item = QListWidgetItem(effect)
            self.effects_list.addItem(item)
        grid.addWidget(self.effects_list, 12, 1, 2, 2)
        self.effects_list.setToolTip("Select any visual effects you want to include (e.g., 'Glowing' or 'Ultra detailed').")

        # Text or Typography
        grid.addWidget(QLabel("Text or typography:"), 14, 0)
        self.text_typography = QLineEdit(self)
        grid.addWidget(self.text_typography, 14, 1, 1, 2)
        self.text_typography.setToolTip("Specify any text or typography to be included (e.g., 'Bold, graffiti-inspired text').")
        
        # Option to exclude text
        self.no_text_radio = QCheckBox("No Text", self)
        grid.addWidget(self.no_text_radio, 14, 3)

        # Inspirations or References
        grid.addWidget(QLabel("Inspirations or references:"), 15, 0)
        self.inspirations_references = QLineEdit(self)
        grid.addWidget(self.inspirations_references, 15, 1, 1, 2)
        self.inspirations_references.setToolTip("Mention any inspirations or references for the design (e.g., 'Inspired by Japanese Ukiyo-e art'). If empty, examples could be 'Inspired by Picasso's Blue Period' or 'Based on the works of Van Gogh'.")

        # Resolution and Quality
        grid.addWidget(QLabel("Resolution and quality:"), 16, 0)
        self.resolution_quality = QComboBox(self)
        resolutions = sorted(["None", "4K", "8K", "Full HDR", "Hyperrealistic", "Poster Quality", "Ultra HD", "Wide Photo for Wallpapers"])
        self.resolution_quality.addItems(resolutions)
        grid.addWidget(self.resolution_quality, 16, 1, 1, 2)
        self.resolution_quality.setToolTip("Select the resolution and quality of the output (e.g., '8K' or 'Wide Photo for Wallpapers').")

        # Additional Details
        grid.addWidget(QLabel("Additional details:"), 17, 0)
        self.additional_details = QLineEdit(self)
        grid.addWidget(self.additional_details, 17, 1, 1, 2)
        self.additional_details.setToolTip("Add any additional details or specifications you want to include. If empty, examples could be 'Include a subtle gradient background' or 'Ensure the colors are vivid and bold'.")

        # Negative (things you don't want)
        grid.addWidget(QLabel("Negative:"), 18, 0)
        self.negative_details = QLineEdit(self)
        grid.addWidget(self.negative_details, 18, 1, 1, 2)
        self.negative_details.setToolTip("Specify anything you want to avoid in the final result (e.g., 'No bright colors', 'No text').")

        # Special Options (Logo, Birthday, Sign)
        grid.addWidget(QLabel("Special Options:"), 19, 0)
        self.special_options = QListWidget(self)
        self.special_options.setSelectionMode(QListWidget.MultiSelection)
        special_items = sorted(["Album Cover", "Birthday", "Culinary Art", "Logo", "Movie Poster", "Poster", "Sign", "Sticker Decal", "Tattoo Design"])
        for item in special_items:
            list_item = QListWidgetItem(item)
            self.special_options.addItem(list_item)
        grid.addWidget(self.special_options, 19, 1, 2, 2)
        self.special_options.setToolTip("Select any special options related to the format or purpose of the artwork (e.g., 'Album Cover' or 'Tattoo Design').")

        # Generate Button
        self.generate_button = QPushButton('Generate Prompt', self)
        grid.addWidget(self.generate_button, 21, 0, 1, 3)
        self.generate_button.clicked.connect(self.generate_prompt)

        # Clear Button
        self.clear_button = QPushButton('Clear Selection', self)
        grid.addWidget(self.clear_button, 22, 0, 1, 1)
        self.clear_button.clicked.connect(self.clear_selection)

        # Save Button
        self.save_button = QPushButton('Save Selection', self)
        grid.addWidget(self.save_button, 22, 1, 1, 1)
        self.save_button.clicked.connect(self.save_selection)

        # Load Button
        self.load_button = QPushButton('Load Selection', self)
        grid.addWidget(self.load_button, 22, 2, 1, 1)
        self.load_button.clicked.connect(self.load_selection)

        # Result
        self.result_box = QTextEdit(self)
        self.result_box.setReadOnly(True)
        grid.addWidget(self.result_box, 23, 0, 1, 3)

        # Set the layout
        self.setWindowTitle('Generative AI Prompt Creator')
        self.show()

    def generate_prompt(self):
        prompt_parts = []

        def get_article(word):
            vowels = "aeiou"
            if word[0].lower() in vowels:
                return "an"
            else:
                return "a"

        # Main subject or theme
        main_subject = self.main_subject.text().strip()
        if main_subject:
            article = get_article(main_subject)
            prompt_parts.append(f"{article} {main_subject}")

        # Action or Scene
        action_scene = self.action_scene.currentText()
        if action_scene == "Custom...":
            action_scene = self.custom_action_scene.text().strip()

        # Secondary subject
        secondary_subject = self.secondary_subject.text().strip()
        if secondary_subject:
            if action_scene and action_scene != "None":
                prompt_parts.append(f"{action_scene.lower()} {secondary_subject}")
            else:
                if main_subject:
                    prompt_parts.append(f"with {secondary_subject}")
                else:
                    prompt_parts.append(f"in {secondary_subject}")

        # If there's an action or scene but no secondary subject
        if action_scene and action_scene != "None" and not secondary_subject:
            if main_subject:
                prompt_parts.append(f"{action_scene.lower()}")
            else:
                prompt_parts.append(f"{action_scene.lower()}")

        # Appearance and Details
        appearance_details = self.appearance_details.text().strip()
        if appearance_details:
            prompt_parts.append(f"The subject appears {appearance_details}.")

        # Background and Environment
        background_env = self.background_env.currentText()
        if background_env == "Custom...":
            background_env = self.custom_background_env.text().strip()
        if background_env and background_env != "None":
            prompt_parts.append(f"The background is {background_env}.")

        # Mood or Atmosphere
        mood_atmosphere = self.mood_atmosphere.currentText()
        if mood_atmosphere == "Custom...":
            mood_atmosphere = self.custom_mood_atmosphere.text().strip()
        if mood_atmosphere and mood_atmosphere != "None":
            prompt_parts.append(f"The mood is {mood_atmosphere}.")

        # Image Style or Art Form
        selected_image_styles = [item.text() for item in self.image_style_list.selectedItems()]
        if selected_image_styles:
            prompt_parts.append(f"Image Style: {', '.join(selected_image_styles)}.")

        # Text Style or Art Form
        selected_text_styles = [item.text() for item in self.text_style_list.selectedItems()]
        if selected_text_styles and "None" not in selected_text_styles:
            prompt_parts.append(f"Text Style: {', '.join(selected_text_styles)}.")
        
        # Tattoo Style and Placement
        selected_tattoo_styles = [item.text() for item in self.tattoo_style.selectedItems()]
        if selected_tattoo_styles and "None" not in selected_tattoo_styles:
            prompt_parts.append(f"Tattoo style: {', '.join(selected_tattoo_styles)}.")
        
        tattoo_placement = self.tattoo_placement.currentText()
        if tattoo_placement and tattoo_placement != "None":
            prompt_parts.append(f"Placement: {tattoo_placement}.")

        # Color Scheme
        color_scheme = self.color_scheme.currentText()
        if color_scheme == "Custom...":
            color_scheme = self.custom_color_scheme.text().strip()
        if color_scheme and color_scheme != "None":
            prompt_parts.append(f"Colors: {color_scheme}.")

        # Visual Effects
        selected_effects = [item.text() for item in self.effects_list.selectedItems()]
        if selected_effects and "None" not in selected_effects:
            prompt_parts.append(f"Effects: {', '.join(selected_effects)}.")

        # Text or Typography
        if not self.no_text_radio.isChecked():
            text_typography = self.text_typography.text().strip()
            if text_typography:
                prompt_parts.append(f"Text: '{text_typography}'.")

        # Inspirations or References
        inspirations_references = self.inspirations_references.text().strip()
        if inspirations_references and not inspirations_references.startswith("e.g.,"):
            prompt_parts.append(f"Inspired by: {inspirations_references}.")

        # Resolution and Quality
        resolution_quality = self.resolution_quality.currentText()
        if resolution_quality and resolution_quality != "None":
            prompt_parts.append(f"Resolution: {resolution_quality}.")

        # Special Options
        selected_special_options = [item.text() for item in self.special_options.selectedItems()]
        if selected_special_options:
            prompt_parts.append(f"Special options: {', '.join(selected_special_options)}.")

        # Additional Details
        additional_details = self.additional_details.text().strip()
        if additional_details and not additional_details.startswith("e.g.,"):
            prompt_parts.append(f"Additional details: {additional_details}.")

        # Negative (things you don't want)
        negative_details = self.negative_details.text().strip()
        if negative_details:
            prompt_parts.append(f"Exclude: {negative_details}.")

        # Combine prompt parts into a single prompt
        prompt = " ".join(prompt_parts)

        # Display the result
        self.result_box.setText(prompt)

    def clear_selection(self):
        self.main_subject.clear()
        self.secondary_subject.clear()
        self.custom_action_scene.clear()
        self.appearance_details.clear()
        self.custom_background_env.clear()
        self.custom_mood_atmosphere.clear()
        self.custom_color_scheme.clear()
        self.text_typography.clear()
        self.inspirations_references.clear()
        self.additional_details.clear()
        self.negative_details.clear()

        self.action_scene.setCurrentIndex(0)
        self.background_env.setCurrentIndex(0)
        self.mood_atmosphere.setCurrentIndex(0)
        self.color_scheme.setCurrentIndex(0)
        self.text_style_list.clearSelection()
        self.resolution_quality.setCurrentIndex(0)

        self.image_style_list.clearSelection()
        self.tattoo_style.clearSelection()
        self.tattoo_placement.setCurrentIndex(0)
        self.effects_list.clearSelection()
        self.special_options.clearSelection()
        self.no_text_radio.setChecked(False)

        self.result_box.clear()

    def save_selection(self):
        save_data = {
            "main_subject": self.main_subject.text(),
            "secondary_subject": self.secondary_subject.text(),
            "action_scene": self.action_scene.currentText(),
            "custom_action_scene": self.custom_action_scene.text(),
            "appearance_details": self.appearance_details.text(),
            "background_env": self.background_env.currentText(),
            "custom_background_env": self.custom_background_env.text(),
            "mood_atmosphere": self.mood_atmosphere.currentText(),
            "custom_mood_atmosphere": self.custom_mood_atmosphere.text(),
            "image_style_list": [item.text() for item in self.image_style_list.selectedItems()],
            "text_style_list": [item.text() for item in self.text_style_list.selectedItems()],
            "tattoo_style": [item.text() for item in self.tattoo_style.selectedItems()],
            "tattoo_placement": self.tattoo_placement.currentText(),
            "color_scheme": self.color_scheme.currentText(),
            "custom_color_scheme": self.custom_color_scheme.text(),
            "effects_list": [item.text() for item in self.effects_list.selectedItems()],
            "text_typography": self.text_typography.text(),
            "inspirations_references": self.inspirations_references.text(),
            "resolution_quality": self.resolution_quality.currentText(),
            "additional_details": self.additional_details.text(),
            "negative_details": self.negative_details.text(),
            "special_options": [item.text() for item in self.special_options.selectedItems()],
            "no_text": self.no_text_radio.isChecked()
        }

        filename, _ = QFileDialog.getSaveFileName(self, "Save Selection", "", "JSON Files (*.json);;All Files (*)")
        if filename:
            try:
                with open(filename, 'w') as file:
                    json.dump(save_data, file, indent=4)
                QMessageBox.information(self, "Success", "Selection saved successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save the selection: {str(e)}")

    def load_selection(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Load Selection", "", "JSON Files (*.json);;All Files (*)")
        if filename:
            try:
                with open(filename, 'r') as file:
                    save_data = json.load(file)
                self.clear_selection()
                self.main_subject.setText(save_data.get("main_subject", ""))
                self.secondary_subject.setText(save_data.get("secondary_subject", ""))
                self.action_scene.setCurrentText(save_data.get("action_scene", "None"))
                self.custom_action_scene.setText(save_data.get("custom_action_scene", ""))
                self.appearance_details.setText(save_data.get("appearance_details", ""))
                self.background_env.setCurrentText(save_data.get("background_env", "None"))
                self.custom_background_env.setText(save_data.get("custom_background_env", ""))
                self.mood_atmosphere.setCurrentText(save_data.get("mood_atmosphere", "None"))
                self.custom_mood_atmosphere.setText(save_data.get("custom_mood_atmosphere", ""))
                
                image_styles = save_data.get("image_style_list", [])
                for i in range(self.image_style_list.count()):
                    item = self.image_style_list.item(i)
                    if item.text() in image_styles:
                        item.setSelected(True)

                text_styles = save_data.get("text_style_list", [])
                for i in range(self.text_style_list.count()):
                    item = self.text_style_list.item(i)
                    if item.text() in text_styles:
                        item.setSelected(True)

                tattoo_styles = save_data.get("tattoo_style", [])
                for i in range(self.tattoo_style.count()):
                    item = self.tattoo_style.item(i)
                    if item.text() in tattoo_styles:
                        item.setSelected(True)

                self.tattoo_placement.setCurrentText(save_data.get("tattoo_placement", "None"))
                self.color_scheme.setCurrentText(save_data.get("color_scheme", "None"))
                self.custom_color_scheme.setText(save_data.get("custom_color_scheme", ""))
                
                effects = save_data.get("effects_list", [])
                for i in range(self.effects_list.count()):
                    item = self.effects_list.item(i)
                    if item.text() in effects:
                        item.setSelected(True)

                self.text_typography.setText(save_data.get("text_typography", ""))
                self.inspirations_references.setText(save_data.get("inspirations_references", ""))
                self.resolution_quality.setCurrentText(save_data.get("resolution_quality", "None"))
                self.additional_details.setText(save_data.get("additional_details", ""))
                self.negative_details.setText(save_data.get("negative_details", ""))

                special_options = save_data.get("special_options", [])
                for i in range(self.special_options.count()):
                    item = self.special_options.item(i)
                    if item.text() in special_options:
                        item.setSelected(True)

                self.no_text_radio.setChecked(save_data.get("no_text", False))
                QMessageBox.information(self, "Success", "Selection loaded successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load the selection: {str(e)}")

def main():
    app = QApplication(sys.argv)
    ex = PromptGenerator()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
