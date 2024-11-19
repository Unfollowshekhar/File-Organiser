# File Organizer Web App

A simple web application to organize files in a directory based on their file extensions. The app features a clean and responsive HTML/CSS frontend and a Python backend using Flask.

**Screenshots**
The GUI
![image](https://github.com/user-attachments/assets/24c2f23f-7f3f-4dff-ba7e-4ad56d03722c)

---

## Features

- **Select a Directory**: Choose a directory from your system to organize.
- **Organize Files**: Automatically groups files into subfolders based on their file types.
- **Responsive Design**: Clean and user-friendly interface with mobile responsiveness.
- **Error Handling**: Displays appropriate messages for errors such as invalid directories.

---

## Technologies Used

- **Frontend**:
  - HTML5
  - CSS3 (Responsive design with modern styles)
  - JavaScript (for interactivity and communication with the backend)

- **Backend**:
  - Python
  - Flask (for handling requests and organizing files)

---

## Installation

### Prerequisites
- Python 3.x installed on your system.
- Basic understanding of Python and web development.

### Steps

1. Clone the repository or download the files.
   bash
   git clone https://github.com/your-username/file-organizer-web-app.git
   cd file-organizer-web-app

2. Install the required Python libraries:
   pip install flask

3. Run the backend:
   python app.py

4. Open your browser and navigate to:
   http://localhost:5000


Usage
Select a Directory:

Click the "Browse" button and input the path to a directory.
Organize Files:

Click the "Organize Files" button to group files into subfolders based on their extensions.
View Results:

A success or error message will be displayed on the page.


**File Structure**

project/
├── app.py           # Backend Python script
├── index.html       # Frontend HTML file
├── styles.css       # Frontend CSS for styling
├── script.js        # JavaScript for frontend logic
└── README.md        # Documentation


