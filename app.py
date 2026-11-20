"""Credit Card Customer Segmentation - Streamlit app.
Run:  streamlit run app.py   (keep cc_scaler.pkl and cc_segmentation_model.pkl in the same folder)"""
import joblib
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Credit Card Segmentation", page_icon="💳", layout="wide")


@st.cache_resource
def load():
    return joblib.load("models/cc_scaler.pkl"), joblib.load("models/cc_segmentation_model.pkl")


def add_features(d, raw_cols):
    f = d[raw_cols].copy()
    t = f["TENURE"].clip(lower=1)
    f["Monthly_Avg_Purchase"] = f["PURCHASES"] / t
    f["Monthly_Avg_Cash_Advance"] = f["CASH_ADVANCE"] / t
    f["Limit_Usage"] = np.where(f["CREDIT_LIMIT"] > 0, f["BALANCE"] / f["CREDIT_LIMIT"].where(f["CREDIT_LIMIT"] > 0, 1), 0)
    f["Payment_to_Minpayment_Ratio"] = f["PAYMENTS"] / (f["MINIMUM_PAYMENTS"] + 1)
    return f


def preprocess(raw_df, b):
    f = add_features(raw_df, b["raw_columns"])
    for c, u in b["caps"].items():
        f[c] = f[c].clip(upper=u)
    f[b["log_cols"]] = np.log1p(f[b["log_cols"]])
    return f[b["feature_columns"]]


try:
    scaler, bundle = load()
except FileNotFoundError:
    st.error("cc_scaler.pkl / cc_segmentation_model.pkl not found. Run the notebook first and keep them next to app.py.")
    st.stop()

d = bundle["defaults"]
st.title("💳 Credit Card Customer Segmentation")
st.caption(f"Model: {bundle['algorithm']} · {len(bundle['personas'])} segments. Enter a cardholder's behaviour to get their segment and the recommended action.")

money = {"BALANCE": "Balance", "PURCHASES": "Total purchases", "ONEOFF_PURCHASES": "One-off purchases", "INSTALLMENTS_PURCHASES": "Instalment purchases",
         "CASH_ADVANCE": "Cash advance", "CREDIT_LIMIT": "Credit limit", "PAYMENTS": "Payments", "MINIMUM_PAYMENTS": "Minimum payments"}
freq = {"BALANCE_FREQUENCY": "Balance frequency", "PURCHASES_FREQUENCY": "Purchases frequency", "ONEOFF_PURCHASES_FREQUENCY": "One-off purchase frequency",
        "PURCHASES_INSTALLMENTS_FREQUENCY": "Instalment purchase frequency", "CASH_ADVANCE_FREQUENCY": "Cash advance frequency", "PRC_FULL_PAYMENT": "Share of full payments"}
cnt = {"CASH_ADVANCE_TRX": "Cash advance transactions", "PURCHASES_TRX": "Purchase transactions"}

vals, cols = {}, st.columns(4)
for i, (k, lab) in enumerate(money.items()):
    vals[k] = cols[i % 4].number_input(lab, min_value=0.0, value=float(round(d[k], 2)), step=100.0)
with st.expander("Frequencies, transaction counts and tenure", expanded=True):
    c2 = st.columns(4)
    for i, (k, lab) in enumerate(freq.items()):
        vals[k] = c2[i % 4].slider(lab, 0.0, 1.0, float(round(min(d[k], 1.0), 2)), 0.01)
    for i, (k, lab) in enumerate(cnt.items()):
        vals[k] = float(c2[(len(freq) + i) % 4].number_input(lab, min_value=0, value=int(d[k]), step=1))
    vals["TENURE"] = float(c2[(len(freq) + len(cnt)) % 4].slider("Tenure (months)", 6, 12, int(d["TENURE"])))

if st.button("Predict segment", type="primary"):
    row = pd.DataFrame([{**d, **vals}])
    c = int(bundle["model"].predict(scaler.transform(preprocess(row, bundle)))[0])
    p = bundle["personas"][c]
    st.success(f"**Segment: {p['name']}**  (cluster {c})")
    st.info(f"**Recommended action:** {p['action']}")
    st.caption(f"Why: {p['why']}")
    prof = bundle["profile"].copy()
    prof.insert(0, "Persona", [bundle["personas"][k]["name"] for k in prof.index])
    st.subheader("Segment profiles (average values)")
    st.dataframe(prof.style.format(precision=2, thousands=",").apply(lambda r: ["background-color:#fff3cd" if r.name == c else "" for _ in r], axis=1))
