import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

# --- DB AYARI ---
def init_db():
    conn = sqlite3.connect('hali_yikama.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS siparisler
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, musteri_adi TEXT, telefon TEXT, 
                  bolge TEXT, metrekare REAL, ucret REAL, odeme_durumu TEXT, durum TEXT, kayit_tarihi TEXT)''')
    conn.commit()
    conn.close()

init_db()

# --- ARAYÜZ VE GÜVENLİK ---
st.set_page_config(page_title="MODEREN Halı Yıkama", layout="wide")

# Sol menü kontrolü
st.sidebar.title("🧺 MODEREN Menü")
mode = st.sidebar.radio("Geçiş Yap:", ["Müşteri Takip Ekranı", "Yönetici Girişi"])

# --- MÜŞTERİ TAKİP EKRANI (HERKESE AÇIK) ---
if mode == "Müşteri Takip Ekranı":
    st.title("🔍 MODEREN Halı Takip Sistemi")
    st.write("Hoş geldiniz! Halınızın durumunu öğrenmek için numaranızı giriniz.")
    sorgu = st.text_input("Telefon Numaranız (905...):")
    if st.button("Sorgula"):
        conn = sqlite3.connect('hali_yikama.db')
        df = pd.read_sql_query(f"SELECT * FROM siparisler WHERE telefon LIKE '%{sorgu}%'", conn)
        conn.close()
        if not df.empty:
            st.success(f"Sayın {df['musteri_adi'][0]}, Halınızın durumu: **{df['durum'][0]}**")
            st.info(f"Toplam Tutar: {df['ucret'][0]} TL")
        else:
            st.error("Kayıt bulunamadı. Lütfen numaranızı kontrol edin.")

# --- YÖNETİCİ GİRİŞİ (ŞİFRELİ) ---
elif mode == "Yönetici Girişi":
    st.title("🔐 Yönetici Paneli")
    sifre = st.text_input("Giriş Şifresini Yazın:", type="password")
    
    if sifre == "1234": # BURAYI KENDİ ŞİFRENLE DEĞİŞTİREBİLİRSİN
        st.success("Giriş Yapıldı! MODEREN Mühendislik Yönetim Üssü Aktif.")
        
        tab1, tab2, tab3 = st.tabs(["📊 Özet", "📝 Yeni Kayıt", "🚚 Operasyon"])
        
        conn = sqlite3.connect('hali_yikama.db')
        df_all = pd.read_sql_query("SELECT * FROM siparisler", conn)
        conn.close()

        with tab1:
            if not df_all.empty:
                st.metric("Toplam Ciro", f"{df_all['ucret'].sum()} TL")
                st.bar_chart(df_all['bolge'].value_counts())

        with tab2:
            with st.form("yeni"):
                ad = st.text_input("Ad Soyad")
                tel = st.text_input("Telefon (905...)")
                if st.form_submit_button("Kaydet"):
                    # Veritabanı kayıt işlemi...
                    st.write("Kaydedildi!")

        with tab3:
            st.write("Aktif Siparişleri Buradan Yönetin...")
    else:
        st.warning("Lütfen geçerli bir yönetici şifresi giriniz.")