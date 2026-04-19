import streamlit as st
import urllib.parse

# MODEREN Halı Yıkama & Oyun Üssü
st.set_page_config(page_title="MODEREN", layout="wide")

st.title("🧺 MODEREN Operasyon & Oyun Üssü")

t1, t2 = st.tabs(["🚀 WhatsApp", "🎮 Oyunlar"])

with t1:
    m = st.text_input("Müşteri", "Mustafa Usta")
    t = st.text_input("Telefon", "90")
    d = st.selectbox("Durum", ["Sipariş Alındı", "Yıkama", "Teslimata Hazır"])
    msg = urllib.parse.quote(f"Merhaba {m}, halınız: {d}. MODEREN Mühendislik.")
    if st.button("Güncelle"):
        st.link_button("WP Gönder", f"https://wa.me/{t}?text={msg}")

with t2:
    oyun = st.radio("Oyun Seç", ["Yılan", "XOX", "Pong"], horizontal=True)
    
    if oyun == "Yılan":
        src = """<canvas id="s" width="400" height="400" style="background:#000; display:block; margin:auto; border:2px solid #0f0;"></canvas><script>var c=document.getElementById("s"),x=c.getContext("2d"),g=20,p={x:10,y:10},a={x:15,y:15},v={x:0,y:0},t=[],l=5;function draw(){p.x+=v.x;p.y+=v.y;if(p.x<0)p.x=19;if(p.x>19)p.x=0;if(p.y<0)p.y=19;if(p.y>19)p.y=0;x.fillStyle="black";x.fillRect(0,0,400,400);x.fillStyle="lime";for(var i=0;i<t.length;i++){x.fillRect(t[i].x*g,t[i].y*g,18,18);if(t[i].x==p.x&&t[i].y==p.y)l=5;}t.push({x:p.x,y:p.y});while(t.length>l)t.shift();if(a.x==p.x&&a.y==p.y){l++;a.x=Math.floor(Math.random()*20);a.y=Math.floor(Math.random()*20);}x.fillStyle="red";x.fillRect(a.x*g,a.y*g,18,18);}document.onkeydown=function(e){if(e.keyCode==37&&v.x==0)v={x:-1,y:0};if(e.keyCode==38&&v.y==0)v={x:0,y:-1};if(e.keyCode==39&&v.x==0)v={x:1,y:0};if(e.keyCode==40&&v.y==0)v={x:0,y:1};};setInterval(draw,100);</script>"""
        st.components.v1.html(src, height=450)
    
    elif oyun == "XOX":
        src = """<div id="b" style="display:grid;grid-template-columns:repeat(3,80px);gap:5px;justify-content:center;"></div><script>let b=Array(9).fill(""),t="X";function r(){const el=document.getElementById("b");el.innerHTML="";b.forEach((v,i)=>{let d=document.createElement("div");d.style="width:80px;height:80px;background:#333;color:#fff;display:flex;align-items:center;justify-content:center;font-size:2em;cursor:pointer";d.innerText=v;d.onclick=()=>{if(!v){b[i]=t;t=t=="X"?"O":"X";r();}};el.appendChild(d);});}r();</script>"""
        st.components.v1.html(src, height=300)
        
    elif oyun == "Pong":
        src = """<canvas id="p" width="500" height="300" style="background:#000; display:block; margin:auto;"></canvas><script>var c=document.getElementById("p"),x=c.getContext("2d"),b={x:250,y:150,dx:3,dy:3},p={y:100,h:80};c.onmousemove=(e)=>{p.y=e.clientY-c.getBoundingClientRect().top-40;};function d(){x.fillStyle="black";x.fillRect(0,0,500,300);x.fillStyle="white";x.fillRect(10,p.y,10,p.h);x.beginPath();x.arc(b.x,b.y,8,0,7);x.fill();b.x+=b.dx;b.y+=b.dy;if(b.y<0||b.y>300)b.dy*=-1;if(b.x>500)b.dx*=-1;if(b.x<20&&b.y>p.y&&b.y<p.y+p.h)b.dx*=-1.1;if(b.x<0){b={x:250,y:150,dx:3,dy:3};}requestAnimationFrame(d);}d();</script>"""
        st.components.v1.html(src, height=350)
