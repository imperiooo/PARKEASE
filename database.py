import pymysql
import streamlit as st
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="Chocku$6",
    database="ParkEase"
)

c = mydb.cursor()

# ----------------------------------------------------Security Guard-------------------------------------------------#
def create_table_vehicle_enter():
    c.execute('CREATE TABLE IF NOT EXISTS Vehicle_in(Date DATE, Type TEXT, Owner_type TEXT, Vehicle_no varchar(50), P_id varchar(2),ID varchar(13))')
    mydb.commit()

def add_data_enter(Date, Type, Owner_type, Vehicle_no, Parking_id, id):
    # Check if the parking space is occupied
    c.execute('SELECT Status FROM parking_space WHERE Parking_id = %s', (Parking_id,))
    status_result = c.fetchone()

    if status_result and status_result[0] == 'Occupied':
        st.error("Sorry, the parking space {} is currently occupied. Cannot enter the vehicle.".format(Parking_id))
        # ("Successfully added Vehicle record: {}".format(Veh_No))
        # You can display a message to the user or handle the situation accordingly.
    else:
        # Parking space is available, proceed with adding the vehicle
        c.execute('INSERT INTO Vehicle_in(Date, Type, Owner_type, Vehicle_no, P_id, ID) VALUES (%s,%s,%s,%s,%s,%s)',
                  (Date, Type, Owner_type, Vehicle_no, Parking_id, id))
        c.execute('CALL StatusUpdation("{}")'.format(Parking_id))
        mydb.commit()
        st.success("Successfully added Vehicle record: {}".format(Vehicle_no))


def add_data_exit(Date, id,parking_id):
    # c.execute('SELECT P_id FROM Vehicle_in WHERE ID = %s', (id,))
    # parking_id_result = c.fetchone()

    # if parking_id_result:
    #     parking_id = parking_id_result[0]

        # Update the parking space status back to "Active"
    c.execute('UPDATE parking_space SET Status="Active" WHERE Parking_id = %s', (parking_id,))
    c.execute('DELETE FROM Vehicle_in WHERE ID = %s', (id,))
    st.success("Successfully exited Vehicle record: {}".format(id))
        # Insert the exit record into the Vehicle_out table
    #     c.execute('INSERT INTO Vehicle_out(Date, ID) VALUES (%s, %s)', (Date, id))
    #     mydb.commit()
    #     print(f"Vehicle with ID {id} exited successfully. Parking space {parking_id} status updated to 'Active'.")
    # # else:
    #     print(f"No entry record found for vehicle ID {id}. Cannot process exit.")

def count_vehicles():
    data=c.execute('SELECT COUNT(P_id) from Vehicle_in')
    data = c.fetchall()
    mydb.commit()
    return data

# ------------------------------------------------------Admin_Create---------------------------------------------------------#
def create_table_student():
    c.execute('CREATE TABLE IF NOT EXISTS student(Contact varchar(10), ID varchar(13), Name varchar(50), Semester INT)')
    mydb.commit()

def create_table_teacher():
    c.execute('CREATE TABLE IF NOT EXISTS faculty(Contact varchar(10), ID varchar(13), Name varchar(50))')
    mydb.commit()

def create_table_parking_lot():
    c.execute('CREATE TABLE IF NOT EXISTS parking_space(Parking_id varchar(2), Status TEXT)')
    mydb.commit()

def create_table_vehicle_type():
    c.execute('CREATE TABLE IF NOT EXISTS VehicleType (Type_ID INT AUTO_INCREMENT, TypeName VARCHAR(20) NOT NULL,O_type VARCHAR(20) NOT NULL,Vehicleid VARCHAR(20) NOT NULL, PRIMARY KEY(Type_ID))')
    mydb.commit()

# -------------------------------------Admin_data---------------------------------------------------------------------------

def add_data_student(Contact, ID, Name, Semester):
    c.execute('INSERT INTO student(Contact, ID , Name , Semester) VALUES (%s,%s,%s,%s)', (Contact, ID, Name, Semester))
    mydb.commit()

def remove_data_student(ID):
    c.execute('DELETE FROM student WHERE ID="{}"'.format(ID))
    mydb.commit()

def add_data_teacher(Contact, ID, Name):
    c.execute('INSERT INTO faculty(Contact , ID , Name ) VALUES (%s,%s,%s)', (Contact, ID, Name))
    mydb.commit()

def remove_data_teacher(ID):
    c.execute('DELETE FROM faculty WHERE ID="{}"'.format(ID))
    mydb.commit()

def add_data_parking_lot(Parking_id, Status):
    c.execute('INSERT INTO parking_space(Parking_id , Status) VALUES (%s,%s)', (Parking_id, Status))
    mydb.commit()

def remove_data_parking_lot(Parking_id):
    c.execute('DELETE FROM parking_space WHERE Parking_id="{}"'.format(Parking_id))
    mydb.commit()

def view_vehicle_entered():
    c.execute('SELECT Date,Type,Owner_type,Vehicle_no,P_id,ID FROM Vehicle_in')
    data = c.fetchall()
    return data

def show_parking_lots():
    c.execute('SELECT * FROM parking_space')
    data = c.fetchall()
    return data

def read_amount():
    c.execute('select vehicle_no,amount_calc(owner_type,type) from vehicle_in;')
    data = c.fetchall()
    return data

def read_records_count():
    c.execute('SELECT count(*) as total_records,Owner_type,Date  FROM Vehicle_in group by date,Owner_type;')
    data = c.fetchall()
    return data

def faculty_not_parked():
    c.execute('Select * from faculty where faculty.ID NOT IN (Select ID from Vehicle_in);')
    data = c.fetchall()
    return data

def student_not_parked():
    c.execute('Select * from student where student.ID NOT IN(Select ID from Vehicle_in);')
    data = c.fetchall()
    return data

def read_vehicle_types():
    c.execute('SELECT ID, Type ,Owner_type,Vehicle_no  FROM Vehicle_in')
    data = c.fetchall()
    return data
