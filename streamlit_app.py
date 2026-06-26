import streamlit as st

# ✅ CONFIG
st.set_page_config(
    page_title="CAD ↔ DZD Premium",
    layout="centered"
)

# ✅ STYLE
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #0B0F1A, #070A12);
    color: white;
}
h1 {
    text-align: center;
    color: #00C853;
}
.card {
    background: #121826;
    padding: 25px;
    border-radius: 15px;
    margin-top: 20px;
    text-align: center;
}
.value {
    font-size: 32px;
    font-weight: bold;
    color: #00E676;
}
.arrow {
    text-align: center;
    font-size: 30px;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ✅ TITRE
st.title("Convertisseur CAD ↔ DZD")

# ✅ TAUX
taux = st.number_input("Taux", value=170.0)

# ✅ MÉMOIRE (important)
if "last" not in st.session_state:
    st.session_state.last = "cad"

# ✅ INPUTS
col1, col2, col3 = st.columns([3,1,3])

with col1:
    cad = st.number_input(
        "CAD",
        value=st.session_state.get("cad_val", 100.0),
        key="cad_input"
    )
    if cad != st.session_state.get("cad_val", None):
        st.session_state.last = "cad"
        st.session_state.cad_val = cad

with col2:
    st.markdown("<div class='arrow'>↔️</div>", unsafe_allow_html=True)

with col3:
    dzd = st.number_input(
        "DZD",
        value=st.session_state.get("dzd_val", 0.0),
        key="dzd_input"
    )
    if dzd != st.session_state.get("dzd_val", None):
        st.session_state.last = "dzd"
        st.session_state.dzd_val = dzd

# ✅ CALCUL INTELLIGENT
if st.session_state.last == "cad":
    cad = st.session_state.cad_val
    dzd = cad * taux
    st.session_state.dzd_val = dzd
else:
    dzd = st.session_state.dzd_val
    cad = dzd / taux if taux != 0 else 0
    st.session_state.cad_val = cad

# ✅ FORMATAGE
cad_affiche = f"{int(cad):,} CAD"
dzd_affiche = f"{int(dzd):,} DZD"

# ✅ RESULTATS
st.markdown(f"<div class='card'><div class='value'>{dzd_affiche}</div></div>", unsafe_allow_html=True)
st.markdown(f"<div class='card'><div class='value'>{cad_affiche}</div></div>", unsafe_allow_html=True)

# ✅ SIGNATURE
st.markdown("<hr><center style='color:#00C853;'>💻 Développé par M. Madani</center>", unsafe_allow_html=True)
