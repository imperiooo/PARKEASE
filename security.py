import streamlit as st
from create import create_enter ,create_exit
from database import create_table_vehicle_enter
from read import read_no_vehicles, read_data_vehicle_amount

def main2():
    st.title("SECURITY GUARD")
    menu2 = ["Vehicle ENTER", "Vehicle EXIT","Vehicle COUNT", "Vehicle Parking Fee"]  # Added "Parking Transactions"
    choice = st.sidebar.selectbox("Menu", menu2)

    if choice == "Vehicle ENTER":
        create_table_vehicle_enter()
        st.subheader("Enter Details:")
        create_enter()

    elif choice == "Vehicle EXIT":
        #create_table_vehicle_exit()
        st.subheader("Exit Details:")
        create_exit()

    elif choice == "Vehicle COUNT":
        read_no_vehicles()

    elif choice == "Vehicle Parking Fee":
        st.subheader("Amount per vehicle")
        read_data_vehicle_amount()
