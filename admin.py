import streamlit as st
from read import (
    read_vehicles,
    read_parking_lots,
    read_records_count,
    read_not_faculty,
    read_not_student,  
    read_data_vehicle_types, 
)
from create import (
    create_add_parking_lot,
    create_remove_parking_lot,
    create_add_student,
    create_remove_student,
    create_add_teacher,
    create_remove_teacher,
)
from database import (
    create_table_parking_lot,
    create_table_student,
    create_table_teacher,
    create_table_vehicle_type,
)

def main1():
    st.title("ADMIN")
    menu = [
        "Add Student",
        "Remove Student",
        "Add Teacher",
        "Remove Teacher",
        "View Vehicles Entered",
        "Add Parking Lot",
        "Remove Parking Lot",
        "Show Parking Lots",
        "Number of parking lots occupied",
        "Teachers not parked",
        "Students not parked",
        "Vehicle Types"
    ]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table_student()
    create_table_teacher()
    create_table_parking_lot()
    create_table_vehicle_type()

    if choice == "Add Student":
        st.subheader("Enter Student Details To Be Added:")
        create_add_student()

    elif choice == "Remove Student":
        st.subheader("Enter Student Details To Be Removed:")
        create_remove_student()

    elif choice == "Add Teacher":
        st.subheader("Enter Teacher Details To Be Added:")
        create_add_teacher()

    elif choice == "Remove Teacher":
        st.subheader("Enter Teacher Details To Be Removed:")
        create_remove_teacher()

    elif choice == "View Vehicles Entered":
        st.subheader("Vehicles Entered:")
        read_vehicles()

    elif choice == "Add Parking Lot":
        st.subheader("Enter Parking Lot Details To Be Added:")
        create_add_parking_lot()

    elif choice == "Remove Parking Lot":
        st.subheader("Enter Parking Lot Details To Be Removed:")
        create_remove_parking_lot()

    elif choice == "Show Parking Lots":
        st.subheader("All Parking Lots:")
        read_parking_lots()

    elif choice == "Number of parking lots occupied":
        st.subheader("Number of parking lots occupied by teachers and students:")
        read_records_count()

    elif choice == "Teachers not parked":
        st.subheader("Parking lots not occupied by teachers:")
        read_not_faculty()

    elif choice == "Students not parked":
        st.subheader("Parking lots not occupied by students:")
        read_not_student()

    elif choice == "Vehicle Types":
        st.subheader("Vehicle Types:")
        read_data_vehicle_types()

if __name__ == "__main__":
    main1()
