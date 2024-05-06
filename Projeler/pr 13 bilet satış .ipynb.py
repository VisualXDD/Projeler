{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "83a2cee8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import ttk, messagebox\n",
    "import random\n",
    "\n",
    "class Kullanici:\n",
    "    def __init__(self, ad, soyad, email):\n",
    "        self.ad = ad\n",
    "        self.soyad = soyad\n",
    "        self.email = email\n",
    "        self.biletler = []\n",
    "\n",
    "class Etkinlik:\n",
    "    def __init__(self, ad, tarih, mekan):\n",
    "        self.ad = ad\n",
    "        self.tarih = tarih\n",
    "        self.mekan = mekan\n",
    "\n",
    "class Bilet:\n",
    "    def __init__(self, numara, etkinlik):\n",
    "        self.numara = numara\n",
    "        self.etkinlik = etkinlik\n",
    "\n",
    "class Arayuz:\n",
    "    def __init__(self, root):\n",
    "        self.root = root\n",
    "        self.root.title(\"Etkinlik ve Bilet Yönetimi\")\n",
    "        self.root.configure(background=\"white\")\n",
    "\n",
    "        # Kullanıcı bilgileri girişi\n",
    "        self.ad_label = ttk.Label(root, text=\"Ad:\")\n",
    "        self.ad_label.grid(row=0, column=0, padx=5, pady=5, sticky=\"e\")\n",
    "        self.ad_entry = ttk.Entry(root)\n",
    "        self.ad_entry.grid(row=0, column=1, padx=5, pady=5, sticky=\"we\")\n",
    "\n",
    "        self.soyad_label = ttk.Label(root, text=\"Soyad:\")\n",
    "        self.soyad_label.grid(row=1, column=0, padx=5, pady=5, sticky=\"e\")\n",
    "        self.soyad_entry = ttk.Entry(root)\n",
    "        self.soyad_entry.grid(row=1, column=1, padx=5, pady=5, sticky=\"we\")\n",
    "\n",
    "        self.email_label = ttk.Label(root, text=\"E-posta:\")\n",
    "        self.email_label.grid(row=2, column=0, padx=5, pady=5, sticky=\"e\")\n",
    "        self.email_entry = ttk.Entry(root)\n",
    "        self.email_entry.grid(row=2, column=1, padx=5, pady=5, sticky=\"we\")\n",
    "\n",
    "        self.giris_btn = ttk.Button(root, text=\"Giriş\", command=self.giris)\n",
    "        self.giris_btn.grid(row=3, columnspan=2, padx=5, pady=5)\n",
    "\n",
    "        # Kullanıcı bilgi paneli\n",
    "        self.kullanici_bilgi = tk.Text(root, height=2, width=30)\n",
    "        self.kullanici_bilgi.grid(row=4, columnspan=2, padx=5, pady=5, sticky=\"we\")\n",
    "\n",
    "        # Bilet listesi\n",
    "        self.bilet_listesi = tk.Listbox(root, height=5, width=50)\n",
    "        self.bilet_listesi.grid(row=5, columnspan=2, padx=5, pady=5, sticky=\"we\")\n",
    "        self.bilet_listesi.bind(\"<Double-Button-1>\", self.bilet_detay)\n",
    "\n",
    "    def giris(self):\n",
    "        ad = self.ad_entry.get()\n",
    "        soyad = self.soyad_entry.get()\n",
    "        email = self.email_entry.get()\n",
    "\n",
    "        self.kullanici = Kullanici(ad, soyad, email)\n",
    "        self.kullanici_bilgi.insert(tk.END, f\"Giriş başarılı! Hoş geldiniz, {ad} {soyad}.\\n\")\n",
    "\n",
    "        self.ikinci_sayfa = IkinciSayfa(self.root, self.kullanici, self.bilet_listesi)\n",
    "\n",
    "    def bilet_detay(self, event):\n",
    "        selection = event.widget.curselection()\n",
    "        if selection:\n",
    "            index = selection[0]\n",
    "            bilet = self.kullanici.biletler[index]\n",
    "\n",
    "            bilet_detay = BiletDetay(self.root, bilet, self.kullanici)\n",
    "\n",
    "class IkinciSayfa:\n",
    "    def __init__(self, root, kullanici, bilet_listesi):\n",
    "        self.root = root\n",
    "        self.kullanici = kullanici\n",
    "        self.bilet_listesi = bilet_listesi\n",
    "\n",
    "        self.ikinci_sayfa = tk.Toplevel(self.root)\n",
    "        self.ikinci_sayfa.title(\"Bilet İşlemleri\")\n",
    "        self.ikinci_sayfa.configure(background=\"white\")\n",
    "\n",
    "        self.etkinlikler = [\"Konser\", \"Spor Etkinliği\", \"Tiyatro Gösterisi\", \"Konferans\"]\n",
    "\n",
    "        ttk.Label(self.ikinci_sayfa, text=\"Etkinlik Seç:\").grid(row=0, column=0, padx=5, pady=5, sticky=\"e\")\n",
    "        self.etkinlik_combo = ttk.Combobox(self.ikinci_sayfa, values=self.etkinlikler)\n",
    "        self.etkinlik_combo.grid(row=0, column=1, padx=5, pady=5, sticky=\"we\")\n",
    "\n",
    "        self.bilet_al_btn = ttk.Button(self.ikinci_sayfa, text=\"Bilet Al\", command=self.bilet_al)\n",
    "        self.bilet_al_btn.grid(row=1, columnspan=2, padx=5, pady=5)\n",
    "\n",
    "    def bilet_al(self):\n",
    "        etkinlik = self.etkinlik_combo.get()\n",
    "        yeni_etkinlik = Etkinlik(etkinlik, \"10.10.2024\", \"Örnek Mekan\")\n",
    "        bilet_numarasi = random.randint(10000, 99999)\n",
    "        yeni_bilet = Bilet(bilet_numarasi, yeni_etkinlik)\n",
    "\n",
    "        if len([b for b in self.kullanici.biletler if b.etkinlik.ad == yeni_etkinlik.ad]) > 0:\n",
    "            messagebox.showerror(\"Hata\", \"Aynı etkinlikten birden fazla bilet alınamaz!\")\n",
    "        else:\n",
    "            self.kullanici.biletler.append(yeni_bilet)\n",
    "            self.bilet_listesi.insert(tk.END, f\"{yeni_etkinlik.ad} - Bilet Numarası: {bilet_numarasi}\")\n",
    "\n",
    "class BiletDetay:\n",
    "    def __init__(self, root, bilet, kullanici):\n",
    "        self.root = root\n",
    "        self.bilet = bilet\n",
    "        self.kullanici = kullanici\n",
    "\n",
    "        self.bilet_detay = tk.Toplevel(self.root)\n",
    "        self.bilet_detay.title(\"Bilet Detayı\")\n",
    "        self.bilet_detay.configure(background=\"white\")\n",
    "\n",
    "        ttk.Label(self.bilet_detay, text=f\"{self.bilet.etkinlik.ad} Bilet Detayı\").grid(row=0, column=0, columnspan=2, padx=5, pady=5)\n",
    "\n",
    "        ttk.Label(self.bilet_detay, text=f\"Bilet Numarası: {self.bilet.numara}\").grid(row=1, column=0, columnspan=2, padx=5, pady=5)\n",
    "\n",
    "        ttk.Label(self.bilet_detay, text=\"Bilet İşlemleri\").grid(row=2, column=0, columnspan=2, padx=5, pady=5)\n",
    "\n",
    "        self.satis_btn = ttk.Button(self.bilet_detay, text=\"Satış Yap\", command=self.satis)\n",
    "        self.satis_btn.grid(row=3, column=0, padx=5, pady=5)\n",
    "\n",
    "        self.iade_btn = ttk.Button(self.bilet_detay, text=\"İade Yap\", command=self.iade)\n",
    "        self.iade_btn.grid(row=3, column=1, padx=5, pady=5)\n",
    "\n",
    "    def satis(self):\n",
    "        self.kullanici.biletler.remove(self.bilet)\n",
    "        messagebox.showinfo(\"Bilgi\", \"Bilet satışı başarıyla gerçekleştirildi.\")\n",
    "        self.root.destroy()\n",
    "\n",
    "    def iade(self):\n",
    "        self.kullanici.biletler.remove(self.bilet)\n",
    "        messagebox.showinfo(\"Bilgi\", \"Bilet iadesi başarıyla gerçekleştirildi.\")\n",
    "        self.root.destroy()\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    root = tk.Tk()\n",
    "    uygulama = Arayuz(root)\n",
    "    root.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0917d01b-4c43-4c11-a5fc-fe92f70d7d59",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
