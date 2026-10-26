# turkiye-dis-ticaret-agi
# Türkiye Merkezli Dış Ticaret Ağ Analizi

Bu proje, Türkiye'nin ana ticaret ortakları arasındaki dış ticaret akışlarını Sosyal Ağ Analizi (SNA) yöntemleriyle incelemektedir.

## 1. Toplanmış Veri ve Kenar Listesi (Edge List)
Veri seti `kenar_listesi.csv` dosyasında yer almaktadır. Türkiye ve başlıca küresel ticaret ortaklarının yıllık ithalat/ihracat hacimlerini içermektedir.

## 2. Temel Ağ İstatistikleri (26 Ekim Ara Kontrol Metrikleri)
- **Düğüm (Node) Sayısı:** 8 (Analize dahil edilen ülke sayısı)
- **Kenar (Edge) Sayısı:** 12 (Ülkeler arası ticaret bağları)
- **Ağ Yoğunluğu (Density):** 0.2143 (Olası tüm bağlantıların gerçekleşme oranı)
- **Bileşen (Component) Sayısı:** 1 (Zayıf bağlı tek bir bütünleşik ticaret ağı)

## 3. Kullanılan Teknolojiler
- Python (Pandas, NetworkX, PyVis)
