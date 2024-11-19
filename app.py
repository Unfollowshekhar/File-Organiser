from flask import Flask, request, jsonify, send_from_directory
import os
import shutil

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.route("/styles.css")
def styles():
    return send_from_directory('.', 'styles.css')

@app.route("/script.js")
def script():
    return send_from_directory('.', 'script.js')

@app.route("/organize", methods=["POST"])
def organize():
    data = request.get_json()
    directory_path = data.get("directory")

    if not os.path.exists(directory_path):
        return jsonify({"error": "Directory does not exist."}), 400

    try:
        for filename in os.listdir(directory_path):
            if os.path.isdir(os.path.join(directory_path, filename)):
                continue

            file_extension = filename.split('.')[-1]
            folder_name = file_extension.upper() + "_files"
            folder_path = os.path.join(directory_path, folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            old_file_path = os.path.join(directory_path, filename)
            new_file_path = os.path.join(folder_path, filename)
            shutil.move(old_file_path, new_file_path)

        return jsonify({"success": "Files have been organized."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
