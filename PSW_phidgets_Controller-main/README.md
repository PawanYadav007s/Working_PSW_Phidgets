# PSW Controller Dashboard 🔌

A professional offline web-based dashboard built with **Flask** for controlling and monitoring an industrial **power supply unit** at Mahindra. This user-friendly interface enables real-time operations like **Connect**, **Disconnect**, **Start**, **Stop**, and **Cycle Monitoring** with live voltage and current readings.

---

## ✨ Features

- ✅ **Responsive UI** with a modern industrial look
- ⚡ Real-time **job cycle data** (Cycle No., Voltage, Current)
- 📂 Planned support for **Excel data export**
- 🔐 Secure access to **Settings** via login popup
- 🔵 Live **status indicator** (Red/Green)
- 📋 View detailed logs and progress
- ⚙ Set custom **parameters** (voltage, cycles, delay)

---

## 💡 Technologies Used

- **Python 3.x** with **Flask** (Backend)
- **HTML5, CSS3, JavaScript** (Frontend)
- **Jinja2** for template rendering
- **(Planned)** `pandas` for Excel export

---

## 🚀 Getting Started

### Prerequisites:  
- Python 3.x installed
- `pip` package manager

### Installation:

```bash
git clone https://github.com/your-username/psw-controller-dashboard.git
cd psw-controller-dashboard
pip install -r requirements.txt
```

### Run the Application:

```bash
python app.py
```

Then open your browser and visit: `http://127.0.0.1:5001`

---

## 📅 Folder Structure
```
psw-controller-dashboard/
|│
|├── static/
|   └── styles.css         # CSS styling
|
|├── templates/
|   ├── index.html         # Dashboard UI
|   ├── settings.html      # Settings page
|   └── cycle_data.html    # Live cycle data table
|
|├── app.py               # Flask main application
|└── requirements.txt      # Python dependencies
```

---

## 🛌 Future Plans
- [x] Stylish & responsive UI
- [x] Dynamic cycle data list
- [ ] Save cycle data to Excel
- [ ] Error handling + alert system
- [ ] Docker containerization

---

## ✊ Contribution
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## ✉ Contact
**Developer**: Pawan Yadav
**Email**: pawanyadav211191@gmail.com  
**LinkedIn**: [linkedin.com/in/yourname](https://linkedin.com/in/yourname)

---

## ⚖ License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.






Commands


pyinstaller --noconfirm --onefile --windowed --add-data "templates;templates" --add-data "static;static" --icon=icon.ico start.py
