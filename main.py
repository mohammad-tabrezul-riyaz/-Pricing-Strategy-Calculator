import streamlit as st

st.set_page_config(page_title="Pricing Strategy Calculator", layout="centered")

st.title("🧮 Pricing Strategy Calculator")
st.markdown("Quickly calculate your ideal selling price including GST and platform fees.")

# === INPUTS ===
cost = st.number_input("Product Cost (₹)", min_value=0.0, value=60.0, step=1.0)
profit_percent = st.number_input("Profit %", min_value=0.0, max_value=100.0, value=25.0)
profit_on = st.radio("Profit Based On", options=["Cost", "Selling Price"])
gst_percent = st.number_input("GST %", min_value=0.0, max_value=100.0, value=5.0)
platform_percent = st.number_input("Platform Commission % (Swiggy/Zomato)", min_value=0.0, max_value=100.0, value=20.0)

st.markdown("---")

# === CALCULATIONS ===
if profit_on == "Cost":
    base_sp = cost + (profit_percent / 100) * cost
elif profit_on == "Selling Price":
    base_sp = cost / (1 - (profit_percent / 100))

# Adjust for platform & GST
sp_after_commission = base_sp / (1 - (platform_percent / 100))
final_sp = sp_after_commission * (1 + (gst_percent / 100))

# === OUTPUT ===
st.subheader("📊 Final Output")
st.write(f"**Base Selling Price (before commission & GST): ₹{base_sp:.2f}**")
st.write(f"Platform Charges: ₹{sp_after_commission - base_sp:.2f}")
st.write(f"GST: ₹{final_sp - sp_after_commission:.2f}")
st.success(f"🎯 **Final Selling Price: ₹{final_sp:.2f}**")
