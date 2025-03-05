# CRUD-APP (DBMS)

A **simple yet efficient database management system (DBMS)** built using Python. This project enables users to **create, read, update, and delete (CRUD) data** in a structured format without relying on external database management systems like MySQL or PostgreSQL.

## 📂 Project Structure
```
DBMS-project/
│── CRUD-APP (DBMS).py    # Main Python script
│── README.md             # Project documentation
│── databases/            # Automatically created on execution
    │── [DatabaseName]/   # Folder for each created database
        │── metadata.txt  # Stores field names & lengths
        │── data.csv      # Stores structured database records
```

## ✨ Features
- **Database Creation & Management**: Users can create multiple databases, each stored in a separate folder.
- **Structured Data Storage**: Each database contains a `metadata.txt` file defining field names and lengths and a `data.csv` file for storing actual records.
- **CRUD Operations**:
  - **Create**: Define database structure and add records.
  - **Read**: Retrieve and display data from the database.
  - **Update**: Modify existing records.
  - **Delete**: Remove records or entire databases.
- **File-Based Storage**: No external database required; data is stored locally in CSV format.
- **User-Friendly Interaction**: Command-line interface for seamless database management.
- **Persistent Data**: Ensures that data remains intact even after program termination.
- **Sample Database**: "Employee Management System" included as an example.

## 🚀 Getting Started
### Prerequisites
- Python 3.x installed on your system

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/DBMS-project.git
   ```
2. Navigate to the project folder:
   ```sh
   cd DBMS-project
   ```
3. Run the script:
   ```sh
   python "CRUD-APP (DBMS).py"
   ```

## 📌 Usage Guide
- Follow on-screen instructions to create, read, update, and delete records.
- Newly created databases will appear in the `databases/` folder.
- Data is stored in CSV format and can be accessed directly if needed.

## 📜 License
This project is open-source and available under the **MIT License**.

## 📞 Contact
For any queries or suggestions, feel free to reach out!

---
> 🚀 **Happy Coding!** 🎯

