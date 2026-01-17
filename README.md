# 🐆 Pardus ETAP Yapay Zeka Asistanı

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![PyQt](https://img.shields.io/badge/PyQt-6-green.svg)
![Platform](https://img.shields.io/badge/Platform-Pardus%20%7C%20Linux-orange.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

**Pardus ETAP (Etkileşimli Tahta Projesi)** ve Linux tabanlı sistemler için geliştirilmiş, **Google Gemini 2.5** modelini kullanan, modern arayüzlü (GUI) bir masaüstü eğitim asistanıdır.

Bu proje, öğretmenlerin ve öğrencilerin akıllı tahta üzerinde komut satırı ile uğraşmadan, görsel bir arayüz üzerinden yapay zeka ile etkileşime girmesini sağlar.

---

## 🚀 Özellikler

* **Modern Arayüz:** PyQt6 ile geliştirilmiş, yüksek çözünürlük uyumlu şık tasarım.
* **Güçlü Yapay Zeka:** Google'ın en güncel `gemini-2.5-flash` modelini kullanır.
* **Hızlı ve Akıcı:** Arka plan iş parçacığı (QThread) sayesinde arayüz donmadan çalışır.
* **Sistem Dostu:** Sanal ortam (venv) kullanımı sayesinde Pardus sistem dosyalarını bozmaz.
* **Kolay Erişim:** Masaüstü kısayolu ile tek tıkla açılır.

---

## 🛠️ Gereksinimler

Proje çalıştırılmadan önce sistemde aşağıdaki paketlerin kurulu olması gerekir:

* Pardus 21/23/25 veya Debian tabanlı bir dağıtım.
* Python 3.x
* İnternet bağlantısı.
* Google AI Studio API Anahtarı.

---

## 📦 Kurulum

Projeyi bilgisayarınıza kurmak için terminali açın ve aşağıdaki adımları sırasıyla uygulayın.

### 1. Sistem Paketlerini Güncelleyin
```bash
sudo apt update
sudo apt install python3-venv python3-pip git -y

📄 Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Açık kaynaklıdır ve eğitim amaçlı özgürce kullanılabilir.

<p align="center"> <sub>Pardus ve Açık Kaynak Gönüllüleri Tarafından ❤️ ile Hazırlanmıştır.</sub> </p>
