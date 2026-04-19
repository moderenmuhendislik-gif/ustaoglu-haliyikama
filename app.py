import streamlit as st
import urllib.parse

# Sayfa Yapılandırması
st.set_page_config(page_title="MODEREN Halı Yıkama", layout="wide")

st.title("🧺 MODEREN Mühendislik - Halı Yıkama Operasyon Üssü")

# Sekme Yapısı
tab1, tab2 = st.tabs(["🚀 Operasyon & WhatsApp", "🎮 Mola (Oyun)"])

with tab1:
    st.subheader("Müşteri Durum Paneli")
    
    col1, col2 = st.columns(2)
    with col1:
        # Görseldeki gibi 'mustafa usta' örneği üzerinden
        musteri_adi = st.text_input("Müşteri Adı", value="mustafa usta")
        # Telefonun başına 90 eklemeyi unutma
        telefon = st.text_input("Telefon (90 ile başla)", value="90")
    
    with col2:
        durum = st.selectbox("Durum Güncelle", 
                            ["Sipariş Alındı", "Yıkama Aşamasında", "Kurumada", "Teslimata Hazır", "Teslim Edildi"])

    # WhatsApp Mesajını Hazırlama
    mesaj = f"Merhaba {musteri_adi}, MODEREN Halı Yıkama'dan yazıyoruz. Siparişinizin güncel durumu: *{durum}*."
    encoded_mesaj = urllib.parse.quote(mesaj)
    # Web uyumlu WhatsApp linki
    wp_link = f"https://wa.me/{telefon}?text={encoded_mesaj}"

    if st.button("Veriyi Güncelle ve Mesajı Hazırla"):
        # Burada işlem başarı mesajı gösteriyoruz
        st.success(f"{musteri_adi} için kayıt '{durum}' olarak güncellendi.")
        # Link butonu tarayıcıda yeni sekme açtığı için hata vermez
        st.link_button("WhatsApp'ı Aç ve Gönder 💬", wp_link)

with tab2:
    st.subheader("Kısa Bir Mola")
    st.write("Yön tuşları ile yılanı kontrol et!")
    
    # HTML/JavaScript tabanlı yılan oyunu
    snake_game = """
    <div style="display: flex; justify-content: center;">
        <canvas id="snake" width="400" height="400" style="border:5px solid #4CAF50; background:#000;"></canvas>
    </div>
    <script>
    var canvas = document.getElementById('snake');
    var context = canvas.getContext('2d');
    var grid = 16; var count = 0;
    var snake = { x: 160, y: 160, dx: grid, dy: 0, cells: [], maxCells: 4 };
    var apple = { x: 320, y: 320 };
    function getRandomInt(min, max) { return Math.floor(Math.random() * (max - min)) + min; }
    function loop() {
      requestAnimationFrame(loop);
      if (++count < 6) { return; }
      count = 0;
      context.clearRect(0,0,canvas.width,canvas.height);
      snake.x += snake.dx; snake.y += snake.dy;
      if (snake.x < 0) { snake.x = canvas.width - grid; }
      else if (snake.x >= canvas.width) { snake.x = 0; }
      if (snake.y < 0) { snake.y = canvas.height - grid; }
      else if (snake.y >= canvas.height) { snake.y = 0; }
      snake.cells.unshift({x: snake.x, y: snake.y});
      if (snake.cells.length > snake.maxCells) { snake.cells.pop(); }
      context.fillStyle = 'red';
      context.fillRect(apple.x, apple.y, grid-1, grid-1);
      context.fillStyle = 'lime';
      snake.cells.forEach(function(cell, index) {
        context.fillRect(cell.x, cell.y, grid-1, grid-1);
        if (cell.x === apple.x && cell.y === apple.y) {
          snake.maxCells++;
          apple.x = getRandomInt(0, 25) * grid;
          apple.y = getRandomInt(0, 25) * grid;
        }
        for (var i = index + 1; i < snake.cells.length; i++) {
          if (cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {
            snake.x = 160; snake.y = 160; snake.cells = []; snake.maxCells = 4;
            snake.dx = grid; snake.dy = 0;
            apple.x = getRandomInt(0, 25) * grid;
            apple.y = getRandomInt(0, 25) * grid;
          }
        }
      });
    }
    document.addEventListener('keydown', function(e) {
      if (e.which === 37 && snake.dx === 0) { snake.dx = -grid; snake.dy = 0; }
      else if (e.which === 38 && snake.dy === 0) { snake.dy = -grid; snake.dx = 0; }
      else if (e.which === 39 && snake.dx === 0) { snake.dx = grid; snake.dy = 0; }
      else if (e.which === 40 && snake.dy === 0) { snake.dy = grid; snake.dx = 0; }
    });
    requestAnimationFrame(loop);
    </script>
    """
    st.components.v1.html(snake_game, height=450)
