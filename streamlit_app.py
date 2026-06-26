import streamlit as st

# ✅ CONFIGURATION
st.set_page_config(
    page_title="CAD ↔ DZD Premium",
    page_icon="💎",
    layout="centered"
)

# ✅ STYLE PREMIUM (banque / fintech)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #0B0F1A, #070A12);
    color: white;
}

/* TITRE */
h1 {
    text-align: center;
    font-size: 34px;
    color: #00C853;
    margin-bottom: 20px;
}

/* CARTES */
.card {
    background: #121826;
    padding: 25px;
    border-radius: 15px;
    margin-top: 20px;
    text-align: center;
    box-shadow: 0px 0px 25px rgba(0, 200, 83, 0.08);
}

/* VALEUR PRINCIPALE */
.value {
    font-size: 34px;
    font-weight: bold;
    color: #00E676;
}

/* LABEL */
.label {
    font-size: 14px;
    color: #888;
    margin-top: 5px;
}

/* INPUT */
input {
    text-align: center !important;
    font-size: 18px !important;
}
</style>
""", unsafe_allow_html=True)

# ✅ TITRE
st.title("💱 Convertisseur CAD ↔ DZD")

# ✅ ENTRÉES (design propre en 2 colonnes)
col1, col2 = st.columns(2)

with col1:
    montant_cad = st.number_input(
        "💰 Montant CAD",
        min_value=0.0,
        value=100.0,
        step=10.0
    )

with col2:
    taux = st.number_input(
        "📊 Taux",
        value=170.0,
        step=1.0
    )

# ✅ CALCUL AUTOMATIQUE
dzd = montant_cad * taux
cad_inverse = dzd / taux if taux != 0 else 0

# ✅ AFFICHAGE PREMIUM (CARTE 1)
st.markdown(f"""
<div class="card">
    <div class="value">{dzd:,.2f} DZD</div>
    <div class="label">Équivalent en dinars algériens</div>
</div>
""", unsafe_allow_html=True)

# ✅ AFFICHAGE PREMIUM (CARTE 2)
st.markdown(f"""
<div class="card">
    <div class="value">{(cad_inverse)} CAD</div>
    <div class="label">Conversion inverse immédiate</div>
</div>
""", unsafe_allow_html=True)

# ✅ RESET
if st.button("🔄 Réinitialiser taux"):
    st.rerun()

# ✅ SIGNATURE
st.markdown(
    "<hr><center style='color:#00C853;'>💻 Développé par M. Madani</center>",
    unsafe_allow_html=True
)
