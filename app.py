import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

# --- VERİTABANI HAZIRLIĞI ---
def init_db():
    conn = sqlite3.connect('hali_yikama.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS siparisler
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  musteri_adi TEXT, 
                  telefon TEXT, 
                  bolge TEXT, 
                  metrekare REAL, 
                  ucret REAL,
                  odeme_durumu TEXT,
                  durum TEXT, 
                  kayit_tarihi TEXT)''')
    conn.commit()
    conn.close()

init_db()

# --- ARAYÜZ VE GÜVENLİK ---
st.set_page_config(page_title="MODEREN Halı Yıkama", layout="wide")

# Sol menü
st.sidebar.title("🧺 MODEREN Menü")
mode = st.sidebar.radio("Geçiş Yap:", ["Müşteri Takip Ekranı", "Yönetici Girişi"])

# --- MÜŞTERİ TAKİP EKRANI (ŞİFRESİZ) ---
if mode == "Müşteri Takip Ekranı":
    st.title("🔍 Halım Nerede?")
    st.write("Hoş geldiniz! Halınızın durumunu öğrenmek için numaranızı giriniz.")
    sorgu = st.text_input("Telefon numaranızı girin (905...):")
    if st.button("Sorgula"):
        conn = sqlite3.connect('hali_yikama.db')
        df = pd.read_sql_query(f"SELECT * FROM siparisler WHERE telefon LIKE '%{sorgu}%'", conn)
        conn.close()
        if not df.empty:
            st.info(f"Sayın {df['musteri_adi'][0]}, Halınızın durumu: **{df['durum'][0]}**")
            st.write(f"Toplam Tutar: {df['ucret'][0]} TL")
        else:
            st.error("Kayıt bulunamadı. Lütfen numaranızı kontrol edin.")

# --- YÖNETİCİ GİRİŞİ (ŞİFRELİ) ---
elif mode == "Yönetici Girişi":
    st.title("🔐 Yönetici Paneli")
    sifre = st.text_input("Giriş Şifresini Yazın:", type="password")
    
    if sifre == "1234": # Şifre burası
        st.success("Giriş Yapıldı! MODEREN Mühendislik Yönetim Üssü Aktif.")
        
        # Yönetici sekmeleri
        tab_ozet, tab_yeni, tab_operasyon = st.tabs(["📊 İşletme Özeti", "📝 Yeni Kayıt", "🚚 Operasyon & WhatsApp"])
        
        with tab_ozet:
            conn = sqlite3.connect('hali_yikama.db')
            df = pd.read_sql_query("SELECT * FROM siparisler", conn)
            conn.close()
            
            if not df.empty:
                c1, c2, c3 = st.columns(3)
                c1.metric("Toplam Sipariş", len(df))
                c2.metric("Bekleyen Ödeme", f"{len(df[df['odeme_durumu'] == 'Bekliyor'])} Adet")
                c3.metric("Toplam Ciro", f"{df['ucret'].sum()} TL")
                st.subheader("Bölge Dağılımı")
                st.bar_chart(df['bolge'].value_counts())
            else:
                st.info("Henüz kayıt yok. 'Yeni Kayıt' menüsünden başlayın.")

        with tab_yeni:
            with st.form("yeni_siparis"):
                col1, col2 = st.columns(2)
                with col1:
                    ad = st.text_input("Müşteri Ad Soyad")
                    tel = st.text_input("Telefon (Örn: 905...)")
                    bolge = st.selectbox("Bölge", ["Selçuklu", "Meram", "Karatay", "Büsan/Organize", "Diğer"])
                with col2:
                    m2 = st.number_input("Metrekare", min_value=1.0)
                    fiyat = st.number_input("Birim Fiyat (TL)", value=45)
                    odeme = st.selectbox("Ödeme", ["Bekliyor", "Ödendi"])
                
                toplam = m2 * fiyat
                if st.form_submit_button("Siparişi Kaydet"):
                    conn = sqlite3.connect('hali_yikama.db')
                    c = conn.cursor()
                    c.execute("INSERT INTO siparisler (musteri_adi, telefon, bolge, metrekare, ucret, odeme_durumu, durum, kayit_tarihi) VALUES (?,?,?,?,?,?,?,?)", (ad, tel, bolge, m2, toplam, odeme, "Sipariş Alındı", datetime.now().strftime("%d-%m-%Y")))
                    conn.commit()
                    conn.close()
                    st.success(f"Kayıt Tamamlandı: {toplam} TL")

        with tab_operasyon:
            conn = sqlite3.connect('hali_yikama.db')
            df_op = pd.read_sql_query("SELECT * FROM siparisler WHERE durum != 'Teslim Edildi'", conn)
            conn.close()
            
            if df_op.empty:
                st.write("Şu an bekleyen operasyon yok.")
            else:
                for i, row in df_op.iterrows():
                    with st.expander(f"{row['musteri_adi']} - {row['durum']}"):
                        yeni = st.selectbox("Durumu Güncelle", ["Sipariş Alındı", "Yıkamada", "Kurutmada", "Dağıtımda", "Teslim Edildi"], key=f"s_{row['id']}")
                        if st.button("Güncelle ve Mesaj Hazırla", key=f"b_{row['id']}"):
                            conn = sqlite3.connect('hali_yikama.db')
                            c = conn.cursor()
                            c.execute("UPDATE siparisler SET durum = ? WHERE id = ?", (yeni, row['id']))
                            conn.commit()
                            conn.close()
                            
                            # WhatsApp Linki
                            msg = f"Merhaba {row['musteri_adi']}, MODEREN Halı Yıkama: Halınız şu an *{yeni}* aşamasındadır."
                            wa_link = f"https://wa.me/{row['telefon']}?text={msg.replace(' ', '%20')}"
                            st.markdown(f"[💬 WhatsApp'tan Gönder]({wa_link})")
                            st.rerun()
    else:
        if sifre != "":
            st.warning("Lütfen geçerli bir yönetici şifresi giriniz.")
