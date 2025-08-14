import streamlit as st
from main import ParkingLot
import streamlit as st

if "parking_lot" not in st.session_state:
    st.session_state.parking_lot = ParkingLot()

Parking_lot = st.session_state.parking_lot

 
 

 
if "show_sidebar" not in st.session_state:
    st.session_state.show_sidebar = False

# -------------------- Welcome Section --------------------
st.title("👋 Welcome to the Parking Lot System")
st.markdown("Click the button below to toggle parking availability view.")

# -------------------- Capture Button Click --------------------
toggle_clicked = st.button("🔍 Show Availability")

# -------------------- Toggle Sidebar State Immediately --------------------
if toggle_clicked:
    st.session_state.show_sidebar = not st.session_state.show_sidebar

# -------------------- Dynamic Button Label --------------------
 
     
if st.session_state.show_sidebar:
    all_spots = Parking_lot.manager.get_all_spots()
 

    with st.sidebar:
        st.subheader("🅿️ Parking Spot Grid")
        cols = st.columns(3)
        for i, spot in enumerate(all_spots):
            color = "#d4edda" if not spot.is_occupied() else "#f8d7da"
            with cols[i % 3]:
                st.markdown(
                    f"""
                    <div style='
                        background-color:{color};
                        padding:10px;
                        margin:5px;
                        border-radius:6px;
                        text-align:center;
                        font-size:14px;
                        font-weight:bold;
                        box-shadow: 0 0 3px rgba(0,0,0,0.1);
                    '>
                        {spot.get_id()}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# -------------------- Park Vehicle Form --------------------
st.subheader("🚗 Park a Vehicle")

with st.form("park_vehicle_form"):
    vehicle_number = str(st.text_input("Vehicle Number"))
    vehicle_type = str(st.selectbox("Parking Type", ["LargeParkingSpot", "CompactParkingSpot", "BikeParkingSpot","HanicappedParkingSpot"]))
     

     

    submitted = st.form_submit_button("Park Vehicle")

    if submitted:
        result = Parking_lot.park_vehicle(vehicle_type,vehicle_number)
        if result:
            st.success(f"✅ Vehicle parked at spot {result.get_id()} with ticketid is {result.ticket_id}")
            all_spots = Parking_lot.manager.get_all_spots()  # Refresh grid
        else:
            st.error("❌ No available spot for this vehicle type.")

# -------------------- Unpark Vehicle Form --------------------
st.subheader("🚙 Unpark a Vehicle")

with st.form("unpark_vehicle_form"):
    ticket_id = st.text_input("Enter Ticket ID")
    payment_method = st.selectbox("Payment Method", ["Cash", "CreditCard"])
    unpark_submit = st.form_submit_button("Unpark Vehicle")

    if unpark_submit:
        try:
            res=Parking_lot.unpark_vehicle(ticket_id, payment_method)
            if res=='Invalid Payment':
              st.write("Please select payment method")
            elif res=='invalid ticketid':
              st.write("Inavld ticket id")

            else:
              st.success("✅ Vehicle unparked successfully.")
              all_spots = Parking_lot.manager.get_all_spots()  # Refresh grid
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
