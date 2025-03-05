# PYTHON CRUD-APP (DBMS)

A **simple yet efficient database management system (DBMS)** built using Python. This project enables users to **create, read, update, and delete (CRUD) data** in a structured format without relying on external database management systems like MySQL or PostgreSQL.

## 📂 Directory Structure

```
[Your Folder Name]/       # the folder in which user will place the main python script (CRUD-APP (DBMS).py)
│── CRUD-APP (DBMS).py    # Main Python script
│── README.md             # Project documentation (can be placed in the same folder as the code or elsewhere)
│── databases/            # Automatically created on execution
    │── [DatabaseName]/   # Folder for each created database
        │── metadata.txt  # Stores field names & lengths
        │── data.csv      # Stores structured database records

```
## Sample Database  
  - **Employee Management System**:  
  A sample **Employee Management System** database is included in this repository. This sample helps users understand how the DBMS works by providing a ready-to-use structured dataset.
## ✨ Features

- **Database Creation & Management**:  
  Users can create multiple databases, each stored in a separate folder. The folder structure ensures that each database is organized with a metadata file and a CSV file for data storage.

- **Structured Data Storage**:  
  - **metadata.txt**: Contains the field names and their corresponding lengths, ensuring a well-defined structure for data.  
  - **data.csv**: Stores the actual records in a tabular, structured format, making it easy for users to read, modify, and export the data.

- **CRUD Operations**:
  - **Create**: Allows users to define the structure of their database and add records to it.
  - **Read**: Retrieve and display data in an easily readable format, allowing users to view their database content.
  - **Update**: Modify records with new values, making it easy to keep the database current and accurate.
  - **Delete**: Delete specific records or even entire databases, ensuring data can be easily managed.

- **File-Based Storage**:  
  This DBMS uses CSV files for data storage, eliminating the need for an external database management system. This makes it lightweight and easy to use on any machine without additional setup.

- **User-Friendly Command-Line Interface (CLI)**:  
  The program is operated through simple commands in a command-line interface, guiding users through the process of managing their databases.

- **Persistent Data**:  
  Data stored in `data.csv` files is preserved between sessions. This ensures that all changes remain intact even after the application is closed or restarted.

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/huzaifa-2005/DBMS-project.git
   ```
2. Navigate to the folder where you placed the Python script:
   ```sh
   cd <Your Folder Name>
   ```
3. Run the script:
   ```sh
   python "CRUD-APP (DBMS).py"
   ```

## 📌 Usage Guide
- Follow the on-screen instructions to create, read, update, and delete records.
- The **Employee Management System** is included as a sample database to demonstrate the functionality of the application.
- Newly created databases will appear in the `databases/` folder, and the data will be stored in CSV format.

## 🤝 Contributing
   Contributions are welcome! If you’d like to improve this project, feel free to fork the repository, submit pull requests, or suggest new features. Your contributions will help make this project even better!

## 📜 License
This project is open-source and available under the **MIT License**.

---
> 🚀 **Happy Coding!** 🎯

