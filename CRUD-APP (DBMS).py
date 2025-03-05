import csv
import os

# Ensure all paths are relative to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Ensure the "databases" folder exists
databases_folder = os.path.join(os.getcwd(), "databases")
os.makedirs(databases_folder, exist_ok=True)

def display_all_records(lower_case_desired_dbms):
    while True: 
        choice=input('Confirm that you want to display all records (yes/no) : ').strip().lower()
        if choice.strip()!='yes' and choice.strip()!='no':
            print('Invalid Choice')
            continue
        elif choice.strip()=='no':
            print('Exiting without proceeding')
            return
        elif choice.strip()=='yes':      
            lst_actual_existing_dbms = os.listdir(databases_folder)
            lower_case_lst_existing_dbms=[dbms.strip().lower() for dbms in lst_actual_existing_dbms]
            if lower_case_desired_dbms not in lower_case_lst_existing_dbms:
                print(f'DATABASE {lower_case_desired_dbms} does not exist')
                return
            actual_opened_dbms = lst_actual_existing_dbms[lower_case_lst_existing_dbms.index(lower_case_desired_dbms)]
            path_of_opened_dbms = os.path.join(databases_folder, actual_opened_dbms)
            data_file = os.path.join(path_of_opened_dbms, actual_opened_dbms + ".csv")
            
            if not os.path.exists(data_file):
                print("Error: Data file not found!")
                return
            print('ALL RECORDS ARE AS FOLLOWS : ')
            records = []  # List to store all dictionary records
            with open(data_file, mode='r', newline='') as file:
                reader=csv.DictReader(file)
                for row in reader:
                    records.append(dict(row))  # Convert OrderedDict to normal dict
            for record in records:
                print("\n")  # Add a new line for readability
                print(record)  # Prints each dictionary with a newline
            return    


def delete_record(lower_case_desired_dbms):
    while True: 
        choice=input('Confirm that you want to delete record(s) (yes/no) : ').strip().lower()
        if choice.strip()=='no':
            print('Exiting without proceeding')
            return
        elif  choice.strip()!='yes' and  choice.strip()!='no':
            print('Invalid choice')
            continue
        elif choice.strip()=='yes':      
            lst_actual_existing_dbms = os.listdir(databases_folder)
            lower_case_lst_existing_dbms=[dbms.strip().lower() for dbms in lst_actual_existing_dbms]
            if lower_case_desired_dbms not in lower_case_lst_existing_dbms:
                print(f'DATABASE {lower_case_desired_dbms} does not exist')
                return
            actual_opened_dbms = lst_actual_existing_dbms[lower_case_lst_existing_dbms.index(lower_case_desired_dbms)]
            path_of_opened_dbms = os.path.join(databases_folder, actual_opened_dbms)
            data_file = os.path.join(path_of_opened_dbms, actual_opened_dbms + ".csv")
            if not os.path.exists(data_file):
                print("Error: Data file not found!")
                return
            while True:
                # Read existing records
                with open(data_file, mode='r', newline='') as file:
                    reader = csv.reader(file)
                    records = list(reader)  # Read all records into a list
                
                if len(records) < 2:
                    print("No records available to delete.")
                    return
                
                # Display existing records
                print("Existing Records:")
                for i, row in enumerate(records[1:], start=1):  # Skipping header row
                    print(i, row)
                
                try:
                    record_to_delete = int(input("Enter the record number to delete: "))
                    if record_to_delete < 1 or record_to_delete >= len(records):
                        print("Invalid record number.")
                        return
                except ValueError:
                    print("Please enter a valid number.")
                    return
                
                # Remove the selected record
                del records[record_to_delete]
                
                # Write the updated records back to the CSV file
                with open(data_file, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(records)
                
                print(f"Record {record_to_delete} has been deleted successfully from {actual_opened_dbms}.")
                choice=input('Do you want to delete another record (yes/no) : ').strip().lower()
                if choice!='yes':
                    break
            return
    

def add_record(lower_case_desired_dbms):
    while True: 
        choice=input('Confirm that you want to add a record (yes/no) : ').strip().lower()
        if choice=='no':
            print('Exiting without proceeding')
            return
        elif  choice.strip()!='yes' and  choice.strip()!='no':
            print('Invalid choice')
            continue  
        elif choice.strip()=='yes':      
            lst_actual_existing_dbms = os.listdir(databases_folder)
            lower_case_lst_existing_dbms=[dbms.strip().lower() for dbms in lst_actual_existing_dbms]
            if lower_case_desired_dbms not in lower_case_lst_existing_dbms:
                print(f'DATABASE {lower_case_desired_dbms} does not exist')
                return
            actual_opened_dbms = lst_actual_existing_dbms[lower_case_lst_existing_dbms.index(lower_case_desired_dbms)]
            path_of_opened_dbms = os.path.join(databases_folder, actual_opened_dbms)
            data_file = os.path.join(path_of_opened_dbms, actual_opened_dbms + ".csv")
            system_file = path_of_opened_dbms + '/System file_' + actual_opened_dbms + '.txt'
            
            lst_of_field_names = []
            lst_of_field_lengths = []

            # Read system file to extract field lengths and field names
            with open(system_file, 'r') as file:
                lines = file.readlines() #Returns a list having each line(till \n) as a str element.
                for line in lines:
                    parts = line.strip().split(":")
                    if "NAME OF FIELD" in line:
                        lst_of_field_names.append(parts[1].strip())
                    elif "LENGTH OF FIELD" in line:
                        lst_of_field_lengths.append(int(parts[1].strip()))
            # while True:
                #  If field lengths exist but field names are missing, prompt user to enter them
            check_lst_empty=[]
            for i in lst_of_field_lengths:
                check_lst_empty+=['']
            if lst_of_field_names==check_lst_empty: #checking if the field names are missing in the opened dbms
                    print(f'The database "{actual_opened_dbms}" is missing field names.\nPlease enter them and then add your desired record(s).')
                    lst_of_field_names=[]
                    while True:
                        for i, length in enumerate(lst_of_field_lengths, 1):
                            while True:
                                field_name = input(f'Enter name of field {i} (Length {length}): ')
                                if len(field_name) <= length:
                                    lst_of_field_names.append(field_name)
                                    break # move to the next field name entry
                                else:
                                    print(f'Field length of field {i} violated.')
                                    print('Do you want to enter the name of this field again ?')
                                    cont=input('Enter yes or no : ').strip().lower()
                                    if cont=='yes':
                                        continue
                                    elif cont=='no':
                                        lst_of_field_names.append('_') # Add empty entry
                                        break
                                    else:
                                        print('Invalid choice')
                                        continue
                        if len(lst_of_field_names) == len(lst_of_field_lengths):  # Ensure full valid row before writing

                            #  Update CSV file with headers if they don't exist
                            with open(data_file, mode='w', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow(lst_of_field_names)
                            #  Update system file with the newly entered field names (keeping existing lengths)
                            with open(system_file, 'w') as f:
                                for i, length in enumerate(lst_of_field_lengths):
                                    f.write(f'NAME OF FIELD {i + 1}     : '+lst_of_field_names[i]+ '\n')
                                    f.write(f'LENGTH OF FIELD {i + 1}   : {length}\n')
                            print(f'Field names for database "{actual_opened_dbms}" have been set successfully!')
                            break
                        else:
                            print('''Number of field names given are not equal to the number of field 
field lengths specified. Please enter the field names again.''')
                            continue    

            #  Proceed to adding records as normal
            with open(data_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                while True:
                    entry_lst = []  # Row entries
                    for i, length in enumerate(lst_of_field_lengths):
                        while True:  # Keep asking until a valid entry is given
                            entry = input(f'Enter details of field {i + 1} ({lst_of_field_names[i]}) : ')
                            if len(entry) <= length:
                                entry_lst.append(entry)
                                break  # Move to the next field
                            else:
                                print(f'Field length of field {i + 1} violated.')
                                print('Do you want to enter the details of this field again ?')
                                cont=input('Enter yes or no : ').strip().lower()
                                if cont=='yes':
                                    continue
                                elif cont=='no':
                                    entry_lst.append('_')  # Add empty entry
                                    break
                                else:
                                    print('Invalid choice')
                                    continue

                    if len(entry_lst) == len(lst_of_field_lengths):  # Ensure full valid row before writing
                        writer.writerow(entry_lst)
                        cont = input("Do you want to add another record? (yes/no): ").strip().lower()
                        if cont != 'yes':
                            break
                    else:
                        print('''Some records are missing. Please enter the details of the fields again.''')
                        continue    


            print(f"Changes have been made in your database {actual_opened_dbms} \U0001F60A")
            return


def edit_existing_record(lower_case_desired_dbms):
 while True: 
    choice=input('''Confirm that you want to edit an existing record (yes/no) : ''').strip().lower()
    if  choice.strip()=='no':
        print('Exiting without proceeding')
        return
    elif  choice.strip()!='yes' and  choice.strip()!='no':
        print('Invalid choice')
        continue
    elif choice.strip()=='yes':      
        lst_actual_existing_dbms = os.listdir(databases_folder)
        lower_case_lst_existing_dbms=[dbms.strip().lower() for dbms in lst_actual_existing_dbms]
        if lower_case_desired_dbms not in lower_case_lst_existing_dbms:
            print(f'DATABASE {lower_case_desired_dbms} does not exist')
            return
        actual_opened_dbms = lst_actual_existing_dbms[lower_case_lst_existing_dbms.index(lower_case_desired_dbms)]
        path_of_opened_dbms = os.path.join(databases_folder, actual_opened_dbms)
        data_file = os.path.join(path_of_opened_dbms, actual_opened_dbms + ".csv")
        system_file = path_of_opened_dbms + '/System file_' + actual_opened_dbms + '.txt'
        
        lst_of_field_names = []
        lst_of_field_lengths = []

        # Read system file to extract field lengths and field names
        with open(system_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(":")
                if "NAME OF FIELD" in line:
                    lst_of_field_names.append(parts[1].strip())
                elif "LENGTH OF FIELD" in line:
                    lst_of_field_lengths.append(int(parts[1].strip()))

        if not os.path.exists(data_file):
            print("Error: Data file not found!")
            return
        while True:
            # Read existing records
            with open(data_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                records = list(reader)  # Read all records into a list
            
            if len(records) < 2:
                print("No records available to edit.")
                return
            
            # Display existing records
            print("Existing Records:")
            for i, row in enumerate(records[1:], start=1):  # Skipping header row
                print(i, row)
            
            try:
                record_to_edit = int(input("Enter the record number to edit: "))
                if record_to_edit < 1 or record_to_edit >= len(records):
                    print("Invalid record number.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
            

            with open(data_file, mode='w', newline='') as file:                                                                                 
                writer = csv.writer(file)
                while True:
                        entry_lst = []  # Row entries
                        for i, length in enumerate(lst_of_field_lengths):
                            while True: # Keep asking until a valid entry is given  
                                entry = input(f'Enter details of field {i + 1} ({lst_of_field_names[i]}) : MAX LENGTH {length} :\n')
                                if len(entry) <= length:
                                    entry_lst.append(entry)
                                    break # Move to the next field
                                else:
                                    print(f'Field length of field {i + 1} violated.')
                                    print('Do you want to enter the details of this field again ?')
                                    cont=input('Enter yes or no : ').strip().lower()
                                    if cont=='yes':
                                        continue
                                    elif cont=='no':
                                        entry_lst.append('_')
                                        break
                                    else:
                                        print('Invalid choice')
                                        continue
                        if len(entry_lst) == len(lst_of_field_lengths):  # Ensure full valid row before writing
                            
                            # index assignment operation
                            records[record_to_edit]=entry_lst
                            writer.writerows(records)
                            break
                        else:
                            print('''Some records are missing. Please enter the details of the fields of this record again.''')
                            continue
                
            cont=input("Do you want to edit another existing record? (yes/no): ").strip().lower()
            if cont == 'yes':
                continue
            elif cont!='yes':
                break

        print(f"Changes have been made in your database {actual_opened_dbms} \U0001F60A")
        return

def display_selected_record(lower_case_desired_dbms):
    while True: 
        choice=input('''Confirm that you want to display the record(s) you\'ll select (yes/no) : ''').strip().lower()
        if  choice.strip()=='no':
            print('Exiting without proceeding')
            return
        elif  choice.strip()!='yes' and  choice.strip()!='no':
            print('Invalid choice')
            continue
        elif choice.strip()=='yes':      
            lst_actual_existing_dbms = os.listdir(databases_folder)
            lower_case_lst_existing_dbms=[dbms.strip().lower() for dbms in lst_actual_existing_dbms]
            if lower_case_desired_dbms not in lower_case_lst_existing_dbms:
                print(f'DATABASE {lower_case_desired_dbms} does not exist')
                return
            actual_opened_dbms = lst_actual_existing_dbms[lower_case_lst_existing_dbms.index(lower_case_desired_dbms)]
            path_of_opened_dbms = os.path.join(databases_folder, actual_opened_dbms)
            data_file = os.path.join(path_of_opened_dbms, actual_opened_dbms + ".csv")
            with open(data_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                records = list(reader)  # Convert CSV rows into a list of dictionaries
            if not records:
                print("The database is empty!")
                return
            # Show available fields to the user
            available_fields = list(records[0].keys())
            lower_case_available_fields=[f.strip().lower() for f in available_fields]
            print('AVAILABLE FIELDS TO SEARCH BY ARE AS FOLLOWS :')
            for field_name,i in zip(available_fields,range(len(available_fields))):
                print(f'{i+1}'+'-'+f'{field_name}')
            
            while True:
                # Ask the user for field name and value
                searched_field = input("Enter the field name through which you want to search your desired record : ").strip()
                # Validate field
                if searched_field.lower() not in lower_case_available_fields:
                    print(f'Invalid field! Choose one field from the following :')
                    for field_name,i in zip(available_fields,range(len(available_fields))):
                        print(f'{i+1}'+'-'+f'{field_name}')
                    continue
                actual_searched_field_name=available_fields[lower_case_available_fields.index(searched_field.lower())]
                searched_value = input(f"Enter the value of {actual_searched_field_name} to search for: ").strip()
                # Search for matching records
                matching_records = [record for record in records if record[actual_searched_field_name] == searched_value]
                # Display results
                if matching_records:
                    print("\nMatching Record(s):\n")
                    for record in matching_records:
                        print(record, "\n")  # Adds a new line for readability
                    cont=input('Do you want to selecet another record specifically (yes/no) ?  ').strip().lower()
                    if cont!='yes':
                        break
                    elif cont=='yes':
                        continue
                else:
                    print("No matching record found.")
                    break
            return


def find_database(name_of_dbms: str):
    # Check if the database folder already exists
    database_path = os.path.join(databases_folder, name_of_dbms)
    return os.path.isdir(database_path)


def create_database():
    while True:
        choice=input('''Press 1 to confirm creating a new database.\nPress 2 to exit without creating a new database : \n''')
        if choice=='2':
                return
        elif choice!='1' and choice!='2':
                print('Invalid choice')
                continue
        elif choice=='1':
                name_of_dbms = input('Enter the name of database you want to create : ').strip()
                if not name_of_dbms:
                    print('Name of database can\'t be empty')
                    return
                
                # Check if the database already exists
                if find_database(name_of_dbms):
                    print(f'Database \"{name_of_dbms}\" already exists.')
                    return

                # Create folder for the new database
                individual_database_folder = os.path.join(databases_folder, name_of_dbms)
                os.makedirs(individual_database_folder)

                # Paths for the data file and system file
                data_file_path = os.path.join(individual_database_folder, name_of_dbms + ".csv")
                system_file_path = os.path.join(individual_database_folder, 'System file_' + name_of_dbms + '.txt')
                while True:  
                    try: 
                            no_of_fields = int(input('Enter the number of fields you want to have in your database: '))
                            lst_of_field_lengths = []
                            lst_of_field_names = []  # List containing field names
                            if no_of_fields <= 0:
                                print('\nNumber of fields can be specified only as a positive integer.')
                                continue
                            for index in range(1, no_of_fields + 1):
                                len_of_each_field = int(input(f'Enter length of field {index}: '))
                                if len_of_each_field <= 0:
                                    print('It can be only specified as a positive integer.\nEnter again the number of fields and then their respecctive lengths')
                                    continue
                                lst_of_field_lengths.append(len_of_each_field)
                    except ValueError:
                            print('Number of fields can be specified only as a positive integer.\nEnter again the number of fields and then their respecctive lengths')
                            continue
                    for index in range(1,len(lst_of_field_lengths)+1):
                            field_name = input(f'Enter name of field {index} : ')
                            lst_of_field_names.append(field_name)

                    if len(lst_of_field_names)!=len(lst_of_field_lengths):
                        print('Number of field names given should be equal to the number of field lengths given.\nEnter again the number of fields and then their respecctive lengths')
                        continue                 

                    for i in range(len(lst_of_field_names)):
                        if len(lst_of_field_names[i]) > lst_of_field_lengths[i]:
                            print(f'Field length of field {i + 1} violated.')
                            lst_of_field_names[i] = input(f'Enter name of field {i + 1} again: ')
                    break
                # Open the data file in write mode
                with open(data_file_path, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(lst_of_field_names)  # Writing field names
                with open(data_file_path, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    while True:
                        # Get user input for rows
                        lst_row_records = []  # Row entries
                        for index, length_specified in enumerate(lst_of_field_lengths):
                            while True:  # Keep asking until a valid entry is given
                                individual_row_entry= input(f'Enter details of field {index + 1} ({lst_of_field_names[index]}) : MAX LENGTH {length_specified} : \n')
                                if len(individual_row_entry) <= length_specified:
                                    lst_row_records.append(individual_row_entry)
                                    break  # Move to the next field
                                else:
                                    print(f'Field length of field {index + 1} violated.')
                                    continue  # Prevent invalid entry
                        # Write the row
                        writer.writerow(lst_row_records)

                        # Check if user wants to continue
                        cont = input("Do you want to add another record? (yes/no): ").strip().lower()
                        if cont != 'yes':
                            break
                # Create the system file containing meta data
                with open(system_file_path, 'w') as f:
                    for index, length_specified in enumerate(lst_of_field_lengths):
                        f.write(f'NAME OF FIELD {index + 1}     : {lst_of_field_names[index]} \n')
                        f.write(f'LENGTH OF FIELD {index + 1}   : {length_specified}\n')

                print(f"Your Database {name_of_dbms} has been created successfully.\U0001F60A \nData has been saved to {data_file_path} in tabular format.")
                break
    return
  
def open_database():
  while True: 
    choice=input('Press 1 to confirm opening an existing database :\nPress 2 to exit without opening an existing database : \n')
    if choice=='2':
        return
    elif choice!='1' and choice!='2':
        print('Invalid choice')
        continue
    elif choice=='1':
        if not os.path.isdir(databases_folder):
            print('Directory containing databases not found !')
            return
        elif os.path.isdir(databases_folder):
            lst_actual_existing_dbms=os.listdir(databases_folder)
            if lst_actual_existing_dbms==[]:
                print('There are no pre existing databases !')
                return
            print('ALREADY EXISTING DATABASES ARE AS FOLLOWS : ')
            for dbms,i in zip(lst_actual_existing_dbms,range(len(lst_actual_existing_dbms))):
                print(str(i+1)+'-'+dbms)
            user_entered_desired_dbms=input('Enter the name of database you want to open : ')    
            lower_case_desired_dbms=user_entered_desired_dbms.strip().lower()
            lower_case_lst_existing_dbms=[dbms.strip().lower() for dbms in lst_actual_existing_dbms]
            if lower_case_desired_dbms not in lower_case_lst_existing_dbms:
                print(f'DATABASE {user_entered_desired_dbms} does not exist')
                return
            elif lower_case_desired_dbms in lower_case_lst_existing_dbms:
                actual_opened_dbms = lst_actual_existing_dbms[lower_case_lst_existing_dbms.index(lower_case_desired_dbms)]
                i=0
                while True:
                    if i>0:
                        print('\n')
                        print(f'DATABASE {actual_opened_dbms} HAS BEEN OPENED AGAIN : \n')
                        print(f'WELCOME BACK TO DATABASE {actual_opened_dbms} AGAIN \U0001F60A') #unicode of emoji
                    else:    
                        print(f'DATABASE {actual_opened_dbms} HAS BEEN OPENED : \n')
                        print(f'WELCOME TO DATABASE {actual_opened_dbms} \U0001F60A') #unicode of emoji
                    choice_inside_dbms=input('''\n
Press 1 to add record
Press 2 to delete a record
Press 3 to display all records
Press 4 to edit an existing record
Press 5 to display a selected record
Press 6 to exit the opened database\n''')

                    if choice_inside_dbms.strip()=='1':
                        add_record(lower_case_desired_dbms)
                        i+=1
                    elif choice_inside_dbms.strip()=='2':
                        delete_record(lower_case_desired_dbms)
                        i+=1
                    elif choice_inside_dbms.strip()=='3':
                        display_all_records(lower_case_desired_dbms)
                        i+=1
                    elif choice_inside_dbms.strip()=='4':
                        edit_existing_record(lower_case_desired_dbms)
                        i+=1
                    elif choice_inside_dbms.strip()=='5':
                        display_selected_record(lower_case_desired_dbms)
                        i+=1
                    elif choice_inside_dbms.strip()=='6':
                        return    
                    else:
                        print('INVALID CHOICE')
                        i+=1
                        continue
#main program
def main():
    while True:
        print("\nWelcome to CIS-NED DBMS \U0001F60A : ")
        print("Press 1 to create a new database")
        print("Press 2 to open an existing database")
        print("Press 3 to exit")

        choice = input("Please enter your choice: ").strip()

        match choice:
            case "1":
                create_database()
            case "2":
                open_database()
            case "3":
                print("Exiting CIS-NED DBMS. Goodbye! \U0001F60A ")
                break
            case _:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()    
    
