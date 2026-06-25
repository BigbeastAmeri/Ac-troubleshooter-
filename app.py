import streamlit as st
from openai import OpenAI

api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)
st.set_page_config(page_title="Itech AI", page_icon="🔧", layout="wide")

st.title("Itech AI - Electronics Repair Assistant")
st.caption("USA-based AI diagnostics for HVAC, Refrigeration, TVs & Home Appliances")
st.markdown("**⚠️ Disclaimer:** Itech AI provides troubleshooting guidance only. For electrical, gas, or refrigerant work, contact a licensed technician in your state. Use at your own risk.")
st.divider()


user_input = st.text_input("Describe your electronics problem:", key="input_box")
col1, col2, col3 = st.columns([1,2,1])
with col2:
    send_btn = st.button("🔧 Diagnose My Appliance", type="primary", use_container_width=True)

if send_btn and user_input:
    with st.spinner("Itech AI is diagnosing... 🔧"):

        # RULES FOR ITECH AI - PRIORITY 1
        rules = """You are Itech AI, an expert AC, Fridge, TV, Washing Machine & Electronics repair technician.

1. PRIORITY 1: First line must always be: "⚠️ SAFETY: UNPLUG from power socket before touching anything."
2. You ONLY answer electronics repair questions. AC, Fridge, TV, Washing Machine, Microwave, etc.
3. If user asks anything else like JAMB, school, relationship, etc, reply exactly: "I'm sorry, I'm Itech AI - I only fix electronics."
4. Give diagnosis + 3 simple fix steps. Use simple English + add tool needed if any.
5. End with: "If problem continues, call a certified technician."""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": rules},
                {"role": "user", "content": user_input}
            ],
            temperature=0.3
        )
        st.success("Diagnosis Complete:")
        st.write(response.choices[0].message.content)
