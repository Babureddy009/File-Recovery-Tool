# 🗂️ File Recovery Tool

A modern, user-friendly web application to scan, view, and recover files from your system. Built with Flask, this tool helps you easily locate and restore files of specific types from any directory.

---

## 🚀 Features

- **Scan Drives/Folders:** Quickly scan any drive or folder for files of a chosen type.
- **View & Sort Results:** See found files with their last modified timestamps, sorted for convenience.
- **Recover Files:** Select files to recover and copy them to a safe location.
- **Progress Tracking:** Real-time progress updates for both scanning and recovery.
- **Modern UI:** Responsive frontend with clear instructions and feedback.

---

## 🛠️ Tech Stack

- **Backend:** [Flask](https://flask.palletsprojects.com/)
- **Frontend:** HTML5, CSS3, JavaScript
- **UI Dialogs:** [Tkinter](https://docs.python.org/3/library/tkinter.html) (for folder selection)
- **APIs:** RESTful endpoints for all operations

---

## 📦 Project Structure

```
recovery_tool/
│   app.py              # Flask backend with all endpoints
│
├── static/
│   ├── css/
│   │   └── style.css   # Stylesheet for the frontend
│   └── js/
│       └── script.js   # JavaScript for UI interactions
│
├── templates/
│   └── index.html      # Main HTML template
│
└── README.md           # Project documentation
```

---

## ⚡ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/file-recovery-tool.git
cd file-recovery-tool/recovery_tool
```

### 2. Install Dependencies
```bash
pip install flask flask-cors
```

### 3. Run the Application
```bash
python app.py
```

### 4. Open in Browser
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the tool.

---

## 🖥️ Usage

1. **Browse Drive/Folder:** Click to select the drive or folder to scan.
2. **Choose File Type:** Enter the file extension (e.g., `.txt`, `.jpg`).
3. **Scan:** Start scanning for deleted or existing files of that type.
4. **Select Files:** Pick files you want to recover.
5. **Choose Save Location:** Select where recovered files should be saved.
6. **Recover:** Restore the selected files.

---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Python](https://www.python.org/)

---

> **Made with ❤️ for file safety and recovery.** 