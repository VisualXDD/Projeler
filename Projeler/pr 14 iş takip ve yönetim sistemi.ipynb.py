{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ac157741-f196-44a0-bd02-7a09403276b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import ttk, messagebox\n",
    "\n",
    "class Proje:\n",
    "    def __init__(self, ad, baslangic_tarihi, bitis_tarihi):\n",
    "        self.ad = ad\n",
    "        self.baslangic_tarihi = baslangic_tarihi\n",
    "        self.bitis_tarihi = bitis_tarihi\n",
    "        self.gorevler = []\n",
    "\n",
    "    def gorev_ekle(self, gorev):\n",
    "        self.gorevler.append(gorev)\n",
    "\n",
    "    def gorev_sil(self, gorev):\n",
    "        self.gorevler.remove(gorev)\n",
    "\n",
    "class Gorev:\n",
    "    def __init__(self, ad, calisan):\n",
    "        self.ad = ad\n",
    "        self.calisan = calisan\n",
    "\n",
    "class Calisan:\n",
    "    def __init__(self, ad):\n",
    "        self.ad = ad\n",
    "\n",
    "class Uygulama:\n",
    "    def __init__(self, root):\n",
    "        self.root = root\n",
    "        self.root.title(\"Proje Yönetim Sistemi\")\n",
    "\n",
    "        self.stil = ttk.Style()\n",
    "        self.stil.theme_use(\"clam\")  # Arayüz teması\n",
    "\n",
    "        self.proje_listesi = []\n",
    "        self.calisan_listesi = [Calisan(\"Cem\"), Calisan(\"Kemal\"), Calisan(\"Beliz\"), Calisan(\"Eda\")]\n",
    "\n",
    "        self.proje_label = ttk.Label(root, text=\"Proje Adı:\", font=(\"Helvetica\", 12))\n",
    "        self.proje_label.grid(row=0, column=0, sticky=\"w\")\n",
    "        self.proje_entry = ttk.Entry(root, font=(\"Helvetica\", 12))\n",
    "        self.proje_entry.grid(row=0, column=1)\n",
    "\n",
    "        self.baslangic_label = ttk.Label(root, text=\"Başlangıç Tarihi:\", font=(\"Helvetica\", 12))\n",
    "        self.baslangic_label.grid(row=1, column=0, sticky=\"w\")\n",
    "        self.baslangic_entry = ttk.Entry(root, font=(\"Helvetica\", 12))\n",
    "        self.baslangic_entry.grid(row=1, column=1)\n",
    "\n",
    "        self.bitis_label = ttk.Label(root, text=\"Bitiş Tarihi:\", font=(\"Helvetica\", 12))\n",
    "        self.bitis_label.grid(row=2, column=0, sticky=\"w\")\n",
    "        self.bitis_entry = ttk.Entry(root, font=(\"Helvetica\", 12))\n",
    "        self.bitis_entry.grid(row=2, column=1)\n",
    "\n",
    "        self.proje_ekle_button = ttk.Button(root, text=\"Proje Ekle\", command=self.proje_ekle, style=\"Gozde.TButton\")\n",
    "        self.proje_ekle_button.grid(row=3, columnspan=2)\n",
    "\n",
    "        self.proje_listbox = tk.Listbox(root, font=(\"Helvetica\", 12))\n",
    "        self.proje_listbox.grid(row=4, columnspan=2, sticky=\"nsew\")\n",
    "        self.proje_listbox.bind(\"<Double-Button-1>\", self.proje_secildi)\n",
    "\n",
    "        self.root.columnconfigure(1, weight=1)\n",
    "        self.root.rowconfigure(4, weight=1)\n",
    "\n",
    "        self.stil.configure(\"Gozde.TButton\", font=(\"Helvetica\", 12))\n",
    "\n",
    "    def proje_ekle(self):\n",
    "        proje_adi = self.proje_entry.get()\n",
    "        baslangic_tarihi = self.baslangic_entry.get()\n",
    "        bitis_tarihi = self.bitis_entry.get()\n",
    "\n",
    "        if proje_adi and baslangic_tarihi and bitis_tarihi:\n",
    "            yeni_proje = Proje(proje_adi, baslangic_tarihi, bitis_tarihi)\n",
    "            self.proje_listesi.append(yeni_proje)\n",
    "            self.proje_listbox.insert(tk.END, yeni_proje.ad)\n",
    "            messagebox.showinfo(\"Başarılı\", \"Proje başarıyla eklendi.\")\n",
    "        else:\n",
    "            messagebox.showerror(\"Hata\", \"Lütfen tüm alanları doldurun.\")\n",
    "\n",
    "    def proje_secildi(self, event):\n",
    "        if self.proje_listbox.curselection():\n",
    "            secili_proje_index = self.proje_listbox.curselection()[0]\n",
    "            secili_proje = self.proje_listesi[secili_proje_index]\n",
    "            self.proje_detaylari_goster(secili_proje)\n",
    "\n",
    "    def proje_detaylari_goster(self, proje):\n",
    "        pencere = tk.Toplevel(self.root)\n",
    "        pencere.title(\"Proje Detayları\")\n",
    "\n",
    "        ttk.Label(pencere, text=\"Proje Adı:\", font=(\"Helvetica\", 12)).grid(row=0, column=0, sticky=\"w\")\n",
    "        ttk.Label(pencere, text=proje.ad, font=(\"Helvetica\", 12)).grid(row=0, column=1, sticky=\"w\")\n",
    "\n",
    "        ttk.Label(pencere, text=\"Başlangıç Tarihi:\", font=(\"Helvetica\", 12)).grid(row=1, column=0, sticky=\"w\")\n",
    "        ttk.Label(pencere, text=proje.baslangic_tarihi, font=(\"Helvetica\", 12)).grid(row=1, column=1, sticky=\"w\")\n",
    "\n",
    "        ttk.Label(pencere, text=\"Bitiş Tarihi:\", font=(\"Helvetica\", 12)).grid(row=2, column=0, sticky=\"w\")\n",
    "        ttk.Label(pencere, text=proje.bitis_tarihi, font=(\"Helvetica\", 12)).grid(row=2, column=1, sticky=\"w\")\n",
    "\n",
    "        ttk.Label(pencere, text=\"Görevler:\", font=(\"Helvetica\", 12)).grid(row=3, column=0, sticky=\"w\")\n",
    "        for i, gorev in enumerate(proje.gorevler):\n",
    "            ttk.Label(pencere, text=f\"{i + 1}. Görev: {gorev.ad}, Çalışan: {gorev.calisan.ad}\", font=(\"Helvetica\", 12)).grid(row=i + 4, columnspan=2, sticky=\"w\")\n",
    "\n",
    "        ttk.Button(pencere, text=\"Görev Ekle\", command=lambda: self.gorev_ekle_penceresi(proje), style=\"Gozde.TButton\").grid(row=len(proje.gorevler) + 4, columnspan=2)\n",
    "\n",
    "    def gorev_ekle_penceresi(self, proje):\n",
    "        pencere = tk.Toplevel(self.root)\n",
    "        pencere.title(\"Görev Ekle\")\n",
    "\n",
    "        ttk.Label(pencere, text=\"Görev Adı:\", font=(\"Helvetica\", 12)).grid(row=0, column=0, sticky=\"w\")\n",
    "        gorev_entry = ttk.Entry(pencere, font=(\"Helvetica\", 12))\n",
    "        gorev_entry.grid(row=0, column=1)\n",
    "\n",
    "        ttk.Label(pencere, text=\"Çalışan:\", font=(\"Helvetica\", 12)).grid(row=1, column=0, sticky=\"w\")\n",
    "        calisan_secim = ttk.Combobox(pencere, values=[calisan.ad for calisan in self.calisan_listesi], font=(\"Helvetica\", 12))\n",
    "        calisan_secim.grid(row=1, column=1)\n",
    "\n",
    "        def gorev_ekle():\n",
    "            gorev_adi = gorev_entry.get()\n",
    "            secili_calisan_index = calisan_secim.current()\n",
    "\n",
    "            if gorev_adi and secili_calisan_index != -1:\n",
    "                secili_calisan = self.calisan_listesi[secili_calisan_index]\n",
    "                proje.gorev_ekle(Gorev(gorev_adi, secili_calisan))\n",
    "                pencere.destroy()\n",
    "                self.proje_detaylari_goster(proje)\n",
    "            else:\n",
    "                messagebox.showerror(\"Hata\", \"Lütfen tüm alanları doldurun.\")\n",
    "\n",
    "        ttk.Button(pencere, text=\"Ekle\", command=gorev_ekle, style=\"Gozde.TButton\").grid(row=2, columnspan=2)\n",
    "\n",
    "root = tk.Tk()\n",
    "uygulama = Uygulama(root)\n",
    "root.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b487ab3d-c1f1-4617-a30d-3804ec7029c5",
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
