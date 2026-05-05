import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Scrabble RPG", layout="wide")

# 1. Inisialisasi Session State
if 'match_started' not in st.session_state:
    st.session_state.match_started = False
if 'nama_tim_1' not in st.session_state:
    st.session_state.nama_tim_1 = "Tim 1"
if 'nama_tim_2' not in st.session_state:
    st.session_state.nama_tim_2 = "Tim 2"
if 'max_hp' not in st.session_state:
    st.session_state.max_hp = 150
if 'hp_1' not in st.session_state:
    st.session_state.hp_1 = 150
if 'hp_2' not in st.session_state:
    st.session_state.hp_2 = 150
if 'log' not in st.session_state:
    st.session_state.log = []

# 2. SIDEBAR: PENGATURAN MATCH
with st.sidebar:
    st.header("⚙️ Pengaturan Match")
    st.write("Atur form di bawah sebelum mulai.")
    
    input_tim_1 = st.text_input("Nama Tim Kiri:", value=st.session_state.nama_tim_1)
    input_tim_2 = st.text_input("Nama Tim Kanan:", value=st.session_state.nama_tim_2)
    input_hp = st.number_input("HP Awal:", min_value=10, value=st.session_state.max_hp, step=10)
    
    if st.button("Mulai / Reset Match", type="primary"):
        st.session_state.nama_tim_1 = input_tim_1
        st.session_state.nama_tim_2 = input_tim_2
        st.session_state.max_hp = input_hp
        st.session_state.hp_1 = input_hp
        st.session_state.hp_2 = input_hp
        st.session_state.log = [f"BATTLE START: {input_tim_1} VS {input_tim_2} ({input_hp} HP)"]
        st.session_state.match_started = True
        st.rerun()

# 3. MAIN DASHBOARD
st.title("⚔️ Scrabble RPG: Battle Arena")

if not st.session_state.match_started:
    st.info("👈 Silakan atur nama tim dan HP di menu samping, lalu klik 'Mulai / Reset Match'.")
else:
    # --- VISUAL HP BAR ---
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        st.subheader(f"🛡️ {st.session_state.nama_tim_1}")
        st.metric(label="HP Tersisa", value=st.session_state.hp_1)
        progress_1 = max(0.0, min(st.session_state.hp_1 / st.session_state.max_hp, 1.0))
        st.progress(progress_1)

    with col2:
        st.markdown("<h1 style='text-align: center; color: red;'>VS</h1>", unsafe_allow_html=True)

    with col3:
        st.subheader(f"🔥 {st.session_state.nama_tim_2}")
        st.metric(label="HP Tersisa", value=st.session_state.hp_2)
        progress_2 = max(0.0, min(st.session_state.hp_2 / st.session_state.max_hp, 1.0))
        st.progress(progress_2)

    st.markdown("---")

    # --- CONTROL PANEL PANITIA ---
    st.header("🎮 Input Aksi Panitia")
    with st.form("input_aksi"):
        c1, c2, c3 = st.columns([1, 1, 1])
        with c1:
            tim_aktif = st.selectbox("Giliran:", [st.session_state.nama_tim_1, st.session_state.nama_tim_2])
        with c2:
            skor_didapat = st.number_input("Skor Kata Dasar:", min_value=0, step=1, help="Total skor murni dari huruf yang disusun")
        with c3:
            aksi = st.radio("Pilih Aksi:", ["ATTACK ⚔️", "HEAL 💚"])

        st.markdown("### 🧪 Efek Spesial (Opsional)")
        st.caption("Centang efek di bawah ini jika tim memenuhi syarat dari kata yang disusun.")
        
        col_debuff, col_buff = st.columns(2)
        with col_debuff:
            st.markdown("**Debuff (Kelemahan Musuh)**")
            efek_stun = st.checkbox("❄️ Stun (Huruf Z/Q)", help="Lawan kehilangan 1 giliran (Skip Turn)")
            efek_blind = st.checkbox("🕶️ Blind (Huruf X)", help="Lawan hanya boleh pakai maksimal 4 huruf di giliran depan")
            efek_poison = st.checkbox("🧪 Poison (Huruf J)", help="Lawan akan terkena -5 HP di awal gilirannya nanti")
            
        with col_buff:
            st.markdown("**Buff & Ultimate (Keuntungan Tim)**")
            efek_atk_up = st.checkbox("🔥 ATK UP (Kata 6+ Huruf)", help="Otomatis menambah +10 Damage ke serangan ini")
            efek_bingo = st.selectbox("🌟 Ultimate Bingo (Habis 7 Huruf)", 
                                      ["Tidak Ada", "Meteoric Strike (+50 DMG)", "Full Recovery (HP Penuh)"],
                                      help="Pilih efek pamungkas jika menghabiskan semua huruf di rak")

        submit = st.form_submit_button("Jalankan Aksi! 🚀")

    # --- TOMBOL QUICK POISON ---
    # Tombol cepat di luar form untuk mengurangi darah musuh yang sedang keracunan
    st.caption("Tombol Cepat (Bila musuh sedang dalam status Poison di awal gilirannya):")
    col_p1, col_p2 = st.columns(2)
    if col_p1.button(f"🧪 Beri Damage Poison ke {st.session_state.nama_tim_1} (-5 HP)"):
        st.session_state.hp_1 -= 5
        st.session_state.log.insert(0, f"🧪 {st.session_state.nama_tim_1} terkena efek Poison! HP berkurang 5.")
        st.rerun()
    if col_p2.button(f"🧪 Beri Damage Poison ke {st.session_state.nama_tim_2} (-5 HP)"):
        st.session_state.hp_2 -= 5
        st.session_state.log.insert(0, f"🧪 {st.session_state.nama_tim_2} terkena efek Poison! HP berkurang 5.")
        st.rerun()

    st.markdown("---")

    # --- LOGIKA SISTEM ---
    if submit:
        if tim_aktif == st.session_state.nama_tim_1:
            hp_kawan, hp_lawan = 'hp_1', 'hp_2'
        else:
            hp_kawan, hp_lawan = 'hp_2', 'hp_1'

        pesan_log = f"▶️ {tim_aktif} "
        
        # Hitung Tambahan Damage
        bonus_atk = 10 if efek_atk_up else 0
        bonus_ultimate_dmg = 50 if efek_bingo == "Meteoric Strike (+50 DMG)" else 0
        total_damage = skor_didapat + bonus_atk + bonus_ultimate_dmg

        # Eksekusi Aksi
        if "ATTACK" in aksi:
            st.session_state[hp_lawan] -= total_damage
            pesan_log += f"menyerang sebesar {total_damage} DMG! "
            if efek_atk_up: pesan_log += "(Termasuk +10 ATK UP) "
            if bonus_ultimate_dmg > 0: pesan_log += "(Termasuk +50 ULTIMATE!) "
        else:
            # Jika aksi HEAL
            if efek_bingo == "Full Recovery (HP Penuh)":
                st.session_state[hp_kawan] = st.session_state.max_hp
                pesan_log += "menggunakan ULTIMATE HEAL! HP kembali penuh (100%). "
            else:
                st.session_state[hp_kawan] = min(st.session_state.max_hp, st.session_state[hp_kawan] + skor_didapat)
                pesan_log += f"memulihkan {skor_didapat} HP! "

        # Catat Efek Debuff di Log
        if efek_stun: pesan_log += "| ❄️ Lawan kena STUN! "
        if efek_blind: pesan_log += "| 🕶️ Lawan kena BLIND! "
        if efek_poison: pesan_log += "| 🧪 Lawan kena POISON! "

        st.session_state.log.insert(0, pesan_log)
        
        # Cek Pemenang
        if st.session_state.hp_1 <= 0:
            st.session_state.log.insert(0, f"🏆 MATCH SELESAI! {st.session_state.nama_tim_2} MENANG!")
        elif st.session_state.hp_2 <= 0:
            st.session_state.log.insert(0, f"🏆 MATCH SELESAI! {st.session_state.nama_tim_1} MENANG!")
            
        st.rerun()

    # --- LOG PERTANDINGAN ---
    st.subheader("📜 Riwayat Pertarungan")
    for teks_log in st.session_state.log[:8]:
        if "🏆" in teks_log:
            st.success(teks_log)
        elif "🧪" in teks_log and "terkena efek Poison" in teks_log:
            st.warning(teks_log)
        else:
            st.info(teks_log)