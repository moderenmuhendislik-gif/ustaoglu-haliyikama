import streamlit as st
import urllib.parse

# Sayfa Ayarları
st.set_page_config(page_title="MODEREN Halı Yıkama", layout="wide")

st.title("🧺 MODEREN Operasyon & Oyun Üssü")

# Sekmeler
tab1, tab2 = st.tabs(["🚀 WhatsApp Operasyon", "🎮 Oyun Salonu"])

with tab1:
    st.subheader("Müşteri Durumu ve Bildirim")
    col1, col2 = st.columns(2)
    with col1:
        musteri = st.text_input("Müşteri Adı", value="Mustafa Usta")
        tel = st.text_input("Telefon (90...)", value="90")
    with col2:
        durum = st.selectbox("İşlem Durumu", ["Sipariş Alındı", "Yıkama Başladı", "Kurutma", "Teslimata Hazır", "Teslim Edildi"])
    
    mesaj = f"Merhaba {musteri}, halınızın durumu: *{durum}*. MODEREN Mühendislik & Halı Yıkama."
    link = f"https://wa.me/{tel}?text={urllib.parse.quote(mesaj)}"
    
    if st.button("Sistemi Güncelle"):
        st.success(f"{musteri} için durum güncellendi!")
        st.link_button("WhatsApp'tan Bildir 💬", link)

with tab2:
    st.subheader("Mola Zamanı: İstediğin Oyunu Seç")
    oyun_secimi = st.selectbox("Bir Oyun Seç", ["Yılan Oyunu", "XOX (Tic-Tac-Toe)", "Ping Pong"])

    if oyun_secimi == "Yılan Oyunu":
        snake_html = """
        <canvas id="s" width="400" height="400" style="border:3px solid #4CAF50; background:#000; display:block; margin:auto;"></canvas>
        <script>
        var c=document.getElementById("s"),x=c.getContext("2d"),g=20,p={x:10,y:10},a={x:15,y:15},v={x:0,y:0},t=[],l=5;
        function draw(){
            p.x+=v.x; p.y+=v.y;
            if(p.x<0)p.x=19; if(p.x>19)p.x=0; if(p.y<0)p.y=19; if(p.y>19)p.y=0;
            x.fillStyle="black"; x.fillRect(0,0,c.width,c.height);
            x.fillStyle="lime";
            for(var i=0;i<t.length;i++){
                x.fillRect(t[i].x*g,t[i].y*g,g-2,g-2);
                if(t[i].x==p.x&&t[i].y==p.y)l=5;
            }
            t.push({x:p.x,y:p.y}); while(t.length>l)t.shift();
            if(a.x==p.x&&a.y==p.y){l++; a.x=Math.floor(Math.random()*20); a.y=Math.floor(Math.random()*20);}
            x.fillStyle="red"; x.fillRect(a.x*g,a.y*g,g-2,g-2);
        }
        document.onkeydown=function(e){
            if(e.keyCode==37&&v.x==0){v={x:-1,y:0}} if(e.
