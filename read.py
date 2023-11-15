import pandas as pd
import streamlit as st
from database import (
    view_vehicle_entered,
    count_vehicles,
    show_parking_lots,
    read_amount as read_vehicle_amount,
    read_records_count as read_vehicle_records_count,
    faculty_not_parked,
    student_not_parked,
    read_vehicle_types,
)

def read_vehicles():
    result = view_vehicle_entered()
    df = pd.DataFrame(result, columns=['Date', 'Type', 'OwnerType', 'VehicleNumber', 'ParkingID', 'ID'])
    with st.expander("View all vehicle details"):
        st.dataframe(df)

def read_no_vehicles():
    result = count_vehicles()
    df = pd.DataFrame(result, columns=['Vehicle Count'])
    with st.expander("All the vehicles inside"):
        st.dataframe(df)

def read_parking_lots():
    result = show_parking_lots()
    df = pd.DataFrame(result, columns=['Parking ID', 'Status'])
    with st.expander("Status of the Parking slots"):
        st.dataframe(df)

def read_data_vehicle_amount():
    result = read_vehicle_amount()
    df = pd.DataFrame(result, columns=['VehicleNumber', 'Amount'])
    with st.expander("Amount per vehicle"):
        st.dataframe(df)

def read_data_vehicle_records_count():
    result = read_vehicle_records_count()
    df = pd.DataFrame(result, columns=['Total records', 'Owner Type', 'Date'])
    with st.expander("Number of records per teacher and student"):
        st.dataframe(df)

def read_not_faculty():
    result = faculty_not_parked()
    df = pd.DataFrame(result, columns=['Contact', 'ID', 'Name'])
    with st.expander("Faculty that haven't used parking"):
        st.dataframe(df)

def read_not_student():
    result = student_not_parked()
    df = pd.DataFrame(result, columns=['Contact', 'ID', 'Name', 'Semester'])
    with st.expander("Student that haven't used parking"):
        st.dataframe(df)

def read_data_vehicle_types():
    result = read_vehicle_types()
    df = pd.DataFrame(result, columns=['Type ID', 'Type Name','Owner ID','Vehicle No'])
    with st.expander("Vehicle Types"):
        st.dataframe(df)

def read_records_count():
    result = read_vehicle_records_count()  # Assuming this is the correct function name
    df = pd.DataFrame(result, columns=['Total records', 'Owner Type', 'Date'])
    with st.expander("Number of records per teacher and student"):
        st.dataframe(df)
