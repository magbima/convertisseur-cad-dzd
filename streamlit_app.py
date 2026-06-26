import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Convertisseur CAD ↔ DZD",
    page_icon="💱",
    layout="centered"
)

# =========================
# STYLE
# =========================
st.markdown("""
<style>
.stApp {
    background: #0B0F1A;
    color: white;
}

h1 {
    text-align: center;
    color: #00E676;
    font-size: 34px;
    font-weight: 800;
}

.rate-box {
    text-align: center;
    color: #DDE6F0;
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 25px;
}

.field-title {
    color: #FFFFFF;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 6px;
}

.input-card {
    background: #FFFFFF;
    border-radius: 12px;
    padding: 8px 12px;
    border: 2px solid #2E7D32;
    margin-bottom: 18px;
}

.currency-badge {
    font-size: 22px;
    font-weight: 800;
    color: #000000;
    text-align: center;
    padding-top: 10px;
}

input {
    font-size: 28px !important;
    font-weight: 800 !important;
    color: #000000 !important;
    background: #FFFFFF !important;
    border: none !important;
    box-shadow: none !important;
}

div[data-testid="stTextInput"] {
    margin-bottom: 0px;
}

.arrow-circle {
    background: #8DEB61;
    color: #000000;
    width: 48px;
    height: 48px;
    border-radius: 50%;
    text-align: center;
    line-height: 48px;
    font-size: 24px;
    font-weight: bold;
    margin: auto;
    margin-top: 8px;
    margin-bottom: 20px;
}

.result-card {
    background: #121826;
    padding: 22px;
    border-radius: 16px;
    margin-top: 18px;
    text-align: center;
    box-shadow: 0px 0px 25px rgba(0, 230, 118, 0.10);
}

.result-value {
    font-size: 30px;
    font-weight: 800;
    color: #00E676;
}

.result-label {
    color: #AAB2C0;
    font-size: 14px;
    margin-top: 6px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# FONCTIONS
# =========================
def parse_number(value):
    if value is None:
        return 0.0

    value = str(value).strip()
    value = value.replace(" ", "")
    value = value.replace("\u00a0", "")
    value = value.replace(",", ".")

    try:
        return float(value)
    except:
        return 0.0


def format_dzd(value):
    # Exemple : 234 860,87
    return f"{value:,.2f}".replace(",", " ").replace(".", ",")


def format_cad(value):
    # Exemple : 2500
    return str(int(round(value)))


# =========================
# SESSION STATE
# =========================
if "taux" not in st.session_state:
    st.session_state.taux = "170"

if "dzd" not in st.session_state:
    st.session_state.dzd = "17000,00"

if "cad" not in st.session_state:
    st.session_state.cad = "100"

if "last_changed" not in st.session_state:
    st.session_state.last_changed = "dzd"


def update_from_dzd():
    taux = parse_number(st.session_state.taux)
    dzd = parse_number(st.session_state.dzd)

    if taux > 0:
        cad = dzd / taux
        st.session_state.cad = format_cad(cad)

    st.session_state.last_changed = "dzd"


def update_from_cad():
    taux = parse_number(st.session_state.taux)
    cad = parse_number(st.session_state.cad)

    dzd = cad * taux
    st.session_state.dzd = format_dzd(dzd)

    st.session_state.last_changed = "cad"


def update_from_taux():
    if st.session_state.last_changed == "dzd":
        update_from_dzd()
    else:
        update_from_cad()


# =========================
# INTERFACE
# =========================
st.title("Convertisseur CAD ↔ DZD")

taux_value = parse_number(st.session_state.taux)

if taux_value > 0:
    inverse_rate = 1 / taux_value
else:
    inverse_rate = 0

st.markdown(
    f"""
    <div class="rate-box">
        Taux de change moyen du marché<br>
        1 CAD = {format_dzd(taux_value)} DZD<br>
        1 DZD = {inverse_rate:.5f} CAD
    </div>
    """,
    unsafe_allow_html=True
)

# TAUX
st.markdown("<div class='field-title'>Taux</div>", unsafe_allow_html=True)

st.text_input(
    "Taux",
    key="taux",
    label_visibility="collapsed",
    on_change=update_from_taux
)

# DZD INPUT
st.markdown("<div class='field-title'>Montant</div>", unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])

with col1:
    st.text_input(
        "DZD",
        key="dzd",
        label_visibility="collapsed",
        on_change=update_from_dzd
    )

with col2:
    st.markdown("<div class='currency-badge'>🇩🇿 DZD</div>", unsafe_allow_html=True)

# FLÈCHE
st.markdown("<div class='arrow-circle'>↕</div>", unsafe_allow_html=True)

# CAD INPUT
st.markdown("<div class='field-title'>Vers</div>", unsafe_allow_html=True)

col3, col4 = st.columns([4, 1])

with col3:
    st.text_input(
        "CAD",
        key="cad",
        label_visibility="collapsed",
        on_change=update_from_cad
    )

with col4:
    st.markdown("<div class='currency-badge'>🇨🇦 CAD</div>", unsafe_allow_html=True)

# RÉSULTATS
dzd_value = parse_number(st.session_state.dzd)
cad_value = parse_number(st.session_state.cad)

st.markdown(
    f"""
    <div class="result-card">
        <div class="result-value">{format_dzd(dzd_value)} DZD</div>
        <div class="result-label">Montant en dinars algériens</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="result-card">
        <div class="result-value">{format_cad(cad_value)} CAD</div>
        <div class="result-label">Montant en dollars canadiens</div>
    </div>
    """,
    unsafe_allow_html=True
)

# SIGNATURE
st.markdown(
    "<hr><center style='color:#00E676;'>💻 Développé par M. Madani</center>",
    unsafe_allow_html=True
)
