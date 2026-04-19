import streamlit as st
import urllib.parse

# Uygulama Ayarları
st.set_page_config(page_title="Ustaoğlu Halı Yıkama", page_icon="🧼", layout="wide")

# ==========================================
# VERİ DEPOLAMA (Sanal Veritabanı)
# ==========================================
# Not: Gerçek bir veritabanı bağlanana kadar veriler burada geçici tutulur.
if "veritabani" not in st.session_state:
    st.session_state["veritabani"] = {
        "905000000000": {"ad": "Örnek Müşteri", "durum": "Teslimata Hazır", "tutar": "500 TL"}
    }

# ==========================================
# YAN MENÜ (NAVİGASYON)
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3003/3003984.png", width=100)
    st.title("Ustaoğlu Kontrol")
    rol = st.radio("Lütfen Giriş Türünü Seçin:", ["👤 Müşteri Sorgulama", "🔐 Yönetici Paneli"])
    st.markdown("---")
    st.info("Müşteriler sadece sorgulama ekranını görebilir.")

# ==========================================
# 👤 MÜŞTERİ SORGULAMA EKRANI
# ==========================================
if rol == "👤 Müşteri Sorgulama":
    st.title("🧼 Ustaoğlu Halı Yıkama - Müşteri Bilgi Sistemi")
    st.write("Hoş geldiniz! Halınızın durumunu öğrenmek için numaranızı girin.")

    sorgu_tel = st.text_input("Telefon Numaranız (90 ile başlayın)", placeholder="905xxxxxxxxx")
    
    if st.button("Durumu Sorgula"):
        if sorgu_tel in st.session_state["veritabani"]:
            bilgi = st.session_state["veritabani"][sorgu_tel]
            st.success(f"Sayın **{bilgi['ad']}**, halınızın güncel durumu: **{bilgi['durum']}**")
            if bilgi['tutar']:
                st.info(f"Ödenecek Tutar: **{bilgi['tutar']}**")
        else:
            st.warning("⚠️ Bu numaraya ait bir kayıt bulunamadı. Lütfen numaranızı kontrol edin veya bizimle iletişime geçin.")

    st.markdown("---")
    st.subheader("🎮 Halınız Yıkanırken Biraz Oyun Oynayın!")
    
    oyun = st.selectbox("Bir Oyun Seçin", ["Yılan", "XOX", "Ping Pong"])
    
    if oyun == "Yılan":
        src = """<div style="display:flex;justify-content:center;"><canvas id="s" width="400" height="400" style="background:#111;border:3px solid #4CAF50;"></canvas></div><script>var c=document.getElementById("s"),x=c.getContext("2d"),g=20,p={x:10,y:10},a={x:15,y:15},v={x:0,y:0},t=[],l=5;function draw(){p.x+=v.x;p.y+=v.y;if(p.x<0)p.x=19;if(p.x>19)p.x=0;if(p.y<0)p.y=19;if(p.y>19)p.y=0;x.fillStyle="#111";x.fillRect(0,0,400,400);x.fillStyle="#4CAF50";for(var i=0;i<t.length;i++){x.fillRect(t[i].x*g,t[i].y*g,18,18);if(t[i].x==p.x&&t[i].y==p.y)l=5;}t.push({x:p.x,y:p.y});while(t.length>l)t.shift();if(a.x==p.x&&a.y==p.y){l++;a.x=Math.floor(Math.random()*20);a.y=Math.floor(Math.random()*20);}x.fillStyle="#FF5252";x.fillRect(a.x*g,a.y*g,18,18);}document.onkeydown=function(e){if(e.keyCode==37&&v.x==0)v={x:-1,y:0};if(e.keyCode==38&&v.y==0)v={x:0,y:-1};if(e.keyCode==39&&v.x==0)v={x:1,y:0};if(e.keyCode==40&&v.y==0)v={x:0,y:1};};setInterval(draw,100);</script>"""
        st.components.v1.html(src, height=450)
    elif oyun == "XOX":
        src = """<div style="display:flex;flex-direction:column;align-items:center;"><div id="b" style="display:grid;grid-template-columns:repeat(3,90px);gap:8px;margin-bottom:20px;"></div><button onclick="reset()" style="padding:10px 20px;background:#4CAF50;color:#fff;border:none;border-radius:5px;">Sıfırla</button></div><script>let b=Array(9).fill(""),t="X";function r(){const el=document.getElementById("b");el.innerHTML="";b.forEach((v,i)=>{let d=document.createElement("div");d.style="width:90px;height:90px;background:#2c3e50;color:#fff;display:flex;align-items:center;justify-content:center;font-size:3em;cursor:pointer;border-radius:10px;";d.innerText=v;d.onclick=()=>{if(!v){b[i]=t;t=t=="X"?"O":"X";r();}};el.appendChild(d);});}function reset(){b=Array(9).fill("");t="X";r();}r();</script>"""
        st.components.v1.html(src, height=450)
    elif oyun == "Ping Pong":
        src = """<div style="display:flex;justify-content:center;"><canvas id="p" width="600" height="350" style="background:#000;border:4px solid #fff;"></canvas></div><script>var c=document.getElementById("p"),x=c.getContext("2d"),b={x:300,y:175,dx:4,dy:4},p={y:135,h:80};c.onmousemove=(e)=>{p.y=e.clientY-c.getBoundingClientRect().top-40;};function d(){x.fillStyle="black";x.fillRect(0,0,600,350);x.fillStyle="white";x.fillRect(10,p.y,12,p.h);x.beginPath();x.arc(b.x,b.y,10,0,7);x.fill();b.x+=b.dx;b.y+=b.dy;if(b.y<0||b.y>350)b.dy*=-1;if(b.x>600)b.dx*=-1;if(b.x<22&&b.y>p.y&&b.y<p.y+p.h)b.dx*=-1.05;if(b.x<0){b={x:300,y:175,dx:4,dy:4};}requestAnimationFrame(d);}d();</script>"""
        st.components.v1.html(src, height=450)

# ==========================================
# 🔐 YÖNETİCİ PANELİ (ŞİFRELİ)
# ==========================================
elif rol == "🔐 Yönetici Paneli":
    sifre = st.text_input("Yönetici Şifresini Girin", type="password")
    
    if sifre == "00755133Eren": # ŞİFREN BURASI
        st.title("👨‍💼 Yönetici Kontrol Paneli")
        
        with st.form("kayit_formu"):
            st.subheader("Yeni Müşteri Ekle / Güncelle")
            m_ad = st.text_input("Müşteri Adı")
            m_tel = st.text_input("Telefon (90...)", value="90")
            m_durum = st.selectbox("Durum", ["Sipariş Alındı", "Yıkama", "Kurutma", "Teslimata Hazır", "Teslim Edildi"])
            m_tutar = st.text_input("Tutar (Örn: 450 TL)")
            
            if st.form_submit_button("Sisteme İşle"):
                st.session_state["veritabani"][m_tel] = {"ad": m_ad, "durum": m_durum, "tutar": m_tutar}
                st.success(f"{m_ad} başarıyla kaydedildi. Müşteri artık kendi ekranından görebilir.")

        st.markdown("---")
        st.subheader("📱 Hızlı WhatsApp Bildirimi")
        secili_tel = st.selectbox("Kayıtlı Müşteriler", list(st.session_state["veritabani"].keys()))
        
        if secili_tel:
            info = st.session_state["veritabani"][secili_tel]
            mesaj = f"Merhaba {info['ad']}, Ustaoğlu Halı Yıkama'dan yazıyoruz. Halınızın durumu: *{info['durum']}*."
            encoded_msg = urllib.parse.quote(mesaj)
            st.link_button("WhatsApp'tan Gönder", f"https://wa.me/{secili_tel}?text={encoded_msg}")
            
    elif sifre != "":
        st.error("❌ Hatalı Şifre! Yetkiniz yok.")
