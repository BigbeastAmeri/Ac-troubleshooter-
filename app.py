import streamlit as st
from openai import OpenAI

api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)
st.set_page_config(page_title="Itech AI", page_icon="🔧", layout="wide")

st.title("Itech AI - Electronics Repair Assistant")
st.caption("USA-based AI diagnostics for HVAC, Refrigeration, TVs & Home Appliances")
st.markdown("**⚠️ Disclaimer:** Itech AI provides troubleshooting guidance only. For electrical, gas, or refrigerant work, contact a licensed technician in your state. Use at your own risk.")
st.divider()


14 user_input = st.text_input("Describe your appliance issue: E.g. AC not cooling", key="input_box")
15 zip_code = st.text_input("Enter your US ZIP code for local technician referrals: E.g. 90210", max_chars=5, key="zip_box")
16 col1, col2, col3 = st.columns([1,2,1])
17 with col2:
18     send_btn = st.button("🔧 Diagnose My Appliance", type="primary", use_container_width=True)

if send_btn and user_input:
    with st.spinner("Itech AI is diagnosing... 🔧"):
22     prompt = f"""
23     You are Itech AI, a USA-based certified appliance technician.
24     Customer location: ZIP {zip_code if zip_code else 'Not provided'}
25     
26     RULES:
27     1. Safety first: Always start with 'UNPLUG the appliance before inspection'
28     2. Only diagnose electronics: HVAC, Refrigeration, TVs, Washing Machines
29     3. Give 3 clear troubleshooting steps in plain English
30     4. End with: 'If this doesn't work, contact a licensed HVAC technician in ZIP {zip_code if zip_code else 'your area'}'
31     
32     Customer problem: {user_input}
33     """
        
 34
35 # TEST MODE - USA Standard: Show what AI will send
36 st.write("**Itech AI Prompt:**")
37 st.code(prompt)
38 st.success("✅ Prompt built correctly! Add API key next for real diagnosis")
39
40 # TODO: Uncomment below after adding API key
41 # response = client.chat.completions.create(
42 # model="gpt-4o-mini",
43 # messages=[
44 # {"role": "system", "content": prompt},
45 # {"role": "user", "content": user_input}
46 # ],
47 # temperature=0.3
48 # )
49 # st.write(response.choices[0].message.content) 
