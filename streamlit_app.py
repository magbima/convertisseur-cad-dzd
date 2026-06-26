import streamlit as st

# =========================
# CONFIGURATION
# =========================
st.set_page_config(
    page_title="CAD ↔ DZD Premium",
    page_icon="💱",
    layout="centered"
)

# =========================
# STYLE PREMIUM
# =========================
st.markdown("""
<style>
.stApp {
    background: #0B0F1A;
    color: white;
}

/* TITRE */
h1 {
    text-align: center;
    color: #00E676;
    font-size: 36px;
    font-weight: 800;
}

/* LABELS VISIBLES */
.field-label {
    color: #FFFFFF;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 6px;
}

/* TEXTE INFO */
.info-rate {
    text-align: center;
    color: #AAB2C0;
    font-size: 14px;
    margin-bottom: 20px;
}

/* INPUTS */
input {
    text-align: center !important;
    font-size: 22px !important;
    font-weight: bold !important;
}

/* CARTES */
.card {
    background: #121826;
    padding: 24px;
    border-radius: 18px;
    margin-top: 22px;
    text-align: center;
    box-shadow: 0px 0px 25px rgba(0, 230, 118, 0.10);
}

/* VALEURS */
.value {
    font-size: 34px;
    font-weight: 800;
    color: #00E676;
}

/* SOUS-TITRES */
.label {
    color: #AAB2C0;
    font-size: 14px;
    margin-top: 6px;
}

/* FLÈCHE */
.arrow {
    text-align: center;
    font-size: 32px;
    margin-top: 38px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# VARIABLES SESSION
# =========================
if "taux" not in st.session_state:
    st.session_state.taux = 170.0

if "cad" not in st.session_state:
    st.session_state.cad = 100.0

if "dzd" not in st.session_state:
    st.session_state.dzd = 17000.0

if "last_changed" not in st.session_state:
    st.session_state.last_changed = "cad"


# =========================
# FONCTIONS
# =========================
def update_from_cad():
    st.session_state.last_changed = "cad"
    st.session_state.dzd = st.session_state.cad * st.session_state.taux


def update_from_dzd():
    st.session_state.last_changed = "dzd"
    if st.session_state.taux != 0:
        st.session_state.cad = st.session_state.dzd / st.session_state.taux


def update_rate():
    if st.session_state.last_changed == "cad":
        update_from_cad()
    else:
        update_from_dzd()


def format_cad(value):
    # CAD sans centimes, avec séparateur si gros montant
    return f"{int(round(value)):,} CAD"


def format_dzd(value):
    # DZD avec centimes seulement si nécessaire
    if abs(value - round(value)) < 0.005:
        return f"{int(round(value)):,} DZD"
    return f"{value:,.2f} DZD"


# =========================
# INTERFACE
# =========================
st.title("Convertisseur CAD ↔ DZD")

st.markdown("<div class='field-label'>Taux de change</div>", unsafe_allow_html=True)
st.number_input(
    label="Taux de change",
    value=st.session_state.taux,
    step=1.0,
    format="%.0f",
    key="taux",
    label_visibility="collapsed",
    on_change=update_rate
)

st.markdown(
    f"<div class='info-rate'>1 CAD = {st.session_state.taux:.0f} DZD</div>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([3, 1, 3])

with col1:
    st.markdown("<div class='field-label'>CAD</div>", unsafe_allow_html=True)
    st.number_input(
        label="CAD",
        min_value=0.0,
        step=1.0,
        format="%.0f",
        key="cad",
        label_visibility="collapsed",
        on_change=update_from_cad
    )

with col2:
    st.markdown("<div class='arrow'>↔️</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='field-label'>DZD</div>", unsafe_allow_html=True)
    st.number_input(
        label="DZD",
        min_value=0.0,
        step=1.0,
        format="%.0f",
        key="dzd",
        label_visibility="collapsed",
        on_change=update_from_dzd
    )

# =========================
# AFFICHAGE RÉSULTATS
# =========================
st.markdown(
    f"""
    <div class="card">
        <div class="value">{format_dzd(st.session_state.dzd)}</div>
        <div class="label">Montant en dinars algériens</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="card">
        <div class="value">{format_cad(st.session_state.cad)}</div>
        <div class="label">Montant en dollars canadiens</div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# SIGNATURE
# =========================
st.markdown(
    "<hr><center style='color:#00E676;'>💻 Développé par M. Madani</center>",
    unsafe_allow_html=True
)
