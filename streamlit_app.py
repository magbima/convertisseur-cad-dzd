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

/* INPUT */
input {
    text-align: center !important;
    font-size: 18px !important;
}

/* CARD RESULT */
.card {
    background: #121826;
    padding: 25px;
    border-radius: 15px;
    margin-top: 20px;
    text-align: center;
    box-shadow: 0px 0px 25px rgba(0,200,83,0.08);
}

/* VALUE */
.value {
    font-size: 34px;
    font-weight: bold;
    color: #00E676;
}

/* LABEL */
.label {
    color: #888;
}

/* ARROW */
.arrow {
    text-align: center;
    font-size: 30px;
    margin-top: 35px;
}
</style>
""", unsafe_allow_html=True)

# ✅ TITRE
st.title("Convertisseur CAD ↔ DZD")

# ✅ TAUX
taux = st.number_input("Taux", value=170.0)

# ✅ ZONE FACE-À-FACE
col1, col2, col3 = st.columns([3,1,3])

with col1:
    cad_input = st.number_input("CAD", min_value=0.0, value=100.0, key="cad")

with col2:
    st.markdown("<div class='arrow'>↔️</div>", unsafe_allow_html=True)

with col3:
    dzd_input = st.number_input("DZD", min_value=0.0, value=0.0, key="dzd")

# ✅ LOGIQUE INTELLIGENTE
if cad_input > 0:
    cad = cad_input
    dzd = cad * taux
elif dzd_input > 0:
    dzd = dzd_input
    cad = dzd / taux if taux != 0 else 0
else:
    cad = 0
    dzd = 0

# ✅ FORMATAGE PRO
dzd_affiche = f"{int(dzd):,} DZD"
cad_affiche = f"{int(cad):,} CAD"

# ✅ AFFICHAGE
st.markdown(
    f"<div class='card'><div class='value'>{dzd_affiche}</div><div class='label'>Montant en dinars algériens</div></div>",
    unsafe_allow_html=True
)

st.markdown(
    f"<div class='card'><div class='value'>{cad_affiche}</div><div class='label'>Montant en dollars canadiens</div></div>",
    unsafe_allow_html=True
)

# ✅ SIGNATURE
st.markdown(
    "<hr><center style='color:#00C853;'>💻 Développé par M. Madani</center>",
    unsafe_allow_html=True
)
