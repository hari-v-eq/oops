import mysql.connector

def get_connection():
    connection=mysql.connector.connect(
    host="localhost",
    database="test",
    port=3307,
    username="root",
    password="")

    return connection

def close_connection(connection):
    if connection:
        connection.close()
def main():

    print("-----------------------------------------")
    print("""Available Tables to make changes: 
            
            E=Employee,
            C=Company """)

    choice = input('Choose your option = ')
    if choice == 'E' or choice=='e':       
        print("Creating your data----")
        common_1()
        
    elif choice == 'C' or choice=='c':       
        print("Creating your data----")
        common_2()
    else:
        print("wrong Input")

def common_1():
    print("""Available Options: 
            C=Create, 
            R=Read, 
            U=Update, 
            D=Delete """)
    choice = input('Choose your option = ')
    if choice == 'C' or choice=='c':
        print("Creating your data----")
        createObj=CRUD()
        createObj.func_CreateData_e()
    elif choice == 'R' or choice=='r':
        print("Reading your data: ")
        readObj =CRUD()
        readObj.func_ReadData_e()
    elif choice == 'U' or choice=='u':
        print("Updating your data: ")
        updateObj =CRUD()
        updateObj.func_UpdateData_e()
    elif choice == 'D' or choice=='d':
        print("Deleting your data: ")
        deleteObj =CRUD()
        deleteObj.func_DeleteData_e()
    else:
        print('Wrong choice, Thank u')

def common_2():
    print("""Available Options: 
            C=Create, 
            R=Read, 
            U=Update, 
            D=Delete """)
    choice = input('Choose your option = ')
    if choice == 'C' or choice=='c':
        print("Creating your data----")
        createObj=CRUD()
        createObj.func_CreateData_c()
    elif choice == 'R' or choice=='r':
        print("Reading your data: ")
        readObj =CRUD()
        readObj.func_ReadData_c()
    elif choice == 'U' or choice=='u':
        print("Updating your data: ")
        updateObj =CRUD()
        updateObj.func_UpdateData_c()
    elif choice == 'D' or choice=='d':
        print("Deleting your data: ")
        deleteObj =CRUD()
        deleteObj.func_DeleteData_c()
    else:
        print('Wrong choice, Thank u')

class CRUD:
             
    def func_CreateData_e(self):
                
        # Get the sql connection
            connection =get_connection()
            cursor = connection.cursor()
            
            name = input('Enter Name = ')
            age = input('Enter Age = ')

            try:       
                
                query = "Insert Into employee (Name, Age) Values (%s,%s)" 
                cursor =connection.cursor()
                # Execute the sql query
                cursor.execute(query, [name, age])
                # Commit the datac
                connection.commit()
                print('Data Saved Successfully')

            except:
                print('Something wrong, please check')

            finally:
                # Close the connection
                connection.close()
        
    def func_ReadData_e(self):
           
        # Get the sql connection
        connection =get_connection()
        cursor = connection.cursor()
        # Execute the sql query
        cursor.execute('Select * from employee')        
        # Print the data
        for i in cursor:
            print("data: ",i)
            #print('row = %r' % (i,))

    def func_UpdateData_e(self):
        # Get the SQL connection
        connection = get_connection()

        id = input('Enter Employee Id = ')
    
        try:
            # Fetch the data which needs to be updated
            sql = "Select * From employee Where Id = %s" 
            cursor = connection.cursor()
            cursor.execute(sql, [id,])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t Name\t\t\t Age')
            print('-------------------------------------------')       
            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            print('Enter New Data To Update Employee Record ')

            name = input('Enter New Name = ')
            age = input('Enter New Age = ')
            query = "Update employee Set Name = %s, Age =%s Where Id =%s" 
        
            # Execute the update query
            cursor.execute(query, [name, age, id,])
            connection.commit()

            #to show the updated data
            sql = "Select * From employee Where Id = %s" 
            cursor = connection.cursor()
            cursor.execute(sql, [id,])
            item = cursor.fetchone()

            print("Udpated data: ")
            print('Data Fetched for Id = ', id)
            print('ID\t\t Name\t\tAge')
            print('-------------------------------------------')       
            print(' {}\t\t {} \t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            print('Data Updated Successfully')

        except:
            print('Something wrong, please check')

        finally:
           # Close the connection
            connection.close()

    def func_DeleteData_e(self):
        # Get the SQL connection
        connection = get_connection()
        id = input('Enter Employee Id = ')
    
        try:
            # Get record which needs to be deleted
            sql = "Select * From employee Where Id = %s" 
            cursor = connection.cursor()
            cursor.execute(sql, [id])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t Name\t\tAge')
            print('-------------------------------------------')       
            print(' {}\t\t {} \t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            confirm = input('Are you sure to delete this record (Y/N)?')

            # Delete after confirmation
            if confirm == 'Y':
                deleteQuery = "Delete From employee Where Id = %s"
                cursor.execute(deleteQuery,[id,])
                connection.commit()
                print('Data deleted successfully!')
            else:
                print('Wrong Entry')
        except:
            print('Something wrong, please check')
        finally:
            connection.close()
             
    def func_CreateData_c(self):
                
        # Get the sql connection
            connection =get_connection()
            cursor = connection.cursor()
            
            c_name = input('Enter company Name = ')
            location = input('Enter Location = ')

            try:       
                
                query = "Insert Into company (c_name, location) Values (%s,%s)" 
                cursor =connection.cursor()
                # Execute the sql query
                cursor.execute(query, [c_name, location,])
                # Commit the data
                connection.commit()
                print('Data Saved Successfully')

            except:
                print('Something wrong, please check')

            finally:
                # Close the connection
                connection.close()
        
    def func_ReadData_c(self):
           
        # Get the sql connection
        connection =get_connection()
        cursor = connection.cursor()
        # Execute the sql query
        cursor.execute('Select * from company')        
        # Print the data
        for i in cursor:
            print("data: ",i)

    def func_UpdateData_c(self):
        # Get the SQL connection
        connection = get_connection()

        id = input('Enter Company Id = ')
    
        try:
            # Fetch the data which needs to be updated
            sql = "Select * From company Where Id = %s" 
            cursor = connection.cursor()
            cursor.execute(sql, [id,])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t company_Name\t\t\t Location')
            print('-------------------------------------------')       
            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            print('Enter New Data To Update Company Record ')

            c_name = input('Enter New company Name = ')
            location = input('Enter New Location = ')
            query = "Update company Set c_name = %s, location =%s Where Id =%s" 
        
            # Execute the update query
            cursor.execute(query, [c_name, location, id,])
            connection.commit()

            #to show the updated data
            sql = "Select * From company Where Id = %s" 
            cursor = connection.cursor()
            cursor.execute(sql, [id,])
            item = cursor.fetchone()

            print("Udpated data: ")
            print('Data Fetched for Id = ', id)
            print('ID\t\t company_Name\t\t\t Location')
            print('-------------------------------------------')       
            print(' {}\t\t {} \t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            print('Data Updated Successfully')

        except:
            print('Something wrong, please check')

        finally:
           # Close the connection
            connection.close()

    def func_DeleteData_c(self):
        # Get the SQL connection
        connection = get_connection()
        id = input('Enter Company Id = ')
    
        try:
            # Get record which needs to be deleted
            sql = "Select * From company Where Id = %s" 
            cursor = connection.cursor()
            cursor.execute(sql, [id])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t company_Name\t\t Location')
            print('-------------------------------------------')       
            print(' {}\t\t {} \t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            confirm = input('Are you sure to delete this record (Y/N)?')

            # Delete after confirmation
            if confirm == 'Y':
                deleteQuery = "Delete From company Where Id = %s"
                cursor.execute(deleteQuery,[id,])
                connection.commit()
                print('Data deleted successfully!')
            else:
                print('Wrong Entry')
        except:
            print('Something wrong, please check')
        finally:
            connection.close()

main()            
CRUD()

