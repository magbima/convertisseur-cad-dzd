import streamlit as st

st.set_page_config(
    page_title="CAD ↔ DZD Premium",
    page_icon="💎",
    layout="centered"
)

# ✅ STYLE ULTRA CLEAN
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #0B0F1A, #070A12);
    color: white;
}

/* TITRE */
h1 {
    text-align: center;
    color: #00C853;
}

/* ZONE INPUT */
.container {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

/* CARD */
.card {
    background: #121826;
    padding: 25px;
    border-radius: 15px;
    margin-top: 20px;
    text-align: center;
}

/* RESULT */
.value {
    font-size: 32px;
    font-weight: bold;
    color: #00E676;
}

/* LABEL */
.label {
    color: #888;
}

/* FLECHE */
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

# ✅ CHAMPS FACE À FACE
col1, col2, col3 = st.columns([3, 1, 3])

with col1:
    cad_input = st.number_input("CAD", min_value=0.0, value=100.0, key="cad")

with col2:
    st.markdown("<div class='arrow'>↔️</div>", unsafe_allow_html=True)

with col3:
    dzd_input = st.number_input("DZD", min_value=0.0, value=0.0, key="dzd")

# ✅ LOGIQUE INTELLIGENTE
if cad_input != 0:
    dzd = cad_input * taux
    cad = cad_input
elif dzd_input != 0:
    cad = dzd_input / taux if taux != 0 else 0
    dzd = dzd_input
else:
    cad = 0
    dzd = 0

# ✅ AFFICHAGE
st.markdown(f"""
<div class="card">
    <div class="value">{int(dzd):,} DZD</div>
    <div class="label">Montant en dinars</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="card">
    <div class="value">{int(cad):,} CAD</div>
    <div class="label">Montant en dollars canadiens</div>
</div>
""", unsafe_allow_html=True)

# ✅ SIGNATURE
st.markdown(
    "<hr><center style='color:#00C853;'>💻 Développé par M. Madani</center>",
    unsafe_allow_html=True
)
``
