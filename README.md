# ⚔️ Scrabble RPG: Battle Arena Dashboard

**Scrabble RPG** adalah inovasi permainan Scrabble konvensional yang digabungkan dengan mekanik *Role-Playing Game* (RPG). Aplikasi ini adalah *dashboard* interaktif berbasis **Streamlit** yang dirancang untuk panitia perlombaan agar mudah melacak *Hit Points* (HP), menghitung *damage*, dan mencatat status efek (Buff/Debuff) dari setiap tim secara *real-time*.

## ✨ Fitur Utama
* **Pengaturan Pertandingan Dinamis:** Panitia dapat mengatur nama tim dan jumlah maksimal HP sebelum pertandingan dimulai.
* **Visual HP Bar:** Menampilkan persentase sisa nyawa (*Hit Points*) masing-masing tim secara langsung.
* **Kalkulator Damage & Heal Otomatis:** Menghitung total skor kata yang disusun dan mengubahnya menjadi *Damage* (Serangan) atau *Heal* (Pemulihan).
* **Tracking Efek Spesial (Buff & Debuff):** 
  * ❄️ Stun (Huruf Z/Q): Lawan kehilangan giliran.
  * 🕶️ Blind (Huruf X): Batasan penggunaan maksimal 4 huruf untuk lawan.
  * 🧪 Poison (Huruf J): Efek pengurangan darah (-5 HP) per giliran.
  * 🔥 ATK UP (Kata 6+ Huruf): Bonus +10 Damage.
  * 🌟 Ultimate Bingo (7 Huruf): Pilihan antara *Meteoric Strike* (+50 DMG) atau *Full Recovery* (HP Penuh).
* **Live Match Log:** Riwayat interaktif yang mencatat setiap aksi, serangan, dan efek yang sedang berlangsung.

## 💻 Cara Menjalankan di Komputer Lokal

Pastikan sudah menginstal **Python**.

1. **Clone Repository ini:**
   ```bash
   git clone [https://github.com/Imaaachan/Scrabble-RPG-Dashboard.git](https://github.com/Imaaachan/Scrabble-RPG-Dashboard.git)
   cd Scrabble-RPG-Dashboard
