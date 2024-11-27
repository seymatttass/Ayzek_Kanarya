# Ayzek Kanarya: Sağlıklı ve Hasta Bitki Sınıflandırma Projesi

Bu depo, **Ayzek Kanarya** takımı olarak katıldığımız **TEKNOFEST 2024 2242 Üniversite Öğrencileri Araştırma Yarışması** için geliştirdiğimiz projeye ait kodları ve dokümantasyonu içermektedir. Projemiz, sağlıklı ve hasta bitki görsellerini analiz ederek hasta bitkileri tespit etmeyi ve sınıflandırmayı amaçlamaktadır.

## Proje Hakkında

### Problem Tanımı
Bitki hastalıkları, tarımsal üretimi olumsuz etkileyen önemli bir faktördür. Erken teşhis ve doğru müdahale, verimliliği artırmanın yanı sıra ekonomik kayıpları da önleyebilir. Ancak geleneksel yöntemler zaman alıcı ve hata yapmaya açıktır. Bu projede, görüntü işleme ve derin öğrenme teknolojileri kullanılarak hastalıklı bitkilerin otomatik olarak tespit edilmesi hedeflenmiştir.

### Çözümümüz
Projemizde, bitki yapraklarının görüntülerini işleyerek hastalıklı ve sağlıklı sınıflandırması yapan bir model geliştirdik. Derin öğrenme tabanlı bu çözüm, çiftçilere ve tarım uzmanlarına hızlı ve doğru bir teşhis aracı sunmayı amaçlar.

---

## Proje Özellikleri
- **Sınıflandırma Modeli:** Görüntüler, bir derin öğrenme modeli ile işlenerek bitkilerin sağlıklı veya hastalıklı olduğu tespit edilmektedir.
- **Modelin Eğitimi:** 
  - Eğitim, sağlıklı ve hastalıklı bitki görüntülerinden oluşan bir veri seti üzerinde gerçekleştirilmiştir.
  - Kullanılan modeller arasında **InceptionV3**, **CNN** ,**ResNet-50** ,**MobileNetV2**,**VGG-16** ve **DenseNet121** bulunmaktadır.
- **Başarı Oranı:** Modelimiz, yüksek bir doğruluk oranı sergilemiştir.
- **Kullanım Alanları:** 
  - Çiftlik yönetim sistemleri
  - Tarım teknolojileri
  - Sürdürülebilir tarım uygulamaları

---

## Depo İçeriği
Bu depo şu dosya ve klasörleri içermektedir:

- **`models/`**  
  Eğitim ve test işlemleri için kullanılan modellerin kodları.

- **`README.md`**  
  Bu dosya, proje ile ilgili genel bilgileri içerir.

---

## Kullanılan Teknolojiler
Projede kullanılan ana teknolojiler şunlardır:
- **Python:** Model geliştirme ve veri işleme
- **TensorFlow ve Keras:** Derin öğrenme modellerinin eğitimi ve uygulanması
- **OpenCV:** Görüntü işleme
- **NumPy ve Pandas:** Veri analizi
- **Matplotlib ve Seaborn:** Veri görselleştirme

---

## Çalıştırma Talimatları
Projeyi çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. Depoyu klonlayın:  
   ```bash
   git clone https://github.com/kullanici-adi/ayzek-kanarya.git
   cd ayzek-kanarya


2. Gerekli Python kütüphanelerini yükleyin:
   pip install -r requirements.txt


## Katkı Sağlama
Projeye katkıda bulunmak isterseniz, lütfen bir pull request oluşturun veya bir issue açın. Tüm katkılar değerlendirilip projeye uygun olanlar entegre edilecektir.


## Başarılarımız
Bu proje, 2242 Üniversite Öğrencileri Araştırma Yarışması'nda finale kalma başarısı göstermiştir. Elde edilen bu başarı, takımımızın azmi ve yenilikçi yaklaşımlarının bir sonucudur.

## İletişim
Proje ile ilgili her türlü soru ve geri bildirim için bize ulaşabilirsiniz:

Takım Adı: Ayzek Kanarya
E-posta: seyyyma08@gmail.com
GitHub: Ayzek Kanarya



   
