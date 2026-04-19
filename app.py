import streamlit as st
import urllib.parse

# ==========================================
# USTAOĞLU HALI YIKAMA - PROFESYONEL PANEL
# ==========================================

# 1. Sayfa Ayarları (Geniş ekran, özel ikon)
st.set_page_config(
    page_title="Ustaoğlu Halı Yıkama",
    page_icon="🧼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Üst Başlık ve Karşılama
st.title("🧼 Ustaoğlu Halı Yıkama Profesyonel Yönetim Paneli")
st.markdown("---")

# 3. Sekmeli Yapı (Operasyon, İstatistik, Oyunlar)
tab1, tab2, tab3 = st.tabs(["📱 Operasyon & İletişim", "📊 Günlük Durum", "🎮 Mola Salonu"])

# --- SEKME 1: OPERASYON VE WHATSAPP ---
with tab1:
    st.header("Müşteri İşlem Merkezi")
    
    # Form yapısı ile daha şık bir görünüm
    with st.container(border=True):
        col1, col2 = st.columns(2)
        
        with col1:
            musteri_adi = st.text_input("👤 Müşteri Adı ve Soyadı", placeholder="Örn: Mustafa Usta")
            telefon = st.text_input("📞 Telefon Numarası", value="90", help="Başında + olmadan, 90 ile başlayarak yazın.")
        
        with col2:
            durum = st.selectbox("🔄 Sipariş Durumu", [
                "Sipariş Alındı - Araç Bekleniyor", 
                "Yıkama Aşamasında", 
                "Kurutma Odasında", 
                "Paketlendi - Teslimata Hazır", 
                "Teslim Edildi - İşlem Tamam"
            ])
            tutar = st.text_input("💰 Toplam Tutar (İsteğe Bağlı)", placeholder="Örn: 450 TL")

        # Özel Mesaj Taslağı Oluşturma
        if tutar:
            mesaj_metni = f"Merhaba {musteri_adi},\n\nUstaoğlu Halı Yıkama'dan yazıyoruz. Halılarınızın güncel durumu: *{durum}*.\nToplam Tutar: *{tutar}*.\n\nBizi tercih ettiğiniz için teşekkür ederiz. İyi günler dileriz! 🧼"
        else:
            mesaj_metni = f"Merhaba {musteri_adi},\n\nUstaoğlu Halı Yıkama'dan yazıyoruz. Halılarınızın güncel durumu: *{durum}*.\n\nBizi tercih ettiğiniz için teşekkür ederiz. İyi günler dileriz! 🧼"
        
        mesaj_kodlu = urllib.parse.quote(mesaj_metni)
        wp_link = f"https://wa.me/{telefon}?text={mesaj_kodlu}"

        st.markdown("###") # Boşluk
        
        # Butonlar
        c1, c2 = st.columns([1, 3])
        with c1:
            if st.button("💾 Sisteme Kaydet", use_container_width=True):
                st.toast(f"{musteri_adi} kaydı başarıyla güncellendi!", icon="✅")
        with c2:
            st.link_button("🟢 WhatsApp'tan Mesajı Gönder", wp_link, use_container_width=True)

# --- SEKME 2: İSTATİSTİK (Görsel Zenginlik İçin) ---
with tab2:
    st.header("Bugünün Özet Tablosu")
    st.info("Sistemin genel durumu aşağıda özetlenmiştir. (Veritabanı bağlandığında canlı güncellenecektir.)")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Alınan Sipariş", value="12", delta="3 Artış")
    m2.metric(label="Yıkanan Halı (m²)", value="145 m²", delta="20 m² Artış")
    m3.metric(label="Teslim Edilen", value="8", delta="-2 Azalış", delta_color="inverse")
    m4.metric(label="Günlük Ciro", value="3.450 TL", delta="450 TL Artış")

# --- SEKME 3: OYUN SALONU ---
with tab3:
    st.header("Mola Zamanı")
    st.write("İşlere kısa bir ara. Oynamak istediğiniz oyunu seçin:")
    
    oyun_secimi = st.selectbox("🎮 Oyun Seçiniz", ["Klasik Yılan Oyunu", "XOX (Tic-Tac-Toe)", "Ping Pong"])
    st.markdown("---")

    if oyun_secimi == "Klasik Yılan Oyunu":
        snake_html = """
        <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
            <canvas id="s" width="400" height="400" style="background:#111; border:3px solid #4CAF50; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.5);"></canvas>
            <p style="color: gray; font-family: sans-serif; margin-top:10px;">Oynamak için yön tuşlarını kullanın. ⬆️ ⬇️ ⬅️ ➡️</p>
        </div>
        <script>
        var c=document.getElementById("s"),x=c.getContext("2d"),g=20,p={x:10,y:10},a={x:15,y:15},v={x:0,y:0},t=[],l=5;
        function draw(){
            p.x+=v.x;p.y+=v.y;
            if(p.x<0)p.x=19;if(p.x>19)p.x=0;if(p.y<0)p.y=19;if(p.y>19)p.y=0;
            x.fillStyle="#111";x.fillRect(0,0,400,400);
            x.fillStyle="#4CAF50";
            for(var i=0;i<t.length;i++){
                x.fillRect(t[i].x*g,t[i].y*g,18,18);
                if(t[i].x==p.x&&t[i].y==p.y)l=5;
            }
            t.push({x:p.x,y:p.y});while(t.length>l)t.shift();
            if(a.x==p.x&&a.y==p.y){l++;a.x=Math.floor(Math.random()*20);a.y=Math.floor(Math.random()*20);}
            x.fillStyle="#FF5252";x.fillRect(a.x*g,a.y*g,18,18);
        }
        document.onkeydown=function(e){
            if(e.keyCode==37&&v.x==0)v={x:-1,y:0};if(e.keyCode==38&&v.y==0)v={x:0,y:-1};
            if(e.keyCode==39&&v.x==0)v={x:1,y:0};if(e.keyCode==40&&v.y==0)v={x:0,y:1};
        };setInterval(draw,100);
        </script>
        """
        st.components.v1.html(snake_html, height=500)

    elif oyun_secimi == "XOX (Tic-Tac-Toe)":
        xox_html = """
        <div style="font-family: sans-serif; display: flex; flex-direction: column; align-items: center;">
            <div id="b" style="display:grid; grid-template-columns:repeat(3,90px); gap:8px; justify-content:center; margin-bottom: 20px;"></div>
            <button onclick="reset()" style="padding: 10px 20px; font-size: 16px; cursor: pointer; background-color: #4CAF50; color: white; border: none; border-radius: 5px;">Oyunu Sıfırla</button>
        </div>
        <script>
        let b=Array(9).fill(""),t="X";
        function r(){
            const el=document.getElementById("b");el.innerHTML="";
            b.forEach((v,i)=>{
                let d=document.createElement("div");
                d.style="width:90px; height:90px; background:#2c3e50; color:#ecf0f1; display:flex; align-items:center; justify-content:center; font-size:3em; cursor:pointer; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); font-weight: bold;";
                d.innerText=v;
                d.onclick=()=>{if(!v){b[i]=t;t=t=="X"?"O":"X";r();}};
                el.appendChild(d);
            });
        }
        function reset(){ b=Array(9).fill(""); t="X"; r(); }
        r();
        </script>
        """
        st.components.v1.html(xox_html, height=450)

    elif oyun_secimi == "Ping Pong":
        pong_html = """
        <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
            <canvas id="p" width="600" height="350" style="background:#000; border:4px solid #fff; border-radius: 5px; box-shadow: 0 4px 8px rgba(0,0,0,0.5);"></canvas>
            <p style="color: gray; font-family: sans-serif; margin-top:10px;">Fare (Mouse) ile raketi yukarı/aşağı hareket ettirin.</p>
        </div>
        <script>
        var c=document.getElementById("p"),x=c.getContext("2d"),b={x:300,y:175,dx:4,dy:4},p={y:135,h:80};
        c.onmousemove=(e)=>{p.y=e.clientY-c.getBoundingClientRect().top-40;};
        function d(){
            x.fillStyle="black";x.fillRect(0,0,600,350);
            x.fillStyle="white";x.fillRect(10,p.y,12,p.h);
            x.beginPath();x.arc(b.x,b.y,10,0,Math.PI*2);x.fill();
            b.x+=b.dx;b.y+=b.dy;
            if(b.y<0||b.y>350)b.dy*=-1;if(b.x>600)b.dx*=-1;
            if(b.x<22&&b.y>p.y&&b.y<p.y+p.h)b.dx*=-1.05;
            if(b.x<0){b={x:300,y:175,dx:4,dy:4};}
            requestAnimationFrame(d);
        }
        d();
        </script>
        """
        st.components.v1.html(pong_html, height=500)
