import pandas as pd
import networkx as nx

# Kenar listesini oku
df = pd.read_csv("kenar_listesi.csv")

# Yönlü Ağ (DiGraph) oluştur
G = nx.from_pandas_edgelist(
    df, 
    source='Kaynak', 
    target='Hedef', 
    edge_attr='Hacim_Milyar_USD', 
    create_using=nx.DiGraph()
)

# Temel Ağ İstatistikleri Hesaplama
dugum_sayisi = G.number_of_nodes()
kenar_sayisi = G.number_of_edges()
yogunluk = nx.density(G)
bilesen_sayisi = nx.number_weakly_connected_components(G)

print(f"Düğüm Sayısı: {dugum_sayisi}")
print(f"Kenar Sayısı: {kenar_sayisi}")
print(f"Ağ Yoğunluğu: {yogunluk:.4f}")
print(f"Bileşen Sayısı: {bilesen_sayisi}")
