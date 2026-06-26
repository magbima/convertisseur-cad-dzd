import streamlit as st

# ✅ Configuration de la page py -m streamlit run app_web.py
st.set_page_config(
    page_title="Convertisseur CAD → DZD",
    layout="centered"
)

# ✅ Thème sombre
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}
h1 {
    text-align: center;
    color: #00C853;
}
.stNumberInput label {
    color: #BBBBBB;
}
.stButton>button {
    background-color: #0078D7;
    color: white;
    border-radius: 8px;
    padding: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ✅ Taux par défaut
TAUX_PAR_DEFAUT = 170.0

# ✅ Titre
st.title("💱 Convertisseur CAD → DZD")

# ✅ Entrées utilisateur
montant = st.number_input("💰 Montant CAD", min_value=0.0, step=10.0)
taux = st.number_input("📊 Taux (modifiable)", value=TAUX_PAR_DEFAUT)

# ✅ Boutons
col1, col2 = st.columns(2)

with col1:
    if st.button("Convertir"):
        resultat = montant * taux
        st.success(f"💵 {resultat:,.2f} DZD")

with col2:
    if st.button("Réinitialiser taux"):
        st.rerun()

# ✅ Signature visible
st.markdown(
    "<hr><center style='color:#00C853;'>💻 Développé par M. Madani</center>",
    unsafe_allow_html=True
)
