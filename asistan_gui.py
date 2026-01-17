
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTextEdit, 
                             QLineEdit, QPushButton, QLabel)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QCursor
from google import genai
from google.genai import types

# --- AYARLAR ---
API_KEY = "BURAYA_API_ANAHTARINIZI_YAZIN"
MODEL_ADI = "gemini-2.5-flash" # En güncel ve hızlı model

# --- ARKA PLAN İŞÇİSİ (THREAD) ---
# Arayüzün donmaması için API isteği ayrı kanaldan yapılır
class GeminiWorker(QThread):
    cevap_geldi = pyqtSignal(str)

    def __init__(self, soru):
        super().__init__()
        self.soru = soru

    def run(self):
        try:
            client = genai.Client(api_key=API_KEY)
            response = client.models.generate_content(
                model=MODEL_ADI,
                contents=self.soru,
                config=types.GenerateContentConfig(
                    system_instruction="Sen Pardus ETAP akıllı tahtasında çalışan yardımcı bir eğitim asistanısın. Cevapların kibar, Türkçe, kısa ve öğrenciler için eğitici olsun."
                )
            )
            self.cevap_geldi.emit(response.text)
        except Exception as e:
            self.cevap_geldi.emit(f"Bağlantı Hatası: {str(e)}")

# --- ANA PENCERE (GUI) ---
class PardusAsistan(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Pencere Ayarları
        self.setWindowTitle('Pardus ETAP Asistanı (v2.0)')
        self.setGeometry(100, 100, 700, 600)
        self.setStyleSheet("background-color: #f4f6f9;") # Göz yormayan gri

        layout = QVBoxLayout()

        # Başlık (Logo Alanı)
        baslik = QLabel("🐆 Pardus Yapay Zeka Asistanı")
        baslik.setFont(QFont('Segoe UI', 16, QFont.Weight.Bold))
        baslik.setAlignment(Qt.AlignmentFlag.AlignCenter) # PyQt6 Hizalama
        baslik.setStyleSheet("color: #d35400; margin: 15px;")
        layout.addWidget(baslik)

        # Sohbet Geçmişi
        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        self.chat_area.setFont(QFont('Segoe UI', 12))
        self.chat_area.setStyleSheet("""
            QTextEdit {
                background-color: white;
                border: 1px solid #bdc3c7;
                border-radius: 10px;
                padding: 15px;
            }
        """)
        layout.addWidget(self.chat_area)

        # Soru Giriş Kutusu
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Öğretmenim, sorunuzu buraya yazın...")
        self.input_box.setFont(QFont('Segoe UI', 12))
        self.input_box.setStyleSheet("""
            QLineEdit {
                border: 2px solid #3498db;
                border-radius: 8px;
                padding: 10px;
                background-color: white;
            }
            QLineEdit:focus {
                border: 2px solid #2980b9;
            }
        """)
        self.input_box.returnPressed.connect(self.soru_gonder)
        layout.addWidget(self.input_box)

        # Gönder Butonu
        self.btn_gonder = QPushButton("CEVAPLA 🚀")
        self.btn_gonder.setFont(QFont('Segoe UI', 11, QFont.Weight.Bold))
        self.btn_gonder.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_gonder.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border-radius: 8px;
                padding: 12px;
                border: none;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        self.btn_gonder.clicked.connect(self.soru_gonder)
        layout.addWidget(self.btn_gonder)

        self.setLayout(layout)

    def soru_gonder(self):
        soru = self.input_box.text().strip()
        if not soru:
            return

        # Kullanıcı sorusunu ekrana bas
        self.chat_area.append(f"<div style='margin-bottom:10px;'><b style='color:#2980b9'>Siz:</b> {soru}</div>")
        
        # Arayüzü kilitle
        self.input_box.clear()
        self.input_box.setDisabled(True)
        self.btn_gonder.setText("Düşünüyor...")
        
        # İşçiyi başlat
        self.worker = GeminiWorker(soru)
        self.worker.cevap_geldi.connect(self.cevabi_yaz)
        self.worker.start()

    def cevabi_yaz(self, cevap):
        # Markdown satırlarını HTML break ile değiştir
        temiz_cevap = cevap.replace("\n", "<br>")
        
        self.chat_area.append(f"<div style='background-color:#ecf0f1; padding:10px; border-radius:10px; margin-bottom:20px;'><b style='color:#d35400'>Asistan:</b><br>{temiz_cevap}</div>")
        
        # Otomatik aşağı kaydır
        self.chat_area.moveCursor(self.chat_area.textCursor().MoveOperation.End)
        
        # Arayüzü aç
        self.input_box.setDisabled(False)
        self.btn_gonder.setText("CEVAPLA 🚀")
        self.input_box.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PardusAsistan()
    ex.show()
    sys.exit(app.exec())