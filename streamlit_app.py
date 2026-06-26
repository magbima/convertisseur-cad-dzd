import streamlit as st

# ✅ CONFIG
st.set_page_config(
    page_title="Convertisseur Premium",
    page_icon="💱",
    layout="centered"
)

# ✅ STYLE ULTRA APP
st.markdown("""
<style>
.stApp {
    background: #0B0F1A;
    color: white;
}

/* TITLE */
h1 {
    text-align:center;
    color:#00E676;
}

/* CARD */
.card {
    background:#121826;
    padding:20px;
    border-radius:15px;
    margin-top:15px;
    text-align:center;
}

/* VALUE */
.value {
    font-size:28px;
    font-weight:bold;
}

/* FLAG */
.flag {
    font-size:20px;
}

/* ARROW BUTTON */
.arrow-btn {
    text-align:center;
    font-size:28px;
    margin:15px;
}
button {
    width:100%;
}
</style>
""", unsafe_allow_html=True)

# ✅ TITRE
st.title("💱 Convertisseur CAD ↔ DZD")

# ✅ TAUX
taux = st.number_input("Taux de change", value=170.0)

# ✅ SESSION STATE
if "mode" not in st.session_state:
    st.session_state.mode = "cad"

# ✅ INPUT CAD
cad = st.number_input("CAD", value=100.0)

# ✅ BOUTON INVERSE
if st.button("↕️ Inverser"):
    if st.session_state.mode == "cad":
        st.session_state.mode = "dzd"
    else:
        st.session_state.mode = "cad"

# ✅ INPUT DZD
dzd = st.number_input("DZD", value=0.0)

# ✅ LOGIQUE
if st.session_state.mode == "cad":
    dzd = cad * taux
else:
    cad = dzd / taux if taux != 0 else 0

# ✅ FORMAT
cad_affiche = f"{int(cad)}"
dzd_affiche = f"{dzd:,.2f}".replace(",", " ").replace(".", ",")

# ✅ UI CARTE
st.markdown(f"""
<div class="card">
<div class="flag">🇨🇦 CAD</div>
<div class="value">{cad_affiche}</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="card">
<div class="flag">🇩🇿 DZD</div>
<div class="value">{dzd_affiche}</div>
</div>
""", unsafe_allow_html=True)

# ✅ SIGNATURE
st.markdown("<br><center style='color:#00E676;'>M. Madani</center>", unsafe_allow_html=True)
