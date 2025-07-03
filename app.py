import os
import shutil
import threading
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from tkinter import Tk, filedialog

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

progress = {
    'scan': 0,
    'recover': 0
}

def browse_folder():
    root = Tk()
    root.withdraw()  # Hide the main window
    root.attributes("-topmost", True)  # Ensure the dialog is on top
    folder_path = filedialog.askdirectory()
    root.destroy()  # Close the Tkinter instance
    return folder_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/browse_drive', methods=['GET'])
def browse_drive():
    path = browse_folder()
    return jsonify({'path': path})

@app.route('/browse_save', methods=['GET'])
def browse_save():
    path = browse_folder()
    return jsonify({'path': path})

@app.route('/scan_files', methods=['GET'])
def scan_files():
    drive = request.args.get('drive')
    file_type = request.args.get('fileType')
    deleted_files = []

    total_files = sum([len(files) for r, d, files in os.walk(drive)])
    file_count = 0

    for root, dirs, files in os.walk(drive):
        for file in files:
            file_count += 1
            if file.endswith(file_type):
                file_path = os.path.join(root, file)
                modified_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                deleted_files.append({'path': file_path, 'modified_time': modified_time})
            progress['scan'] = (file_count / total_files) * 100

    deleted_files.sort(key=lambda x: x['modified_time'], reverse=True)
    progress['scan'] = 100  # Ensure progress is 100% at the end
    return jsonify({'files': deleted_files})

@app.route('/recover_files', methods=['POST'])
def recover_files():
    data = request.get_json()
    save_dir = data['saveDir']
    files = data['files']

    total_files = len(files)
    file_count = 0

    for file_info in files:
        timestamp, file_path = file_info.split(" - ")
        file_path = os.path.normpath(file_path)
        file_path = os.path.abspath(file_path)
        if os.path.exists(file_path):
            file_name = os.path.basename(file_path)
            save_file_path = os.path.join(save_dir, file_name)
            shutil.copy(file_path, save_file_path)
        file_count += 1
        progress['recover'] = (file_count / total_files) * 100

    progress['recover'] = 100  # Ensure progress is 100% at the end
    return jsonify({'status': 'success'})

@app.route('/progress', methods=['GET'])
def get_progress():
    return jsonify(progress)

if __name__ == '__main__':
    app.run(debug=True)
