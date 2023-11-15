import streamlit as st
from database import (
    add_data_enter,
    add_data_exit,
    add_data_student,
    add_data_teacher,
    remove_data_parking_lot,
    remove_data_student,
    remove_data_teacher,
    add_data_parking_lot,
)

#################################################### Security Guard ###################################################
def create_enter():
    Enter_date = st.date_input("Date:")
    Veh_type = st.selectbox("Type:", ["Two wheeler", "Four wheeler"])
    Owner_type = st.selectbox("Owner Type:", ["Teacher", "Student"])
    Veh_No = st.text_input("Vehicle_no:")
    Parking_id = st.text_input("Parking_id:")
    id = st.text_input("ID:")
    if st.button("Add Vehicle"):
        add_data_enter(Enter_date, Veh_type, Owner_type, Veh_No, Parking_id, id)
        

def create_exit():
    Exit_date = st.date_input("Date:")
    Parking_id = st.text_input("Parking_id:")
    id = st.text_input("ID:")
    if st.button("Search Vehicle"):
        add_data_exit(Exit_date, id,Parking_id)
        

# -------------------------------------------------------------- Admin ------------------------------------------------------------#

def create_add_student():
    Contact = st.text_input("Contact:")
    ID = st.text_input("ID:")
    Name = st.text_input("Name")
    Semester = st.text_input("Semester")
    if st.button("Add Student"):
        add_data_student(Contact, ID, Name, Semester)
        st.success("Successfully added Student record: {}".format(ID))

def create_remove_student():
    ID = st.text_input("ID:")
    if st.button("Remove Student"):
        remove_data_student(ID)
        st.success("Successfully Removed Student record: {}".format(ID))

def create_add_teacher():
    Contact = st.text_input("Contact:")
    ID = st.text_input("ID:")
    Name = st.text_input("Name")
    if st.button("Add Teacher"):
        add_data_teacher(Contact, ID, Name)
        st.success("Successfully added Teacher record: {}".format(ID))

def create_remove_teacher():
    ID = st.text_input("ID:")
    if st.button("Remove Teacher"):
        remove_data_teacher(ID)
        st.success("Successfully removed Teacher record: {}".format(ID))

def create_add_parking_lot():
    Parking_id = st.text_input("Parking ID:")
    Status = st.selectbox("Status", ["Active", "Occupied"])
    if st.button("Add Parking Lot"):
        add_data_parking_lot(Parking_id, Status)
        st.success("Successfully added Parking Lot: {}".format(Parking_id))

def create_remove_parking_lot():
    Parking_id = st.text_input("Parking ID:")
    if st.button("Remove Parking Lot"):
        remove_data_parking_lot(Parking_id)
        st.success("Successfully removed Parking Lot: {}".format(Parking_id))
