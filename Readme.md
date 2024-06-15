# Hand Gesture Recognition Project

This project involves detecting hand gestures using a microcontroller and translating them into Morse code. The project consists of a web server for handling and displaying the decoded gestures, a microcontroller running MicroPython to detect gestures, and a machine learning model to classify the gestures.

## Folder Structure

### 1. Web Server
This folder contains the code for the web server which is written using Python and Flask. The web server handles incoming data from the microcontroller and displays it on a web page.

#### Files:
- **index.html**: The front-end HTML file that displays the received Morse code.
- **api.py**: The Flask-based API to handle incoming data and serve it to the web page.

#### How to Run:
1. Start the Flask API server:
    ```bash
    python -m api
    ```
2. Start the web server to serve the HTML file:
    ```bash
    python -m http.server
    ```

### 2. MicroController_Auto_Run_Codes
This folder contains the MicroPython code that runs on the microcontroller to detect hand gestures using various sensors and send the detected gestures to the web server.

#### Files:
- **main.py**: The main script that initializes the microcontroller and runs the gesture detection.
- **module.py**: Contains helper functions and classes used in `main.py`.
- **myModel.py**: Contains the machine learning model code for gesture detection.
- **scheme.png**: Diagram showing the architecture of the boards.
- **draw.png**: Additional diagram for the setup.

#### Sensors Used:
- Accelerometer
- Gyroscope
- WiFi Module
- Display
- Push Button
- Resistor (10 ohm)

#### Gestures Detected:
- **Downward / class 0**: Simulates a dot.
- **Leftward / class 1**: Simulates a dash.
- **Forward / class 2**: Simulates the end of an alphabet character.
- **Backward / class 3**: Simulates the end of a word.

### 3. Machine_Learning
This folder contains the machine learning model used to classify the gestures detected by the accelerometer and gyroscope.

#### Files:
- **Classifier.ipynb**: A Jupyter notebook that contains the machine learning code for gesture classification using a RandomForest algorithm.
- **dataset1.csv**: The dataset used to train and test the machine learning model.

## Diagrams
- **scheme.png**: [View Architecture Diagram](file-GaE9Gjh8t3ouKyAzh4TWgM7T)
- **draw.png**: [View Setup Diagram](file-LQPS0MT4tbsH5GGWcrLpa1LT)

## How to Run the Project
1. **Start the Web Server:**
    - Navigate to the Web Server folder and run:
        ```bash
        python -m api
        python -m http.server
        ```
2. **Deploy the Microcontroller Code:**
    - Upload the `main.py`, `module.py`, and `myModel.py` to the microcontroller.
    - Ensure the microcontroller is connected to the necessary sensors (Accelerometer, Gyroscope, etc.).
    - Power on the microcontroller to start detecting gestures and sending data to the web server.
3. **Run the Machine Learning Model:**
    - Open `Classifier.ipynb` in Jupyter Notebook.
    - Ensure `dataset1.csv` is in the same directory.
    - Run the notebook to see the gesture classification in action.

This setup allows the system to detect hand gestures, classify them using the machine learning model, and display the results on a web page.


