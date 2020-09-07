"""
This is the LifeStore-SalesList data:
lifestore-searches = [id_search, id product]
lifestore-sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore-products = [id_product, name, price, category, stock]
"""

lifestore_products = [
    [1, 'Procesador AMD Ryzen 3 3300X S-AM4, 3.80GHz, Quad-Core, 16MB L2 Cache', 3019, 'procesadores', 16],
    [2, 'Procesador AMD Ryzen 5 3600, S-AM4, 3.60GHz, 32MB L3 Cache, con Disipador Wraith Stealth', 4209, 'procesadores', 182],
    [3, 'Procesador AMD Ryzen 5 2600, S-AM4, 3.40GHz, Six-Core, 16MB L3 Cache, con Disipador Wraith Stealth', 3089, 'procesadores', 987],
    [4, 'Procesador AMD Ryzen 3 3200G con Gráficos Radeon Vega 8, S-AM4, 3.60GHz, Quad-Core, 4MB L3, con Disipador Wraith Spire', 2209, 'procesadores', 295],
    [5, 'Procesador Intel Core i3-9100F, S-1151, 3.60GHz, Quad-Core, 6MB Cache (9na. Generación - Coffee Lake)', 1779, 'procesadores', 130],
    [6, 'Procesador Intel Core i9-9900K, S-1151, 3.60GHz, 8-Core, 16MB Smart Cache (9na. Generación Coffee Lake)', 11809, 'procesadores', 54],
    [7, 'Procesador Intel Core i7-9700K, S-1151, 3.60GHz, 8-Core, 12MB Smart Cache (9na. Generación Coffee Lake)', 8559, 'procesadores', 114],
    [8, 'Procesador Intel Core i5-9600K, S-1151, 3.70GHz, Six-Core, 9MB Smart Cache (9na. Generiación - Coffee Lake)', 5399, 'procesadores', 8],
    [9, 'Procesador Intel Core i3-8100, S-1151, 3.60GHz, Quad-Core, 6MB Smart Cache (8va. Generación - Coffee Lake)', 2549, 'procesadores', 35],
    [10, 'MSI GeForce 210, 1GB GDDR3, DVI, VGA, HDCP, PCI Express 2.0', 889, 'tarjetas de video', 13],
    [11, 'Tarjeta de Video ASUS AMD Radeon RX 570, 4GB 256-bit GDDR5, PCI Express 3.0', 7399, 'tarjetas de video', 2],
    [12, 'Tarjeta de Video ASUS NVIDIA GeForce GTX 1660 SUPER EVO OC, 6GB 192-bit GDDR6, PCI Express x16 3.0', 6619, 'tarjetas de video', 0],
    [13, 'Tarjeta de Video Asus NVIDIA GeForce GTX 1050 Ti Phoenix, 4GB 128-bit GDDR5, PCI Express 3.0', 3989, 'tarjetas de video', 1],
    [14, 'Tarjeta de Video EVGA NVIDIA GeForce GT 710, 2GB 64-bit GDDR3, PCI Express 2.0', 1439, 'tarjetas de video', 36],
    [15, 'Tarjeta de Video EVGA NVIDIA GeForce GTX 1660 Ti SC Ultra Gaming, 6GB 192-bit GDDR6, PCI 3.0', 8439, 'tarjetas de video', 15],
    [16, 'Tarjeta de Video EVGA NVIDIA GeForce RTX 2060 SC ULTRA Gaming, 6GB 192-bit GDDR6, PCI Express 3.0', 9799, 'tarjetas de video', 10],
    [17, 'Tarjeta de Video Gigabyte AMD Radeon R7 370 OC, 2GB 256-bit GDDR5, PCI Express 3.0', 4199, 'tarjetas de video', 1],
    [18, 'Tarjeta de Video Gigabyte NVIDIA GeForce GT 1030, 2GB 64-bit GDDR5, PCI Express x16 3.0', 2199, 'tarjetas de video', 5],
    [19, 'Tarjeta de Video Gigabyte NVIDIA GeForce GTX 1650 OC Low Profile, 4GB 128-bit GDDR5, PCI Express 3.0 x16', 4509, 'tarjetas de video', 8],
    [20, 'Tarjeta de Video Gigabyte NVIDIA GeForce RTX 2060 SUPER WINDFORCE OC, 8 GB 256 bit GDDR6, PCI Express x16 3.0', 11509, 'tarjetas de video', 10],
    [21, 'Tarjeta de Video MSI AMD Mech Radeon RX 5500 XT MECH Gaming OC, 8GB 128-bit GDDR6, PCI Express 4.0', 5159, 'tarjetas de video', 0],
    [22, 'Tarjeta de Video MSI NVIDIA GeForce GTX 1050 Ti OC, 4GB 128-bit GDDR5, PCI Express x16 3.0', 3429, 'tarjetas de video', 0],
    [23, 'Tarjeta de Video MSI Radeon X1550, 128MB 64 bit GDDR2, PCI Express x16', 909, 'tarjetas de video', 10],
    [24, 'Tarjeta de Video PNY NVIDIA GeForce RTX 2080, 8GB 256-bit GDDR6, PCI Express 3.0\xa0', 30449, 'tarjetas de video', 2],
    [25, 'Tarjeta de Video Sapphire AMD Pulse Radeon RX 5500 XT Gaming, 8GB 128-bit GDDR6, PCI Express 4.0', 5529, 'tarjetas de video', 10],
    [26, 'Tarjeta de Video VisionTek AMD Radeon HD 5450, 1GB DDR3, PCI Express x16 2.1', 1249, 'tarjetas de video', 180],
    [27, 'Tarjeta de Video VisionTek AMD Radeon HD5450, 2GB GDDR3, PCI Express x16', 2109, 'tarjetas de video', 43],
    [28, 'Tarjeta de Video Zotac NVIDIA GeForce GTX 1660 Ti, 6GB 192-bit GDDR6, PCI Express x16 3.0', 9579, 'tarjetas de video', 3],
    [29, 'Tarjeta Madre ASUS micro ATX TUF B450M-PLUS GAMING, S-AM4, AMD B450, HDMI, 64GB DDR4 para AMD', 2499, 'tarjetas madre', 10],
    [30, 'Tarjeta Madre AORUS ATX Z390 ELITE, S-1151, Intel Z390, HDMI, 64GB DDR4 para Intel', 4029, 'tarjetas madre', 50],
    [31, 'Tarjeta Madre AORUS micro ATX B450 AORUS M (rev. 1.0), S-AM4, AMD B450, HDMI, 64GB DDR4 para AMD', 2229, 'tarjetas madre', 120],
    [32, 'Tarjeta Madre ASRock Z390 Phantom Gaming 4, S-1151, Intel Z390, HDMI, 64GB DDR4 para Intel\xa0', 4309, 'tarjetas madre', 10],
    [33, 'Tarjeta Madre ASUS ATX PRIME Z390-A, S-1151, Intel Z390, HDMI, 64GB DDR4 para Intel\xa0', 4269, 'tarjetas madre', 43],
    [34, 'Tarjeta Madre ASUS ATX ROG STRIX B550-F GAMING WI-FI, S-AM4, AMD B550, HDMI, max. 128GB DDR4 para AMD', 5289, 'tarjetas madre', 2],
    [35, 'Tarjeta Madre Gigabyte micro ATX Z390 M GAMING, S-1151, Intel Z390, HDMI, 64GB DDR4 para Intel\xa0', 3419, 'tarjetas madre', 30],
    [36, 'Tarjeta Madre Gigabyte micro ATX Z490M GAMING X (rev. 1.0), Intel Z490, HDMI, 128GB DDR4 para Intel', 4159, 'tarjetas madre', 10],
    [37, 'Tarjeta Madre ASRock ATX Z490 STEEL LEGEND, S-1200, Intel Z490, HDMI, 128GB DDR4 para Intel', 4289, 'tarjetas madre', 60],
    [38, 'Tarjeta Madre Gigabyte Micro ATX H310M DS2 2.0, S-1151, Intel H310, 32GB DDR4 para Intel\xa0', 1369, 'tarjetas madre', 15],
    [39, 'ASUS T. Madre uATX M4A88T-M, S-AM3, DDR3 para Phenom II/Athlon II/Sempron 100', 2169, 'tarjetas madre', 98],
    [40, 'Tarjeta Madre Gigabyte XL-ATX TRX40 Designare, S-sTRX4, AMD TRX40, 256GB DDR4 para AMD', 17439, 'tarjetas madre', 1],
    [41, 'Tarjeta Madre ASUS micro ATX Prime H370M-Plus/CSM, S-1151, Intel H370, HDMI, 64GB DDR4 para Intel', 3329, 'tarjetas madre', 286],
    [42, 'Tarjeta Madre ASRock Micro ATX B450M Steel Legend, S-AM4, AMD B450, HDMI, 64GB DDR4 para AMD', 1779, 'tarjetas madre', 0],
    [43, 'Tarjeta Madre ASUS ATX ROG STRIX Z390-E GAMING, S-1151, Intel Z390, HDMI, 64GB DDR4 para Intel', 6369, 'tarjetas madre', 5],
    [44, 'Tarjeta Madre MSI ATX B450 TOMAHAWK MAX, S-AM4, AMD B450, 64GB DDR4 para AMD', 2759, 'tarjetas madre', 0],
    [45, 'Tarjeta Madre ASRock ATX H110 Pro BTC+, S-1151, Intel H110, 32GB DDR4, para Intel', 2869, 'tarjetas madre', 25],
    [46, 'Tarjeta Madre Gigabyte micro ATX GA-H110M-DS2, S-1151, Intel H110, 32GB DDR4 para Intel', 1539, 'tarjetas madre', 49],
    [47, 'SSD XPG SX8200 Pro, 256GB, PCI Express, M.2', 1209, 'discos duros', 8],
    [48, 'SSD Kingston A2000 NVMe, 1TB, PCI Express 3.0, M2', 2559, 'discos duros', 50],
    [49, 'Kit SSD Kingston KC600, 1TB, SATA III, 2.5, 7mm', 3139, 'discos duros', 3],
    [50, 'SSD Crucial MX500, 1TB, SATA III, M.2', 2949, 'discos duros', 4],
    [51, 'SSD Kingston UV500, 480GB, SATA III, mSATA', 2399, 'discos duros', 0],
    [52, 'SSD Western Digital WD Blue 3D NAND, 2TB, M.2', 5659, 'discos duros', 13],
    [53, 'SSD Addlink Technology S70, 512GB, PCI Express 3.0, M.2', 2039, 'discos duros', 1],
    [54, "SSD Kingston A400, 120GB, SATA III, 2.5'', 7mm", 259, 'discos duros', 300],
    [55, 'SSD para Servidor Supermicro SSD-DM128-SMCMVN1, 128GB, SATA III, mSATA, 6Gbit/s', 4399, 'discos duros', 10],
    [56, "SSD para Servidor Lenovo Thinksystem S4500, 480GB, SATA III, 3.5'', 7mm", 3269, 'discos duros', 3],
    [57, "SSD Adata Ultimate SU800, 256GB, SATA III, 2.5'', 7mm", 889, 'discos duros', 15],
    [58, "SSD para Servidor Lenovo Thinksystem S4510, 480GB, SATA III, 2.5'', 7mm", 3679, 'discos duros', 16],
    [59, 'SSD Samsung 860 EVO, 1TB, SATA III, M.2', 5539, 'discos duros', 10],
    [60, 'Kit Memoria RAM Corsair Dominator Platinum DDR4, 3200MHz, 16GB (2x 8GB), Non-ECC, CL16, XMP', 2519, 'memorias usb', 10],
    [61, 'Kit Memoria RAM Corsair Vengeance LPX DDR4, 2400MHz, 32GB, Non-ECC, CL16', 5209, 'memorias usb', 5],
    [62, "Makena Smart TV LED 32S2 32'', HD, Widescreen, Gris", 2899, 'pantallas', 6],
    [63, 'Seiki TV LED SC-39HS950N 38.5, HD, Widescreen, Negro', 3369, 'pantallas', 146],
    [64, 'Samsung TV LED LH43QMREBGCXGO 43, 4K Ultra HD, Widescreen, Negro', 12029, 'pantallas', 71],
    [65, 'Samsung Smart TV LED UN70RU7100FXZX 70, 4K Ultra HD, Widescreen, Negro', 21079, 'pantallas', 7],
    [66, 'TCL Smart TV LED 55S425 54.6, 4K Ultra HD, Widescreen, Negro', 8049, 'pantallas', 188],
    [67, 'TV Monitor LED 24TL520S-PU 24, HD, Widescreen, HDMI, Negro', 3229, 'pantallas', 411],
    [68, "Makena Smart TV LED 40S2 40'', Full HD, Widescreen, Negro", 4229, 'pantallas', 239],
    [69, 'Hisense Smart TV LED 40H5500F 39.5, Full HD, Widescreen, Negro', 5359, 'pantallas', 94],
    [70, 'Samsung Smart TV LED 43, Full HD, Widescreen, Negro', 7679, 'pantallas', 10],
    [71, 'Samsung Smart TV LED UN32J4290AF 32, HD, Widescreen, Negro', 4829, 'pantallas', 3],
    [72, 'Hisense Smart TV LED 50H8F 49.5, 4K Ultra HD, Widescreen, Negro', 9759, 'pantallas', 11],
    [73, 'Samsung Smart TV LED UN55TU7000FXZX 55, 4K Ultra HD, Widescreen, Negro/Gris', 10559, 'pantallas', 4],
    [74, 'Logitech Bocinas para Computadora con Subwoofer G560, Bluetooth, Inalámbrico, 2.1, 120W RMS, USB, negro', 4239, 'bocinas', 1],
    [75, 'Lenovo Barra de Sonido, Alámbrico, 2.5W, USB, Negro', 441, 'bocinas', 11],
    [76, 'Acteck Bocina con Subwoofer AXF-290, Bluetooth, Inalámbrico, 2.1, 18W RMS, 180W PMPO, USB, Negro', 589, 'bocinas', 18],
    [77, 'Verbatim Bocina Portátil Mini, Bluetooth, Inalámbrico, 3W RMS, USB, Blanco', 178, 'bocinas', 1],
    [78, 'Ghia Bocina Portátil BX300, Bluetooth, Inalámbrico, 40W RMS, USB, Rojo - Resistente al Agua', 769, 'bocinas', 2],
    [79, 'Naceb Bocina Portátil NA-0301, Bluetooth, Inalámbrico, USB 2.0, Rojo', 709, 'bocinas', 31],
    [80, 'Ghia Bocina Portátil BX800, Bluetooth, Inalámbrico, 2.1 Canales, 31W, USB, Negro', 1359, 'bocinas', 15],
    [81, 'Ghia Bocina Portátil BX900, Bluetooth, Inalámbrico, 2.1 Canales, 34W, USB, Negro - Resistente al Agua', 1169, 'bocinas', 20],
    [82, 'Ghia Bocina Portátil BX400, Bluetooth, Inalámbrico, 8W RMS, USB, Negro', 549, 'bocinas', 31],
    [83, 'Ghia Bocina Portátil BX500, Bluetooth, Inalámbrico, 10W RMS, USB, Gris', 499, 'bocinas', 16],
    [84, 'Logitech Audífonos Gamer G332, Alámbrico, 2 Metros, 3.5mm, Negro/Rojo', 1089, 'audifonos', 83],
    [85, 'Logitech Audífonos Gamer G635 7.1, Alámbrico, 1.5 Metros, 3.5mm, Negro/Azul', 2159, 'audifonos', 39],
    [86, 'ASUS Audífonos Gamer ROG Theta 7.1, Alámbrico, USB C, Negro', 8359, 'audifonos', 20],
    [87, 'Acer Audífonos Gamer Galea 300, Alámbrico, 3.5mm, Negro', 1719, 'audifonos', 8],
    [88, 'Audífonos Gamer Balam Rush Orphix RGB 7.1, Alámbrico, USB, Negro', 909, 'audifonos', 15],
    [89, 'Cougar Audífonos Gamer Phontum Essential, Alámbrico, 1.9 Metros, 3.5mm, Negro.', 859, 'audifonos', 4],
    [90, 'Energy Sistem Audífonos con Micrófono Headphones 1, Bluetooh, Inalámbrico, Negro/Grafito', 539, 'audifonos', 1],
    [91, 'Genius GHP-400S Audífonos, Alámbrico, 1.5 Metros, Rosa', 137, 'audifonos', 16],
    [92, 'Getttech Audífonos con Micrófono Sonority, Alámbrico, 1.2 Metros, 3.5mm, Negro/Rosa', 149, 'audifonos', 232],
    [93, 'Ginga Audífonos con Micrófono GI18ADJ01BT-RO, Bluetooth, Alámbrico/Inalámbrico, 3.5mm, Rojo', 160, 'audifonos', 139],
    [94, 'HyperX Audífonos Gamer Cloud Flight para PC/PS4/PS4 Pro, Inalámbrico, USB, 3.5mm, Negro', 2869, 'audifonos', 12],
    [95, 'Iogear Audífonos Gamer GHG601, Alámbrico, 1.2 Metros, 3.5mm, Negro', 999, 'audifonos', 2],
    [96, 'Klip Xtreme Audífonos Blast, Bluetooth, Inalámbrico, Negro/Verde', 769, 'audifonos', 2]
]

lifestore_sales = [
    [1, 1, 5, '24/07/2020', 0],
    [2, 1, 5, '27/07/2020', 0],
    [3, 2, 5, '24/02/2020', 0],
    [4, 2, 5, '22/05/2020', 0],
    [5, 2, 5, '01/01/2020', 0],
    [6, 2, 5, '24/04/2020', 0],
    [7, 2, 4, '31/01/2020', 0],
    [8, 2, 4, '07/02/2020', 0],
    [9, 2, 4, '02/03/2020', 0],
    [10, 2, 4, '07/03/2020', 0],
    [11, 2, 4, '24/03/2020', 0],
    [12, 2, 4, '24/04/2020', 0],
    [13, 2, 4, '02/05/2020', 0],
    [14, 2, 4, '03/06/2020', 0],
    [15, 2, 3, '10/11/2019', 1],
    [16, 3, 5, '21/07/2020', 0],
    [17, 3, 4, '21/07/2020', 0],
    [18, 3, 5, '11/06/2020', 0],
    [19, 3, 5, '11/06/2020', 0],
    [20, 3, 5, '20/05/2020', 0],
    [21, 3, 5, '15/05/2020', 0],
    [22, 3, 5, '02/05/2020', 0],
    [23, 3, 5, '30/04/2020', 0],
    [24, 3, 5, '27/04/2020', 0],
    [25, 3, 4, '22/04/2020', 0],
    [26, 3, 5, '19/04/2020', 0],
    [27, 3, 5, '16/04/2020', 0],
    [28, 3, 3, '14/04/2020', 0],
    [29, 3, 5, '14/04/2020', 0],
    [30, 3, 5, '14/04/2020', 0],
    [31, 3, 5, '13/04/2020', 0],
    [32, 3, 5, '13/04/2020', 0],
    [33, 3, 5, '06/04/2020', 0],
    [34, 3, 5, '02/04/2020', 0],
    [35, 3, 5, '01/04/2020', 0],
    [36, 3, 5, '16/03/2020', 0],
    [37, 3, 5, '11/03/2020', 0],
    [38, 3, 4, '10/03/2020', 0],
    [39, 3, 5, '02/03/2020', 0],
    [40, 3, 5, '27/02/2020', 0],
    [41, 3, 4, '27/02/2020', 0],
    [42, 3, 5, '03/02/2020', 0],
    [43, 3, 5, '31/01/2020', 0],
    [44, 3, 5, '30/01/2020', 0],
    [45, 3, 5, '28/01/2020', 0],
    [46, 3, 5, '25/01/2020', 0],
    [47, 3, 5, '19/01/2020', 0],
    [48, 3, 5, '13/01/2020', 0],
    [49, 3, 5, '11/01/2020', 0],
    [50, 3, 4, '09/01/2020', 0],
    [51, 3, 5, '08/01/2020', 0],
    [52, 3, 4, '06/01/2020', 0],
    [53, 3, 5, '04/01/2020', 0],
    [54, 3, 5, '04/01/2020', 0],
    [55, 3, 5, '03/01/2020', 0],
    [56, 3, 5, '02/01/2020', 0],
    [57, 3, 5, '01/01/2020', 0],
    [58, 4, 4, '19/06/2020', 0],
    [59, 4, 4, '04/06/2020', 0],
    [60, 4, 5, '16/04/2020', 0],
    [61, 4, 4, '07/04/2020', 0],
    [62, 4, 5, '06/04/2020', 0],
    [63, 4, 5, '06/04/2020', 0],
    [64, 4, 5, '30/03/2020', 0],
    [65, 4, 4, '08/03/2020', 0],
    [66, 4, 5, '25/02/2020', 0],
    [67, 4, 3, '29/01/2020', 0],
    [68, 4, 5, '23/01/2020', 0],
    [69, 4, 4, '11/01/2020', 0],
    [70, 4, 5, '09/01/2020', 0],
    [71, 5, 4, '03/07/2020', 0],
    [72, 5, 4, '14/05/2020', 0],
    [73, 5, 4, '05/05/2020', 0],
    [74, 5, 5, '04/05/2020', 0],
    [75, 5, 4, '04/05/2020', 0],
    [76, 5, 5, '03/05/2020', 0],
    [77, 5, 5, '26/04/2020', 0],
    [78, 5, 5, '23/04/2020', 0],
    [79, 5, 5, '17/04/2020', 0],
    [80, 5, 5, '13/04/2020', 0],
    [81, 5, 5, '06/04/2020', 0],
    [82, 5, 5, '26/04/2020', 0],
    [83, 5, 5, '24/03/2020', 0],
    [84, 5, 5, '22/03/2020', 0],
    [85, 5, 4, '10/03/2020', 0],
    [86, 5, 5, '25/02/2020', 0],
    [87, 5, 4, '24/02/2020', 0],
    [88, 5, 5, '15/02/2020', 0],
    [89, 5, 5, '30/01/2020', 0],
    [90, 5, 5, '17/01/2020', 0],
    [91, 6, 5, '05/05/2020', 0],
    [92, 6, 5, '22/03/2020', 0],
    [93, 6, 5, '04/02/2020', 0],
    [94, 7, 5, '25/07/2020', 0],
    [95, 7, 5, '17/06/2020', 0],
    [96, 7, 5, '15/04/2020', 0],
    [97, 7, 5, '03/04/2020', 0],
    [98, 7, 5, '31/03/2020', 0],
    [99, 7, 5, '28/03/2020', 0],
    [100, 7, 5, '22/02/2020', 0],
    [101, 8, 5, '20/04/2020', 0],
    [102, 8, 5, '16/02/2020', 0],
    [103, 8, 5, '27/01/2020', 0],
    [104, 8, 5, '20/01/2020', 0],
    [105, 10, 4, '14/05/2020', 0],
    [106, 11, 5, '30/06/2020', 0],
    [107, 11, 5, '02/04/2020', 0],
    [108, 11, 5, '05/03/2020', 0],
    [109, 12, 5, '05/05/2020', 0],
    [110, 12, 4, '09/04/2020', 0],
    [111, 12, 5, '09/04/2020', 0],
    [112, 12, 5, '02/04/2020', 0],
    [113, 12, 5, '25/03/2020', 0],
    [114, 12, 5, '24/03/2020', 0],
    [115, 12, 5, '06/03/2020', 0],
    [116, 12, 5, '04/03/2020', 0],
    [117, 12, 4, '27/02/2020', 0],
    [118, 13, 4, '17/04/2020', 0],
    [119, 17, 1, '05/09/2020', 1],
    [120, 18, 5, '30/06/2020', 0],
    [121, 18, 4, '14/03/2020', 0],
    [122, 18, 5, '27/02/2020', 0],
    [123, 18, 4, '02/02/2020', 0],
    [124, 18, 4, '01/02/2020', 0],
    [125, 21, 5, '14/04/2020', 0],
    [126, 21, 5, '12/02/2020', 0],
    [127, 22, 5, '20/04/2020', 0],
    [128, 25, 5, '28/03/2020', 0],
    [129, 25, 5, '20/03/2020', 0],
    [130, 28, 5, '30/03/2020', 0],
    [131, 29, 4, '04/05/2020', 0],
    [132, 29, 5, '24/04/2020', 0],
    [133, 29, 4, '24/04/2020', 0],
    [134, 29, 4, '17/04/2020', 0],
    [135, 29, 5, '04/04/2020', 0],
    [136, 29, 5, '09/03/2020', 0],
    [137, 29, 5, '07/03/2020', 0],
    [138, 29, 5, '26/02/2020', 0],
    [139, 29, 5, '09/02/2020', 0],
    [140, 29, 5, '06/02/2020', 0],
    [141, 29, 5, '26/01/2020', 0],
    [142, 29, 4, '25/01/2020', 0],
    [143, 29, 1, '13/01/2020', 1],
    [144, 29, 1, '10/01/2020', 0],
    [145, 31, 1, '02/05/2020', 1],
    [146, 31, 1, '02/05/2020', 1],
    [147, 31, 1, '01/04/2020', 1],
    [148, 31, 4, '20/03/2020', 0],
    [149, 31, 3, '14/03/2020', 0],
    [150, 31, 1, '11/01/2020', 0],
    [151, 33, 5, '20/03/2020', 0],
    [152, 33, 4, '27/02/2020', 0],
    [153, 40, 5, '24/05/2020', 0],
    [154, 42, 5, '27/07/2020', 0],
    [155, 42, 5, '04/05/2020', 0],
    [156, 42, 4, '04/05/2020', 0],
    [157, 42, 4, '04/05/2020', 0],
    [158, 42, 5, '04/05/2020', 0],
    [159, 42, 5, '27/04/2020', 0],
    [160, 42, 5, '26/04/2020', 0],
    [161, 42, 4, '19/04/2020', 0],
    [162, 42, 5, '14/04/2020', 0],
    [163, 42, 5, '09/04/2020', 0],
    [164, 42, 4, '05/04/2020', 0],
    [165, 42, 4, '21/03/2020', 0],
    [166, 42, 5, '09/03/2020', 0],
    [167, 42, 5, '09/03/2020', 0],
    [168, 42, 5, '03/03/2020', 0],
    [169, 42, 4, '23/02/2020', 0],
    [170, 42, 4, '03/02/2020', 0],
    [171, 42, 4, '09/01/2020', 0],
    [172, 44, 5, '16/04/2020', 0],
    [173, 44, 5, '11/04/2020', 0],
    [174, 44, 5, '21/03/2020', 0],
    [175, 44, 4, '02/03/2020', 0],
    [176, 44, 4, '01/03/2020', 0],
    [177, 44, 5, '05/01/2020', 0],
    [178, 45, 1, '11/02/2020', 1],
    [179, 46, 2, '07/03/2020', 1],
    [180, 47, 4, '02/07/2020', 0],
    [181, 47, 5, '10/06/2020', 0],
    [182, 47, 5, '18/04/2020', 0],
    [183, 47, 4, '16/04/2020', 0],
    [184, 47, 5, '08/04/2020', 0],
    [185, 47, 4, '07/04/2020', 0],
    [186, 47, 5, '23/03/2020', 0],
    [187, 47, 5, '10/03/2020', 0],
    [188, 47, 3, '11/02/2020', 0],
    [189, 47, 5, '18/01/2020', 0],
    [190, 47, 5, '17/01/2020', 0],
    [191, 48, 4, '02/08/2020', 0],
    [192, 48, 3, '27/04/2020', 0],
    [193, 48, 5, '25/04/2020', 0],
    [194, 48, 5, '23/04/2020', 0],
    [195, 48, 5, '22/02/2020', 0],
    [196, 48, 5, '10/02/2020', 0],
    [197, 48, 5, '14/01/2020', 0],
    [198, 48, 5, '09/01/2020', 0],
    [199, 48, 5, '09/01/2020', 0],
    [200, 49, 5, '06/04/2020', 0],
    [201, 49, 5, '19/04/2020', 0],
    [202, 49, 5, '22/04/2020', 0],
    [203, 50, 5, '04/05/2020', 0],
    [204, 51, 5, '23/03/2020', 0],
    [205, 51, 4, '04/02/2020', 0],
    [206, 51, 5, '03/01/2020', 0],
    [207, 52, 5, '19/03/2020', 0],
    [208, 52, 5, '02/01/2020', 0],
    [209, 54, 4, '03/08/2020', 0],
    [210, 54, 5, '02/08/2020', 0],
    [211, 54, 5, '04/07/2020', 0],
    [212, 54, 5, '01/07/2020', 0],
    [213, 54, 5, '03/06/2020', 0],
    [214, 54, 5, '23/05/2020', 0],
    [215, 54, 4, '15/05/2020', 0],
    [216, 54, 5, '11/05/2020', 0],
    [217, 54, 5, '08/05/2020', 0],
    [218, 54, 5, '04/05/2020', 0],
    [219, 54, 4, '04/05/2002', 0],
    [220, 54, 5, '04/05/2020', 0],
    [221, 54, 5, '04/05/2020', 0],
    [222, 54, 4, '30/04/2020', 0],
    [223, 54, 4, '24/04/2020', 0],
    [224, 54, 5, '23/04/2020', 0],
    [225, 54, 4, '17/04/2020', 0],
    [226, 54, 5, '15/04/2020', 0],
    [227, 54, 5, '14/04/2020', 0],
    [228, 54, 4, '14/04/2020', 0],
    [229, 54, 5, '13/04/2020', 0],
    [230, 54, 5, '13/04/2020', 0],
    [231, 54, 5, '13/04/2020', 0],
    [232, 54, 5, '09/04/2020', 0],
    [233, 54, 5, '03/04/2020', 0],
    [234, 54, 5, '03/04/2020', 0],
    [235, 54, 5, '30/03/2020', 0],
    [236, 54, 5, '26/03/2020', 0],
    [237, 54, 5, '20/03/2020', 0],
    [238, 54, 2, '19/03/2020', 1],
    [239, 54, 5, '17/03/2020', 0],
    [240, 54, 5, '14/03/2020', 0],
    [241, 54, 5, '13/03/2020', 0],
    [242, 54, 4, '02/03/2020', 0],
    [243, 54, 5, '01/03/2020', 0],
    [244, 54, 5, '25/02/2020', 0],
    [245, 54, 5, '20/02/2020', 0],
    [246, 54, 4, '17/02/2020', 0],
    [247, 54, 5, '14/02/2020', 0],
    [248, 54, 5, '12/02/2020', 0],
    [249, 54, 4, '10/02/2020', 0],
    [250, 54, 5, '07/02/2020', 0],
    [251, 54, 5, '31/01/2020', 0],
    [252, 54, 5, '30/01/2020', 0],
    [253, 54, 5, '29/01/2020', 0],
    [254, 54, 5, '27/01/2020', 0],
    [255, 54, 5, '25/01/2020', 0],
    [256, 54, 5, '23/01/2020', 0],
    [257, 54, 5, '23/01/2020', 0],
    [258, 54, 4, '22/01/2020', 0],
    [259, 57, 5, '05/07/2020', 0],
    [260, 57, 5, '23/05/2020', 0],
    [261, 57, 5, '23/05/2020', 0],
    [262, 57, 5, '01/05/2020', 0],
    [263, 57, 5, '06/04/2020', 0],
    [264, 57, 5, '09/03/2020', 0],
    [265, 57, 5, '25/02/2020', 0],
    [266, 57, 5, '10/02/2020', 0],
    [267, 57, 4, '04/02/2020', 0],
    [268, 57, 5, '04/02/2020', 0],
    [269, 57, 5, '28/01/2020', 0],
    [270, 57, 5, '27/01/2020', 0],
    [271, 57, 4, '22/01/2020', 0],
    [272, 57, 5, '08/01/2020', 0],
    [273, 57, 5, '07/01/2020', 0],
    [274, 60, 5, '17/06/2020', 0],
    [275, 66, 5, '06/05/2020', 0],
    [276, 67, 5, '24/04/2020', 0],
    [277, 74, 4, '12/02/2020', 0],
    [278, 74, 5, '18/02/2020', 0],
    [279, 84, 5, '05/05/2020', 0],
    [280, 85, 5, '05/05/2020', 0],
    [281, 85, 5, '28/04/2020', 0],
    [282, 89, 3, '06/01/2020', 0],
    [283, 94, 4, '10/04/2020', 0]
]

lifestore_searches = [
    [1, 1],
    [2, 1],
    [3, 1],
    [4, 1],
    [5, 1],
    [6, 1],
    [7, 1],
    [8, 1],
    [9, 1],
    [10, 1],
    [11, 2],
    [12, 2],
    [13, 2],
    [14, 2],
    [15, 2],
    [16, 2],
    [17, 2],
    [18, 2],
    [19, 2],
    [20, 2],
    [21, 2],
    [22, 2],
    [23, 2],
    [24, 2],
    [25, 2],
    [26, 2],
    [27, 2],
    [28, 2],
    [29, 2],
    [30, 2],
    [31, 2],
    [32, 2],
    [33, 2],
    [34, 2],
    [35, 3],
    [36, 3],
    [37, 3],
    [38, 3],
    [39, 3],
    [40, 3],
    [41, 3],
    [42, 3],
    [43, 3],
    [44, 3],
    [45, 3],
    [46, 3],
    [47, 3],
    [48, 3],
    [49, 3],
    [50, 3],
    [51, 3],
    [52, 3],
    [53, 3],
    [54, 3],
    [55, 3],
    [56, 3],
    [57, 3],
    [58, 3],
    [59, 3],
    [60, 3],
    [61, 3],
    [62, 3],
    [63, 3],
    [64, 3],
    [65, 3],
    [66, 3],
    [67, 3],
    [68, 3],
    [69, 3],
    [70, 3],
    [71, 3],
    [72, 3],
    [73, 3],
    [74, 3],
    [75, 3],
    [76, 3],
    [77, 3],
    [78, 3],
    [79, 3],
    [80, 3],
    [81, 3],
    [82, 3],
    [83, 3],
    [84, 3],
    [85, 3],
    [86, 3],
    [87, 3],
    [88, 3],
    [89, 3],
    [90, 4],
    [91, 4],
    [92, 4],
    [93, 4],
    [94, 4],
    [95, 4],
    [96, 4],
    [97, 4],
    [98, 4],
    [99, 4],
    [100, 4],
    [101, 4],
    [102, 4],
    [103, 4],
    [104, 4],
    [105, 4],
    [106, 4],
    [107, 4],
    [108, 4],
    [109, 4],
    [110, 4],
    [111, 4],
    [112, 4],
    [113, 4],
    [114, 4],
    [115, 4],
    [116, 4],
    [117, 4],
    [118, 4],
    [119, 4],
    [120, 4],
    [121, 4],
    [122, 4],
    [123, 4],
    [124, 4],
    [125, 4],
    [126, 4],
    [127, 4],
    [128, 4],
    [129, 4],
    [130, 4],
    [131, 5],
    [132, 5],
    [133, 5],
    [134, 5],
    [135, 5],
    [136, 5],
    [137, 5],
    [138, 5],
    [139, 5],
    [140, 5],
    [141, 5],
    [142, 5],
    [143, 5],
    [144, 5],
    [145, 5],
    [146, 5],
    [147, 5],
    [148, 5],
    [149, 5],
    [150, 5],
    [151, 5],
    [152, 5],
    [153, 5],
    [154, 5],
    [155, 5],
    [156, 5],
    [157, 5],
    [158, 5],
    [159, 5],
    [160, 5],
    [161, 6],
    [162, 6],
    [163, 6],
    [164, 6],
    [165, 6],
    [166, 6],
    [167, 6],
    [168, 6],
    [169, 6],
    [170, 6],
    [171, 7],
    [172, 7],
    [173, 7],
    [174, 7],
    [175, 7],
    [176, 7],
    [177, 7],
    [178, 7],
    [179, 7],
    [180, 7],
    [181, 7],
    [182, 7],
    [183, 7],
    [184, 7],
    [185, 7],
    [186, 7],
    [187, 7],
    [188, 7],
    [189, 7],
    [190, 7],
    [191, 7],
    [192, 7],
    [193, 7],
    [194, 7],
    [195, 7],
    [196, 7],
    [197, 7],
    [198, 7],
    [199, 7],
    [200, 7],
    [201, 7],
    [202, 8],
    [203, 8],
    [204, 8],
    [205, 8],
    [206, 8],
    [207, 8],
    [208, 8],
    [209, 8],
    [210, 8],
    [211, 8],
    [212, 8],
    [213, 8],
    [214, 8],
    [215, 8],
    [216, 8],
    [217, 8],
    [218, 8],
    [219, 8],
    [220, 8],
    [221, 8],
    [222, 9],
    [223, 10],
    [224, 11],
    [225, 11],
    [226, 11],
    [227, 11],
    [228, 11],
    [229, 12],
    [230, 12],
    [231, 12],
    [232, 12],
    [233, 12],
    [234, 12],
    [235, 12],
    [236, 12],
    [237, 12],
    [238, 12],
    [239, 12],
    [240, 12],
    [241, 12],
    [242, 12],
    [243, 12],
    [244, 13],
    [245, 13],
    [246, 15],
    [247, 15],
    [248, 15],
    [249, 15],
    [250, 17],
    [251, 17],
    [252, 17],
    [253, 18],
    [254, 18],
    [255, 18],
    [256, 18],
    [257, 18],
    [258, 18],
    [259, 18],
    [260, 18],
    [261, 18],
    [262, 18],
    [263, 18],
    [264, 21],
    [265, 21],
    [266, 21],
    [267, 21],
    [268, 21],
    [269, 21],
    [270, 21],
    [271, 21],
    [272, 21],
    [273, 21],
    [274, 21],
    [275, 21],
    [276, 21],
    [277, 21],
    [278, 21],
    [279, 22],
    [280, 22],
    [281, 22],
    [282, 22],
    [283, 22],
    [284, 25],
    [285, 25],
    [286, 25],
    [287, 25],
    [288, 25],
    [289, 25],
    [290, 25],
    [291, 25],
    [292, 25],
    [293, 25],
    [294, 26],
    [295, 26],
    [296, 26],
    [297, 26],
    [298, 26],
    [299, 27],
    [300, 28],
    [301, 28],
    [302, 28],
    [303, 28],
    [304, 28],
    [305, 29],
    [306, 29],
    [307, 29],
    [308, 29],
    [309, 29],
    [310, 29],
    [311, 29],
    [312, 29],
    [313, 29],
    [314, 29],
    [315, 29],
    [316, 29],
    [317, 29],
    [318, 29],
    [319, 29],
    [320, 29],
    [321, 29],
    [322, 29],
    [323, 29],
    [324, 29],
    [325, 29],
    [326, 29],
    [327, 29],
    [328, 29],
    [329, 29],
    [330, 29],
    [331, 29],
    [332, 29],
    [333, 29],
    [334, 29],
    [335, 29],
    [336, 29],
    [337, 29],
    [338, 29],
    [339, 29],
    [340, 29],
    [341, 29],
    [342, 29],
    [343, 29],
    [344, 29],
    [345, 29],
    [346, 29],
    [347, 29],
    [348, 29],
    [349, 29],
    [350, 29],
    [351, 29],
    [352, 29],
    [353, 29],
    [354, 29],
    [355, 29],
    [356, 29],
    [357, 29],
    [358, 29],
    [359, 29],
    [360, 29],
    [361, 29],
    [362, 29],
    [363, 29],
    [364, 29],
    [365, 31],
    [366, 31],
    [367, 31],
    [368, 31],
    [369, 31],
    [370, 31],
    [371, 31],
    [372, 31],
    [373, 31],
    [374, 31],
    [375, 35],
    [376, 39],
    [377, 39],
    [378, 39],
    [379, 40],
    [380, 40],
    [381, 40],
    [382, 40],
    [383, 40],
    [384, 40],
    [385, 40],
    [386, 40],
    [387, 40],
    [388, 40],
    [389, 42],
    [390, 42],
    [391, 42],
    [392, 42],
    [393, 42],
    [394, 42],
    [395, 42],
    [396, 42],
    [397, 42],
    [398, 42],
    [399, 42],
    [400, 42],
    [401, 42],
    [402, 42],
    [403, 42],
    [404, 42],
    [405, 42],
    [406, 42],
    [407, 42],
    [408, 42],
    [409, 42],
    [410, 42],
    [411, 42],
    [412, 44],
    [413, 44],
    [414, 44],
    [415, 44],
    [416, 44],
    [417, 44],
    [418, 44],
    [419, 44],
    [420, 44],
    [421, 44],
    [422, 44],
    [423, 44],
    [424, 44],
    [425, 44],
    [426, 44],
    [427, 44],
    [428, 44],
    [429, 44],
    [430, 44],
    [431, 44],
    [432, 44],
    [433, 44],
    [434, 44],
    [435, 44],
    [436, 44],
    [437, 45],
    [438, 46],
    [439, 46],
    [440, 46],
    [441, 46],
    [442, 47],
    [443, 47],
    [444, 47],
    [445, 47],
    [446, 47],
    [447, 47],
    [448, 47],
    [449, 47],
    [450, 47],
    [451, 47],
    [452, 47],
    [453, 47],
    [454, 47],
    [455, 47],
    [456, 47],
    [457, 47],
    [458, 47],
    [459, 47],
    [460, 47],
    [461, 47],
    [462, 47],
    [463, 47],
    [464, 47],
    [465, 47],
    [466, 47],
    [467, 47],
    [468, 47],
    [469, 47],
    [470, 47],
    [471, 47],
    [472, 48],
    [473, 48],
    [474, 48],
    [475, 48],
    [476, 48],
    [477, 48],
    [478, 48],
    [479, 48],
    [480, 48],
    [481, 48],
    [482, 48],
    [483, 48],
    [484, 48],
    [485, 48],
    [486, 48],
    [487, 48],
    [488, 48],
    [489, 48],
    [490, 48],
    [491, 48],
    [492, 48],
    [493, 48],
    [494, 48],
    [495, 48],
    [496, 48],
    [497, 48],
    [498, 48],
    [499, 49],
    [500, 49],
    [501, 49],
    [502, 49],
    [503, 49],
    [504, 49],
    [505, 49],
    [506, 49],
    [507, 49],
    [508, 49],
    [509, 50],
    [510, 50],
    [511, 50],
    [512, 50],
    [513, 50],
    [514, 50],
    [515, 50],
    [516, 51],
    [517, 51],
    [518, 51],
    [519, 51],
    [520, 51],
    [521, 51],
    [522, 51],
    [523, 51],
    [524, 51],
    [525, 51],
    [526, 51],
    [527, 52],
    [528, 52],
    [529, 52],
    [530, 52],
    [531, 52],
    [532, 54],
    [533, 54],
    [534, 54],
    [535, 54],
    [536, 54],
    [537, 54],
    [538, 54],
    [539, 54],
    [540, 54],
    [541, 54],
    [542, 54],
    [543, 54],
    [544, 54],
    [545, 54],
    [546, 54],
    [547, 54],
    [548, 54],
    [549, 54],
    [550, 54],
    [551, 54],
    [552, 54],
    [553, 54],
    [554, 54],
    [555, 54],
    [556, 54],
    [557, 54],
    [558, 54],
    [559, 54],
    [560, 54],
    [561, 54],
    [562, 54],
    [563, 54],
    [564, 54],
    [565, 54],
    [566, 54],
    [567, 54],
    [568, 54],
    [569, 54],
    [570, 54],
    [571, 54],
    [572, 54],
    [573, 54],
    [574, 54],
    [575, 54],
    [576, 54],
    [577, 54],
    [578, 54],
    [579, 54],
    [580, 54],
    [581, 54],
    [582, 54],
    [583, 54],
    [584, 54],
    [585, 54],
    [586, 54],
    [587, 54],
    [588, 54],
    [589, 54],
    [590, 54],
    [591, 54],
    [592, 54],
    [593, 54],
    [594, 54],
    [595, 54],
    [596, 54],
    [597, 54],
    [598, 54],
    [599, 54],
    [600, 54],
    [601, 54],
    [602, 54],
    [603, 54],
    [604, 54],
    [605, 54],
    [606, 54],
    [607, 54],
    [608, 54],
    [609, 54],
    [610, 54],
    [611, 54],
    [612, 54],
    [613, 54],
    [614, 54],
    [615, 54],
    [616, 54],
    [617, 54],
    [618, 54],
    [619, 54],
    [620, 54],
    [621, 54],
    [622, 54],
    [623, 54],
    [624, 54],
    [625, 54],
    [626, 54],
    [627, 54],
    [628, 54],
    [629, 54],
    [630, 54],
    [631, 54],
    [632, 54],
    [633, 54],
    [634, 54],
    [635, 54],
    [636, 54],
    [637, 54],
    [638, 54],
    [639, 54],
    [640, 54],
    [641, 54],
    [642, 54],
    [643, 54],
    [644, 54],
    [645, 54],
    [646, 54],
    [647, 54],
    [648, 54],
    [649, 54],
    [650, 54],
    [651, 54],
    [652, 54],
    [653, 54],
    [654, 54],
    [655, 54],
    [656, 54],
    [657, 54],
    [658, 54],
    [659, 54],
    [660, 54],
    [661, 54],
    [662, 54],
    [663, 54],
    [664, 54],
    [665, 54],
    [666, 54],
    [667, 54],
    [668, 54],
    [669, 54],
    [670, 54],
    [671, 54],
    [672, 54],
    [673, 54],
    [674, 54],
    [675, 54],
    [676, 54],
    [677, 54],
    [678, 54],
    [679, 54],
    [680, 54],
    [681, 54],
    [682, 54],
    [683, 54],
    [684, 54],
    [685, 54],
    [686, 54],
    [687, 54],
    [688, 54],
    [689, 54],
    [690, 54],
    [691, 54],
    [692, 54],
    [693, 54],
    [694, 54],
    [695, 54],
    [696, 54],
    [697, 54],
    [698, 54],
    [699, 54],
    [700, 54],
    [701, 54],
    [702, 54],
    [703, 54],
    [704, 54],
    [705, 54],
    [706, 54],
    [707, 54],
    [708, 54],
    [709, 54],
    [710, 54],
    [711, 54],
    [712, 54],
    [713, 54],
    [714, 54],
    [715, 54],
    [716, 54],
    [717, 54],
    [718, 54],
    [719, 54],
    [720, 54],
    [721, 54],
    [722, 54],
    [723, 54],
    [724, 54],
    [725, 54],
    [726, 54],
    [727, 54],
    [728, 54],
    [729, 54],
    [730, 54],
    [731, 54],
    [732, 54],
    [733, 54],
    [734, 54],
    [735, 54],
    [736, 54],
    [737, 54],
    [738, 54],
    [739, 54],
    [740, 54],
    [741, 54],
    [742, 54],
    [743, 54],
    [744, 54],
    [745, 54],
    [746, 54],
    [747, 54],
    [748, 54],
    [749, 54],
    [750, 54],
    [751, 54],
    [752, 54],
    [753, 54],
    [754, 54],
    [755, 54],
    [756, 54],
    [757, 54],
    [758, 54],
    [759, 54],
    [760, 54],
    [761, 54],
    [762, 54],
    [763, 54],
    [764, 54],
    [765, 54],
    [766, 54],
    [767, 54],
    [768, 54],
    [769, 54],
    [770, 54],
    [771, 54],
    [772, 54],
    [773, 54],
    [774, 54],
    [775, 54],
    [776, 54],
    [777, 54],
    [778, 54],
    [779, 54],
    [780, 54],
    [781, 54],
    [782, 54],
    [783, 54],
    [784, 54],
    [785, 54],
    [786, 54],
    [787, 54],
    [788, 54],
    [789, 54],
    [790, 54],
    [791, 54],
    [792, 54],
    [793, 54],
    [794, 54],
    [795, 56],
    [796, 56],
    [797, 57],
    [798, 57],
    [799, 57],
    [800, 57],
    [801, 57],
    [802, 57],
    [803, 57],
    [804, 57],
    [805, 57],
    [806, 57],
    [807, 57],
    [808, 57],
    [809, 57],
    [810, 57],
    [811, 57],
    [812, 57],
    [813, 57],
    [814, 57],
    [815, 57],
    [816, 57],
    [817, 57],
    [818, 57],
    [819, 57],
    [820, 57],
    [821, 57],
    [822, 57],
    [823, 57],
    [824, 57],
    [825, 57],
    [826, 57],
    [827, 57],
    [828, 57],
    [829, 57],
    [830, 57],
    [831, 57],
    [832, 57],
    [833, 57],
    [834, 57],
    [835, 57],
    [836, 57],
    [837, 57],
    [838, 57],
    [839, 57],
    [840, 57],
    [841, 57],
    [842, 57],
    [843, 57],
    [844, 57],
    [845, 57],
    [846, 57],
    [847, 57],
    [848, 57],
    [849, 57],
    [850, 57],
    [851, 57],
    [852, 57],
    [853, 57],
    [854, 57],
    [855, 57],
    [856, 57],
    [857, 57],
    [858, 57],
    [859, 57],
    [860, 57],
    [861, 57],
    [862, 57],
    [863, 57],
    [864, 57],
    [865, 57],
    [866, 57],
    [867, 57],
    [868, 57],
    [869, 57],
    [870, 57],
    [871, 57],
    [872, 57],
    [873, 57],
    [874, 57],
    [875, 57],
    [876, 57],
    [877, 57],
    [878, 57],
    [879, 57],
    [880, 57],
    [881, 57],
    [882, 57],
    [883, 57],
    [884, 57],
    [885, 57],
    [886, 57],
    [887, 57],
    [888, 57],
    [889, 57],
    [890, 57],
    [891, 57],
    [892, 57],
    [893, 57],
    [894, 57],
    [895, 57],
    [896, 57],
    [897, 57],
    [898, 57],
    [899, 57],
    [900, 57],
    [901, 57],
    [902, 57],
    [903, 57],
    [904, 59],
    [905, 63],
    [906, 63],
    [907, 63],
    [908, 63],
    [909, 66],
    [910, 66],
    [911, 66],
    [912, 66],
    [913, 66],
    [914, 66],
    [915, 66],
    [916, 66],
    [917, 66],
    [918, 66],
    [919, 66],
    [920, 66],
    [921, 66],
    [922, 66],
    [923, 66],
    [924, 67],
    [925, 67],
    [926, 67],
    [927, 67],
    [928, 67],
    [929, 67],
    [930, 67],
    [931, 67],
    [932, 67],
    [933, 67],
    [934, 67],
    [935, 67],
    [936, 67],
    [937, 67],
    [938, 67],
    [939, 67],
    [940, 67],
    [941, 67],
    [942, 67],
    [943, 67],
    [944, 67],
    [945, 67],
    [946, 67],
    [947, 67],
    [948, 67],
    [949, 67],
    [950, 67],
    [951, 67],
    [952, 67],
    [953, 67],
    [954, 67],
    [955, 67],
    [956, 70],
    [957, 73],
    [958, 73],
    [959, 73],
    [960, 73],
    [961, 74],
    [962, 74],
    [963, 74],
    [964, 74],
    [965, 74],
    [966, 74],
    [967, 76],
    [968, 76],
    [969, 80],
    [970, 84],
    [971, 84],
    [972, 84],
    [973, 84],
    [974, 84],
    [975, 84],
    [976, 84],
    [977, 84],
    [978, 84],
    [979, 84],
    [980, 85],
    [981, 85],
    [982, 85],
    [983, 85],
    [984, 85],
    [985, 85],
    [986, 85],
    [987, 85],
    [988, 85],
    [989, 85],
    [990, 85],
    [991, 85],
    [992, 85],
    [993, 85],
    [994, 85],
    [995, 85],
    [996, 85],
    [997, 85],
    [998, 85],
    [999, 85],
    [1000, 85],
    [1001, 85],
    [1002, 85],
    [1003, 85],
    [1004, 85],
    [1005, 85],
    [1006, 85],
    [1007, 85],
    [1008, 85],
    [1009, 85],
    [1010, 85],
    [1011, 85],
    [1012, 85],
    [1013, 85],
    [1014, 85],
    [1015, 89],
    [1016, 89],
    [1017, 89],
    [1018, 89],
    [1019, 89],
    [1020, 89],
    [1021, 89],
    [1022, 91],
    [1023, 91],
    [1024, 93],
    [1025, 94],
    [1026, 94],
    [1027, 94],
    [1028, 94],
    [1029, 94],
    [1030, 94],
    [1031, 95],
    [1032, 95],
    [1033, 95]
]



"Primero se va a a hacer una copia de la lista de productos, lifestore_products, la cual posteriormente va a ser modificada añadiendo datos tales como el número de ventas, lás busquedas, reseñas y devoluciones que tuvo cada producto. Esta lista posteriormente será filtrada y ordenada para cumplir cada uno de los requerimientos del proyecto."

# Primero se define la lista como una lista vacía
productos_expandidos = []

# Como la lista 'lifestore_products' es una lista de listas, se rellena la lista  'productos_expandidos' con tantas listas vacías, [], como se tengan productos
for producto in lifestore_products:
  productos_expandidos.append([])

# Se rellena la lista 'productos_expanidos iterando sobre cada elemento en productos_expandidos y sobre cada lista en lifestore_products
for i in range(len(productos_expandidos)):
  for j in range(len(lifestore_products[i])):
    productos_expandidos[i].append(lifestore_products[i][j])


''' El siguiente paso es contar cuántas veces un producto fue buscado o vendido. Para hacer esto primero se va a obtener dos listas con los id de todos los productos vendidos y buscados para luego, mediante bucles for, contar cuántas veces aparece cada producto en dichas listas'''

# Se define una lista vacía con los id de los productos comprados.
id_comprados = []

# Se rellena la lista id de los productos comprados
for venta in lifestore_sales:
  id_comprados.append(venta[1])

# Se define la lista vacía que va a contener los id de los productos buscados
id_buscados = []

# Se rellena la lista
for venta in lifestore_searches:
  id_buscados.append(venta[1])

# Ahora se va a definir dos listas vacías que posteriormente se van a rellenar con el número de veces que cada producto fue comprado o buscado. Afortunadamente, los id de los productos en lifestore_products ya vienen ordenados
compras_por_producto = []
busquedas_por_producto = []

#Se rellena la lista.
# Iteramos sobre cada producto en la tienda
for producto in lifestore_products: 
  # Definimos la variable cuenta, la cual se va a modificar si el id de un producto vendido coincide con el id del producto sobre el cual está actuando el ciclo.
  cuenta_compras = 0
  # Se itera sobre los elementos de id_comprados
  for i in range(len(id_comprados)):
    if producto[0] == id_comprados[i]:
      # Si hay una coincidencia, la cuenta aumenta en 1
      cuenta_compras += 1
  # Se añade la cuenta final a la lista compras_por_producto    
  compras_por_producto.append(cuenta_compras)  

  # Se realiza el mismo procedimiento pero para los productos buscados
  cuenta_busquedas = 0
  for i in range(len(id_buscados)):
    if producto[0] == id_buscados[i]:
      cuenta_busquedas += 1
  busquedas_por_producto.append(cuenta_busquedas)

'''Ahora se va a revisar cuántas reseñas de 1,2,3,4 y 5 estrellas tuvo cada producto, cuál es la calificación promedio de cada producto y cuántas veces cada producto fue devuelto'''

calificaciones_por_producto = []

# La lista de calificaciones por producto va a ser una lista de listas, donde cada elemento va a tener 5 entradas. [score = 5, score = 4, score = 3, score = 2, score = 1]

# Se rellena la lista calificaciones_por_producto al inicio con puros ceros. En caso de que un producto haya recibido una calificación de 1,2,...,5 se sumará un 1 al elemento de la lista correspondiente
for producto in lifestore_products:
  calificaciones_por_producto.append([0,0,0,0,0])

# Se definen las listas vacías que van a corresponder a las calificaciones promedio y devoluciones que tuvo cada producto
calificaciones_promedio = []
devoluciones_por_producto = []

# Se va a iterar sobre cada producto en lifestore_products
for i in range(len(lifestore_products)):

  # Se inicia la cuenta del número de estrellas que recibió cada producto
  cuenta_estrellas = 0

  # Se inicia la cuenta del número de devoluciones que tuvo cada producto
  cuenta_devoluciones = 0

  # También se va a iterar sobre cada venta en lifestore_sales.
  for venta in lifestore_sales:

    # Se revisa si el id del producto en lifestore_sales coincide con el id del producto vendido
    if lifestore_products[i][0] == venta[1]:
      #Se suma el número de estrellas al conteo de estrellas
      cuenta_estrellas += venta[2]

      #Como una devolucion es igual a un 1, vasta con sumar la entrada dicho elemento en la venta a la cuenta de devoluciones.
      cuenta_devoluciones += venta[-1]

      # Se rellena la lista de calificicaciones por producto de acuerdo a la reseña que tuvo el producto.
      calificaciones_por_producto[i][-venta[2]] += 1

  # Para evitar dividir entre 0 al sacar el número de estrellas promedio, se revisa que el número de cuentas sea distinto a cero.   
  if compras_por_producto[i] != 0:
    promedio_estrellas = round(cuenta_estrellas/compras_por_producto[i],2)
    calificaciones_promedio.append(promedio_estrellas)

  # El caso de que el producto no haya tenido ventas, la cuenta de estrellas va a ser cero, por lo que el promedio también lo será. De esta forma basta con agregar el conteo de estrellas (0) a la lista de calificaciones promedio.  
  else:     
    calificaciones_promedio.append(cuenta_estrellas)

  # Se añade el número de devoluciones que tuvo cada producto a la lista de devoluciones_por_producto.  
  devoluciones_por_producto.append(cuenta_devoluciones) 

'''Como usuario y como administrador, es cómodo ver cuántas veces un producto obtuvo tantas estrellas. Para que sea más cómodo leer dichos datos, se creara una lista de listas, donde cada lista interna contendrá cadenas con el formato '#numero_estrellas: veces que se obtuvo dicha calificación'. Esto ayuda a identificar qué tan probable es que un cliente no esté satisfecho con un producto. '''

# Se define la lista vacía a rellenar con las cadenas de calificaciones que obtuvo cada producto.
calificaciones_por_producto_str = []

# Se comienza a rellenar la lista, iterando sobre la lista de calificaciones por producto.
for calificaciones in calificaciones_por_producto:
  # Se define la lista interna vacía
  lista = []
  # Se itera sobre cada lista de calificaciones en 'calificaciones'
  for i in range(len(calificaciones)):
    #Se construye la cadena que se va a anexar a 'lista'
    cadena = str(abs(i-5)) + "*: " + str(calificaciones[i])
    # Es mejor que los clientes vean cuántas veces un producto resulto muy bueno antes de que vean cuántas veces resultó ser malo.

    # Se anexa la cadena a la lista.
    lista.append(cadena)

  #Cuando termine el ciclo se anexa la lista a 'calificaciones_por_producto_str'  
  calificaciones_por_producto_str.append(lista)     


'''Una vez que ya se tienen las listas de cuántes veces un producto fue comprado, buscado, devuelto y el promedio de sus reseñas, se va a agregar cada uno de esos datos a la información de cada producto en la lista productos_expandidos. '''

# Se crea una lista que contenga todas las listas con los datos que se quiere añadir a la basew de datos de los productos.
datos_a_anadir = [busquedas_por_producto, compras_por_producto, calificaciones_promedio, calificaciones_por_producto_str, devoluciones_por_producto]

#Afortunadamente para cada lista, elemento [j] está asociado al producto [j] en la lista lifestore_products, por lo quee no es necesario reordenar las listas.
for i in range(len(productos_expandidos)):
  for datos in datos_a_anadir:
    productos_expandidos[i].append(datos[i])

'''El formato de cada elemento en la lista 'productos expandidos' es [id_product, name, price, category, stock, busquedas, compras, calificacion_promedio, calificaciones_desglosadas, devoluciones].

Ahora ya se puede proceder a ordenar datos'''
   

"------------------------------------------------------"

"ORDENACION DE LISTAS"

"------------------------------------------------------"
"COMPRAS"  
"------------------------------------------------------"

'''Primero se va a reordenar la lista expandida, productos_expandidos, de acuerdo al número de ventas que tuvo cada producto tanto en orden ascendente como descendente'''

'Primero se ordenará la lista de manera ascendente'

# Se hace una copia de la lista productos_expandidos para protegerla. Se va a usar la nueva lista creada.
copia_productos_expandidos = [x for x in productos_expandidos]

copia_productos_expandidos = []
for producto in productos_expandidos:
  copia_productos_expandidos.append(producto)

# Se define una lista vacía que posteriormente se va a rellenar con los datos ordenados
productos_expandidos_mas_comprados = []

# Se genera un ciclo while para comenzar a ordenar la lista. El ciclo se debe detener cuando la lista 'copia_productos_expandidos' ya no contenga elementos-
while copia_productos_expandidos:
  maximo = copia_productos_expandidos[0][6]
  lista = copia_productos_expandidos[0]
  for i in range(1, len(copia_productos_expandidos)):
    if maximo < copia_productos_expandidos[i][6]:
      maximo = copia_productos_expandidos[i][6]
      lista = copia_productos_expandidos[i]
  productos_expandidos_mas_comprados.append(lista)
  copia_productos_expandidos.remove(lista)


'Ahora se va a separar la lista ordenada en los que sí tienen ventas en los que no'

# Productos con al menos una venta
productos_mas_comprados_sin_ceros = []

# Productos sin ventas
productos_mas_comprados_ceros = []

for elemento in productos_expandidos_mas_comprados:
  if elemento[6] != 0:
    productos_mas_comprados_sin_ceros.append(elemento)
  else:
    productos_mas_comprados_ceros.append(elemento) 


# Se vuelve a rellenar la copia de los productos expandidos
for producto in productos_expandidos:
  copia_productos_expandidos.append(producto)

productos_expandidos_menos_comprados = []

# Se rellena la lista productos_expanidmos_menos_comprados con los datos ordenados de menor ventas a mayor ventas
# Es el mismo proceso que para ordenarlos de mayor a menor.

while copia_productos_expandidos:
  minimo = copia_productos_expandidos[0][6]
  lista = copia_productos_expandidos[0]
  for i in range(1, len(copia_productos_expandidos)):
    if minimo > copia_productos_expandidos[i][6]:
      minimo = copia_productos_expandidos[i][6]
      lista = copia_productos_expandidos[i]
  productos_expandidos_menos_comprados.append(lista)
  copia_productos_expandidos.remove(lista)

'Ahora se va a separar la lista ordenada en los que sí tienen ventas en los que no'

# Productos con al menos una venta
productos_menos_comprados_sin_ceros = []
# Productos sin ventas
productos_menos_comprados_ceros = []

for elemento in productos_expandidos_menos_comprados:
  if elemento[6] != 0:
    productos_menos_comprados_sin_ceros.append(elemento)
  else:
    productos_menos_comprados_ceros.append(elemento) 


"-------------------------------------------------------"
"BÚSQUEDAS"
"-------------------------------------------------------"

''' Ahora se va a ordenar la lista de productos expandidos de acuerdo al número de búsquedas que tuvo cada producto tanto en orden ascendente como en descendente'''

"Primero se va a ordenar la lista en orden descendente"

# Se vuelve a rellenar la copia de los productos expandidos
for producto in productos_expandidos:
  copia_productos_expandidos.append(producto)

# Se reordena la lista copia_productos_expandidos en orden descendente de acuerdo al número de búsquedas.
productos_expandidos_mas_buscados = []

while copia_productos_expandidos:
  maximo = copia_productos_expandidos[0][5]
  lista = copia_productos_expandidos[0]
  for i in range(1, len(copia_productos_expandidos)):
    if maximo < copia_productos_expandidos[i][5]:
      maximo = copia_productos_expandidos[i][5]
      lista = copia_productos_expandidos[i]
  productos_expandidos_mas_buscados.append(lista)
  copia_productos_expandidos.remove(lista)

'Ahora se va a separar la lista ordenada en los que sí tienen busquedas en los que no'

# Productos con al menos una búsqueda
productos_mas_buscados_sin_ceros = [] 

# Productos sin búsquedas
productos_mas_buscados_ceros = []

for elemento in productos_expandidos_mas_buscados:
  if elemento[5] != 0:
    productos_mas_buscados_sin_ceros.append(elemento)
  else:
    productos_mas_buscados_ceros.append(elemento)  

"Ahora se va a ordenar la lista en orden descendente" 

#Nuevamente se crea una copia de los productos expandidos

# Se vuelve a rellenar la copia de los productos expandidos
for producto in productos_expandidos:
  copia_productos_expandidos.append(producto)

# Se reordena la lista copia_productos_expandidos en orden descendente de acuerdo al número de búsquedas.
productos_expandidos_menos_buscados = []

while copia_productos_expandidos:
  minimo = copia_productos_expandidos[0][5]
  lista = copia_productos_expandidos[0]
  for i in range(1, len(copia_productos_expandidos)):
    if minimo > copia_productos_expandidos[i][5]:
      minimo = copia_productos_expandidos[i][5]
      lista = copia_productos_expandidos[i]
  productos_expandidos_menos_buscados.append(lista)
  copia_productos_expandidos.remove(lista)

'Ahora se va a separar la lista ordenada en los que sí tienen búsquedas en los que no'

# Productos con al menos una búsqueda
productos_menos_buscados_sin_ceros = []

# Productos sin búsquedas
productos_menos_buscados_ceros = []

for elemento in productos_expandidos_menos_buscados:
  if elemento[5] != 0:
    productos_menos_buscados_sin_ceros.append(elemento)
  else:
    productos_menos_buscados_ceros.append(elemento)

'''--------------------------------------------------- '''
"CALIFICACIONES PROMEDIO"
'''--------------------------------------------------- '''

'''Ahora se van a obtener las listas ordenadas de los productos expandidos de acuerdo a la calificación promedio que éstos han elegido '''

"Primero se va a ordenar la lista en orden descendente"

# Se vuelve a rellenar la copia de los productos expandidos
for producto in productos_expandidos:
  copia_productos_expandidos.append(producto)

# Se reordena la lista copia_productos_expandidos en orden descendente de acuerdo a su calificación promedio.
productos_expandidos_mejor_calificados = []

while copia_productos_expandidos:
  maximo = copia_productos_expandidos[0][7]
  lista = copia_productos_expandidos[0]
  for i in range(1, len(copia_productos_expandidos)):
    if maximo < copia_productos_expandidos[i][7]:
      maximo = copia_productos_expandidos[i][7]
      lista = copia_productos_expandidos[i]
  productos_expandidos_mejor_calificados.append(lista)
  copia_productos_expandidos.remove(lista)

# Ahora se va a separar la lista ordenada en los que sí tienen ventas en los que no
productos_mejor_calificados_sin_ceros = []
productos_mejor_calificados_ceros = []

for elemento in productos_expandidos_mejor_calificados:
  if elemento[6] != 0:
    productos_mejor_calificados_sin_ceros.append(elemento)
  else:
    productos_mejor_calificados_ceros.append(elemento) 

"Ahora se va a ordenar la lista en orden descendente" 


# Se vuelve a rellenar la copia de los productos expandidos
for producto in productos_expandidos:
  copia_productos_expandidos.append(producto)

# Se reordena la lista copia_productos_expandidos en orden descendente de acuerdo a su calificación promedio.
productos_expandidos_peor_calificados = []

while copia_productos_expandidos:
  minimo = copia_productos_expandidos[0][7]
  lista = copia_productos_expandidos[0]
  for i in range(1, len(copia_productos_expandidos)):
    if minimo > copia_productos_expandidos[i][7]:
      minimo = copia_productos_expandidos[i][7]
      lista = copia_productos_expandidos[i]
  productos_expandidos_peor_calificados.append(lista)
  copia_productos_expandidos.remove(lista)

# Ahora se va a separar la lista ordenada en los que sí tienen ventas en los que no
productos_peor_calificados_sin_ceros = []
productos_peor_calificados_ceros = []

for elemento in productos_expandidos_peor_calificados:
  if elemento[6] != 0:
    productos_peor_calificados_sin_ceros.append(elemento)
  else:
    productos_peor_calificados_ceros.append(elemento) 

"-----------------------------------------------------"
"DEVOLUCIONES"  
"-----------------------------------------------------"

'''Ahora se van a obtener las listas ordenadas de los productos expandidos de acuerdo al numero de devoluciones que han tenido '''

"Primero se va a ordenar la lista en orden descendente"

# Se vuelve a rellenar la copia de los productos expandidos
for producto in productos_expandidos:
  copia_productos_expandidos.append(producto)

# Se reordena la lista copia_productos_expandidos en orden descendente de acuerdo al número de devoluciones.
productos_expandidos_mas_devueltos = []

while copia_productos_expandidos:
  maximo = copia_productos_expandidos[0][9]
  lista = copia_productos_expandidos[0]
  for i in range(1, len(copia_productos_expandidos)):
    if maximo < copia_productos_expandidos[i][9]:
      maximo = copia_productos_expandidos[i][9]
      lista = copia_productos_expandidos[i]
  productos_expandidos_mas_devueltos.append(lista)
  copia_productos_expandidos.remove(lista)

# Ahora se va a separar la lista ordenada en los que sí tienen devoluciones en los que no. 
productos_mas_devueltos_sin_ceros = [] 
productos_mas_devueltos_ceros = []

for elemento in productos_expandidos_mas_devueltos:
  if elemento[-1] != 0:
    productos_mas_devueltos_sin_ceros.append(elemento)
  else:
    productos_mas_devueltos_ceros.append(elemento)  

"Ahora se va a ordenar la lista en orden descendente"   

"Ahora se va a ordenar la lista en orden descendente. ESTA LISTA NO ES DE UTILIDAD. SEGURAMENTE SE VA A BORRAR" 


# Se vuelve a rellenar la copia de los productos expandidos
for producto in productos_expandidos:
  copia_productos_expandidos.append(producto)

# Se reordena la lista copia_productos_expandidos en orden descendente de acuerdo al número de devoluciones.
productos_expandidos_menos_devueltos = []

while copia_productos_expandidos:
  minimo = copia_productos_expandidos[0][9]
  lista = copia_productos_expandidos[0]
  for i in range(1, len(copia_productos_expandidos)):
    if minimo > copia_productos_expandidos[i][9]:
      minimo = copia_productos_expandidos[i][9]
      lista = copia_productos_expandidos[i]
  productos_expandidos_menos_devueltos.append(lista)
  copia_productos_expandidos.remove(lista)

"-----------------------------------------------------"
"ANÁLISIS DE VENTAS"
"-----------------------------------------------------"

'Primero se va a anaexar en una lista de listas el año y el mes donde hubo una venta'

#Se define una lista vacía donde se van a ir insertamdo las listas [año, mes] en el cual se realizó la venta
datos_ventas = []

# Se va a iterar sobre cada venta en la lista lifestore_sales
for venta in lifestore_sales:
  # La fecha en la que se hizo la venta es una cadena de la forma "dd/mm/yyyy", por lo que hay que hacer un slicing en ella para obtener el año y el més en los que se hicieron las ventas
  anio = int(venta[-2][-4:])
  mes = int(venta[-2][3:5])
  ingreso = lifestore_products[venta[1]-1][2]
  ganancia = ingreso*(1 - venta[-1])
  combinacion = [ anio , mes, ingreso, venta[-1], ganancia]
  datos_ventas.append(combinacion)


'''Primero se va a hacer la evaluación anual de las ventas '''

# En esta lista se van a registrar los años
anios = []
# En esta lista se van a registrar la combinación mes/año
meses_anios = []
# En esta lista se van a registrar los meses
meses = []
# En esta lista va a ir la evaluación anual
evaluacion_anual = []
# En esta lista va a ir la evaluación mensual
evaluacion_mensual = []

# Se va a analizar cada lista de datos en datos_ventas,que es la combinacion, que es la recopilación de cierta información de cada venta.
for datos in datos_ventas:
  # Se observan el año y mes en que se hizo la venta
  anio = datos[0]
  mes = datos[1]
  # Si el año no está en la lista de años, se añade. En la evaluacón anual se añade una lista que después será llenada con los ingresos, devoluciones y ganancias.
  if anio not in anios:
    anios.append(anio)
    evaluacion_anual.append([anio] + [0,0,0,0])
  # Lo mismo se hace con los meses  
  if mes not in meses:  
    meses.append(mes)
    meses_anios.append([mes])
    evaluacion_mensual.append([mes])
  # Se va a iterar por cada elemento en la lista meses_anios.  
  for i in range(len(meses_anios)):
    # Para cada combinación [mes,año] se va a agregar una lista que va a tener los datos de las ventas de cada mes donde haya registros de ventas
    if meses_anios[i][0] == mes and ([anio] not in meses_anios[i]):
      meses_anios[i].append([anio])
      evaluacion_mensual[i].append([anio,0,0,0,0])  


# Se llena la lista evaluacion_anual con los datos de las ventas
for anio in evaluacion_anual:
  for datos in datos_ventas:
    if anio[0] == datos[0]:
      anio[1] += 1 # Aumenta el número de ventas
      anio[2] += datos[2] # Aumenta la cantidad de ingresos 
      anio[3] += datos[3] # Aumenta el número de devoluciones
      anio[4] += datos[4] # Aumentan las ganancias

# Lo mismo se hace con la lista correspondiente a la evaluación mensual.
for mes in evaluacion_mensual:
  for datos in datos_ventas:
    if mes[0] == datos[1]:
      for i in range(1,len(mes)):
        if mes[i][0] == datos[0]:
          mes[i][1] += 1 #ventas
          mes[i][2] += datos[2] #ingresos
          mes[i][3] += datos[3] #devoluciones
          mes[i][4] += datos[4] #ganancias

copia_evaluacion_mensual = []
for mes in evaluacion_mensual:
  copia_evaluacion_mensual.append(mes)

# Se reordena la lista evaluación_mensual en orden ascendente con repecto a los meses  
evaluacion_mensual_ordenada = []

while copia_evaluacion_mensual:
  minimo = copia_evaluacion_mensual[0][0]
  lista = copia_evaluacion_mensual[0]
  for i in range(1, len(copia_evaluacion_mensual)):
    if minimo > copia_evaluacion_mensual[i][0]:
      minimo = copia_evaluacion_mensual[i][0]
      lista = copia_evaluacion_mensual[i]
  evaluacion_mensual_ordenada.append(lista)
  copia_evaluacion_mensual.remove(lista)

# Se crea una lista con los nombres de todos los meses
meses_nombres = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Se crea una lista con los nombres de los meses donde ha habido al menos una venta
meses_nombres_con_ventas = []
for i in range(len(meses_nombres)):
  for mes in evaluacion_mensual_ordenada:
    if i+1 == mes[0]:
      meses_nombres_con_ventas.append(meses_nombres[i])


"-----------------------------------------------------"
" EXTENSIÓN ANÁLISIS MENSUAL"
"-----------------------------------------------------"
# Lista con cadenas de los meses y años donde se dieron las ventas. Se hizo de nuevo esta lista para no modificar nada de la sección anterior sin querer
meses_anios_str = []

for venta in lifestore_sales:
  anio = venta[-2][-4:]
  mes = venta[-2][3:5]
  combinacion = [anio, mes]
  if combinacion not in meses_anios_str:
    meses_anios_str.append(combinacion)

copia_meses_anios_str = []
for combinacion in meses_anios_str:
  copia_meses_anios_str.append(combinacion)

meses_anios_str_ordenada = []

# Se ordena la lista de meses anios utilizando los meses como métrica
while copia_meses_anios_str:
  maximo = copia_meses_anios_str[0][1]
  lista = copia_meses_anios_str[0]
  for i in range(1, len(copia_meses_anios_str)):
    if maximo < copia_meses_anios_str[i][1]:
      maximo = copia_meses_anios_str[i][1]
      lista = copia_meses_anios_str[i]
  meses_anios_str_ordenada.append(lista)
  copia_meses_anios_str.remove(lista)

# Ahora se va a ordenar la lista pero por año.   
# Copia de la list ordenada
copia_ma_str_ordenada = []
for x in meses_anios_str_ordenada:
  copia_ma_str_ordenada.append(x)

# Ordenación de la lista
meses_anios_str_ordenada = []
while copia_ma_str_ordenada:
  maximo = copia_ma_str_ordenada[0][0]
  lista = copia_ma_str_ordenada[0]
  for i in range(len(copia_ma_str_ordenada)):
    if maximo < copia_ma_str_ordenada[i][0]:
      maximo = copia_ma_str_ordenada[i][0]
      lista = copia_ma_str_ordenada[i]

  meses_anios_str_ordenada.append(lista)
  copia_ma_str_ordenada.remove(lista)   


''' Recordatorio. El formato de cada elemento en la lista 'productos expandidos' es [id_product, name, price, category, stock, busquedas, compras, calificacion_promedio, calificaciones_desglosadas, devoluciones].'''

# Se va a rellenar la lista de productos expandidos, pero ahora se va a hacer elemento a elemento, para proteger la lista de productos expandida.
copia_productos_expandidos =[]

for producto in productos_expandidos:
  lista = []
  for elemento in producto:
    lista.append(elemento)
  copia_productos_expandidos.append(lista)  

# Ahora se va a hacer una lista, la cual se va a llenar con listas que contengan un resumen de las listas por mes.
productos_por_mes_compras = []
productos_por_mes_calificaciones = []

# Para cada combinacion de mes año se va a hacer lo siguiente:

for combinacion in meses_anios_str_ordenada:
  mes_1 = combinacion[1]
  anio_1 = combinacion[0]
  # Se va a definir una lista vacía, la cual después se va a llenar
  lista = []
  # Se va a iterar para cada producto en la lista de productos.
  for producto in copia_productos_expandidos:
    # Se definen las variables compras, estrellas, estrellas_prom y devoluciones, las cuales se van a llenar conforme a las ventas que se han hecho.
    compras = 0
    estrellas = 0
    estrellas_prom = 0
    devoluciones = 0
    
    # Se va a interar por las ventas en lifestore_sales.
    for venta in lifestore_sales:

      # si los id de las ventas y el producto coinciden, además del mes y el año se sigue lo siguiente:
      condicion = (producto[0] == venta[1]) and (venta[-2][3:5] == mes_1) and (venta[-2][-4:] == anio_1)
      if condicion:

        # Se añade una compra a la lista de compras
        compras += 1

        # Se suma el número de estrellas
        estrellas += venta[2]

        # Se suma el número de devoluciones
        devoluciones += venta[-1]

    # Si el número de compras es distinto de cero, se sigue lo siguiente
    if compras != 0:
      
      # Se calcula el número de estrellas promedio
      estrellas_prom = round(estrellas/compras, 2)    

      # Se añade el producto y sus datos a la lista 'lista'
      lista.append([producto[0], producto[1], producto[2], producto[3], compras, estrellas_prom, devoluciones])

  # Se van a crear dos copias de la lista, una para ordenar de acuerdo a las ventas y otra para ordenar de acuerdo a las calificaciones.
  copia_lista_1 = []
  copia_lista_2 = []
  for elemento in lista:
    copia_lista_1.append(elemento)
    copia_lista_2.append(elemento)
  # Se reordena la lista de acuerdo a las compras
  lista_ordenada_compras = []
  while copia_lista_1:
    maximo = copia_lista_1[0][-3]
    lista_max = copia_lista_1[0]
    for i in range(1, len(copia_lista_1)):
      if maximo < copia_lista_1[i][-3]:
        maximo = copia_lista_1[i][-3]
        lista_max = copia_lista_1[i]
    lista_ordenada_compras.append(lista_max)
    copia_lista_1.remove(lista_max)
  # Se reordena la lista de acuerdo a las calificaciones promedio
  lista_ordenada_calif = []
  while copia_lista_2:
    maximo = copia_lista_2[0][-2]
    lista_max = copia_lista_2[0]
    for i in range(1, len(copia_lista_2)):
      if maximo < copia_lista_2[i][-2]:
        maximo = copia_lista_2[i][-2]
        lista_max = copia_lista_2[i]
    lista_ordenada_calif.append(lista_max)
    copia_lista_2.remove(lista_max)  
  # Se añade la lista correspondiente a la combinación a la lista productos_expandidos_por_mes.
  productos_por_mes_compras.append(lista_ordenada_compras)
  productos_por_mes_calificaciones.append(lista_ordenada_calif)   


# Se va a juntar la lista meses_anios_str_ordenada con la lista de productos expandidos por mes ordenados por compras.
analisis_mensual_compras = []
for i in range(len(meses_anios_str_ordenada)):
  analisis_mensual_compras.append(meses_anios_str_ordenada[i] + [productos_por_mes_compras[i]])

# Se va a juntar la lista meses_anios_str_ordenada con la lista de productos expandidos ordenados por calificación.
analisis_mensual_calif = []
for i in range(len(meses_anios_str_ordenada)):
  analisis_mensual_calif.append(meses_anios_str_ordenada[i] + [productos_por_mes_calificaciones[i]])

'''meses_nombres = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"] '''  

"El útlimo paso es meramente estético, se va a cambiar el número de los meses en las listas analisis_mensual_calif y analisis_mensual_compras por el nombre de més"

for j in range(len(analisis_mensual_calif)):
  for i in range(len(meses_nombres)):
    if int(analisis_mensual_calif[j][1]) == i+1:
      analisis_mensual_calif[j][1] = (meses_nombres[i])
      analisis_mensual_compras[j][1] = (meses_nombres[i])
      break

  

"-----------------------------------------------------"
"ANÁLISIS EXTENSIVO DE PRODUCTOS"
"-----------------------------------------------------"

''' Para poder mejorar las ventas hay que pensar en las consideraciones que hace un cliente antes de decidir si comprar o no algún producto. Por simplicidad se reducirá el número de consideraciones a 3: ventas, calificación promedio y porcentaje de devoluciones. No se considerará el precio porque los productos a analizar son de diferentes categorías, de tal manera que sus precios base son distintos y, por lo tanto, no están en igualdad de condiciones de comparación.

A cada una de las consideraciones se les va a asignar un peso de importancia:
  
  ventas: 0.55
  calif_promedio: 0.25
  porcentaje de devoluciones: 0.2

Estos grados de importancia son subjetivos, fueron establecidos de acuerdo a la consideración del programador

Posteriormente se evaluará el desempeño de cada producto ante estos criterios con una calificación del 1 al 5, siendo 1 la más baja y 5 la más alta. Estas calificaciones se multiplicarán por el grado de importancia y se sumarán los resultados. El producto con la mayor calificación será el mejor, mientras que el producto con la menor calificación será en peor.
'''

# Se definen los rangos
rangos_ventas = [[0,6], [6,18], [18,36], [36,72], [72, 284]]

# Se definen los pesos NOTA: DEBEN SUMAR 1
pesos = [0.55, 0.2, 0.25]

# Creamos una lista de los productos expandidos para proteger esta última
copia_productos_expandidos_calif = []
for producto in productos_expandidos:
  lista = []
  for elemento in producto:
    lista.append(elemento)
  copia_productos_expandidos_calif.append(lista) 

# Creamos una lista donde se va a colocar cada producto en su versión expandida con la calificación obtuvida
productos_expandidos_calif = []
for producto in copia_productos_expandidos_calif:
  # Se revisa que el producto sí tenga ventas.
  if producto[-4] != 0:
    # Se asignan las calificaciones correspondientes a la tasa de devoluciones y calificaciones productos_mejor_calificados_ceros
    tasa_dev = producto[-1]/producto[-4]
    calif = [producto[-4], producto[-1]/producto[-4]]
    s = producto[-3]*pesos[-1] + 5*(1- tasa_dev)*pesos[1]
    # Se asigna la calificación correspondiente a las ventas
    for i in range(len(rangos_ventas)):
      if rangos_ventas[i][0] <= producto[-4] < rangos_ventas[i][1]:
        s += (i+1)*pesos[0]
        break     
    producto.append(round(s,2))
    productos_expandidos_calif.append(producto) 

# Se crea una lista de la copia de productos con sus calificaciones para protegerla.
copia_productos_expandidos_calif = []
for x in productos_expandidos_calif:
  copia_productos_expandidos_calif.append(x)

# Reordenamos los productos de acuerdo a la calificación obtenida.
productos_expandidos_calif_ordenada = []
while copia_productos_expandidos_calif:
  maximo = copia_productos_expandidos_calif[0][-1]
  lista = copia_productos_expandidos_calif[0]
  for i in range(len(copia_productos_expandidos_calif)):
    if maximo < copia_productos_expandidos_calif[i][-1]:
      maximo = copia_productos_expandidos_calif[i][-1]
      lista = copia_productos_expandidos_calif[i]

  productos_expandidos_calif_ordenada.append(lista)
  copia_productos_expandidos_calif.remove(lista)


"-----------------------------------------------------"
"ANÁLISIS DE CATEGORÍAS"
"-----------------------------------------------------"

# Se va a ver cuáles son las categorías de los productos
categorias_productos = []
for producto in lifestore_products:
  if producto[3] not in categorias_productos:
    categorias_productos.append(producto[3])

# Se va a analizar cuántas ventas, busquedas y devoluciones a tenido cada categoría.
categorias_expandidas = []
for categoria in categorias_productos:
  cuenta_stock = 0
  cuenta_ventas = 0
  cuenta_busquedas = 0
  cuenta_dev = 0
  for producto in productos_expandidos:
    if categoria == producto[3]:
      cuenta_stock += producto[4]
      cuenta_ventas += producto[6]
      cuenta_busquedas += producto[5]
      cuenta_dev += producto[-1]
  lista = [categoria, cuenta_stock, cuenta_ventas, cuenta_busquedas, cuenta_dev]

  # Se va a calcular los porcentajes compra/busqueda y devoluciones/compra. Sin embargo, hay que tener cuidado de no dividir entre ceros.
  if cuenta_busquedas != 0:
    lista.append(round(cuenta_ventas/cuenta_busquedas,3))
  else:
    lista.append("inf")
  if cuenta_ventas != 0:
    lista.append(round(cuenta_dev/cuenta_ventas,3))
  else:
    lista.append("inf")
  categorias_expandidas.append(lista)        



"-------------------------------------------------------"
"ALMACENAMIENTO"
"-------------------------------------------------------"

# Se va contar cuánto espacio en almacenamiento ocupan los  productos que no se han vendido
almacenamiento_perdido = 0
cuenta_perdido = 0
for producto in productos_expandidos:
  if producto[-4] == 0:
    cuenta_perdido += 1
    almacenamiento_perdido += producto[4]


    
"-----------------------------------------------------"
"INTERACCIÓN USUARIO - ADMINISTRADOR."
"DEFINICIÓN DE LISTAS A USAR"
"-----------------------------------------------------"

# Primero se va a mostrar un mensaje de bienvenida

mensaje_bienvenida = ''' 

+++++++++++++++++++++++++++++++++++++++++++++++++++++++

             
              BIENVENIDO A LIFESTORE

        Lo mejor en electrónica está aquí


+++++++++++++++++++++++++++++++++++++++++++++++++++++++

 '''

mensaje_despedida = ''' 

+++++++++++++++++++++++++++++++++++++++++++++++++++++++

             
              GRACIAS POR TU VISITA

          Esperamos que vuelvas pronto


+++++++++++++++++++++++++++++++++++++++++++++++++++++++

 '''

"ADMINISTRADORES Y USUARIOS"
# Para el log-in se debe identificar si la persona que ingresa es un administrador. De facto se va a suponer que no lo es.
administrador = False

# Se definen los administradores y sus contraseñas
administradores = ["RuyRoa", "JavierRamirez"]
contrasenias_administradores = ["ruy43klm", "reivajR4m1"]

# Se definen los usuarios válidos que no tienen permiso de administrador y sus contraseñas.
usuarios = ["Juan3", "FerRdz"]
contrasenias_usuarios = ["161216", "F3rR4z"]

"+++++++++++++++++++++++++++++++++++++++++++++++++++++"
"OPCIONES EXTRA DE NAVEGACIÓN"

# Se definen otras opciones que se le puede dar al usuario para navegar en el programa
opciones_navegacion = ["inicio", "cerrar", "menu"]

"+++++++++++++++++++++++++++++++++++++++++++++++++++++"
"OPCIONES DEL MENÚ PRINCIPAL PARA CONSULTAR"
menu = False
persona = ''

opciones_menu= [ ["1", "Datos correspondientes a nuestras categorías", categorias_expandidas, len(categorias_expandidas), "\nEstos son los datos correspondientes a nuestras categorías\n"],
  
["2", "Conoce nuestros productos", productos_expandidos, len(productos_expandidos), "\nEstos son todos nuestros productos\n"], 

["3", "Top 100 productos buscados", 
productos_mas_buscados_sin_ceros, 100, "\nEstos son los productos más buscados\n"], 


["4", "Top 50 productos vendidos", productos_mas_comprados_sin_ceros, 50, "\nEstos son los productos más comprados\n"], 

 
["5", "Top 20 en reseñas", productos_mejor_calificados_sin_ceros, 20, "\nEstos son los productos peor calificados\n"], 

 
["6", "Menu Administrador"]] #En el menu de administrador se muestran los peores productos en cada categoría

"+++++++++++++++++++++++++++++++++++++++++++++++++++++"
"OPCIONES DEL MENÚ DEL ADMINISTRADOR"

menu_administrador = False

opciones_menu_admin = [

["1", "Productos menos buscados (al menos una búsqueda)", productos_menos_buscados_sin_ceros, 100, "\nEstos son los productos menos buscados\n"], 

["2", "Productos sin búsquedas", productos_menos_buscados_ceros, len(productos_menos_buscados_ceros), "\nEstos productos no han tenido búsquedas\n" ],

["3", "Productos menos comprados (al menos una compra)", productos_menos_comprados_sin_ceros, 50, "\nÉstos son los productos menos comprados\n"],

["4", "Productos sin ventas", productos_menos_comprados_ceros, len(productos_menos_comprados_ceros), "\nEstos productos no han tenido ventas\n" ],

["5", "Productos peor calificados por promedio", productos_peor_calificados_sin_ceros, 20, "\nÉstos son los productos peor calificados\n"],

["6", "Los productos más devueltos", productos_mas_devueltos_sin_ceros, len(productos_mas_devueltos_sin_ceros), "\nÉstos son los productos peor calificados\n"],

["7", "Productos más comprados por mes", analisis_mensual_compras],

["8", "Productos con las mejores reseñas por mes", analisis_mensual_calif],
 
["9", "Productos segun la métrica de evaluación", productos_expandidos_calif_ordenada, len(productos_expandidos_calif_ordenada), "\nLos mejores productos.\n\n Cada producto se valuó del 1 al 5 considerando tres criterios, el número de ventas, su calificación promedio y el número de devoluciones."],

["10", "Reporte anual y mensual de las ventas", "ingresos"]
]

"+++++++++++++++++++++++++++++++++++++++++++++++++++++"

"+++++++++++++++++++++++++++++++++++++++++++++++++++++"
"INICIO DE LA INTERACCIÓN"
"+++++++++++++++++++++++++++++++++++++++++++++++++++++"
# Se define la variable pantalla_de_inicio. Si este valor es verdadero se muestra la pantalla de inicio, si es falso no se muestra.
pantalla_de_inicio = True

# Se inicia un ciclo while que actúe hasta que la variable pantalla de inicio sea False
while pantalla_de_inicio:

  # Se cambia la variable pantalla de inicio a False. La idea de esto es poder volver a la pantalla de inicio cuando se desee.
  pantalla_de_inicio = False

  #Inicialmente se muestra el mensaje de bienvenida

  print(mensaje_bienvenida)
  
  # Se define una variable que se va a modificar si se quiere terminar el programa
  terminar_programa = False

  # Se le pide al usuario que indique si es un usuario, un administrador o si quiere salir del programa. Por lo cual se le va a dar tres opciones de ingreso.

  entradas_validas = ["1", "2", "cerrar", "registrar"]

  # Se define la clase de entrada inicial, la cual no debe estar en la lista de entradas válidas. Esta variable va a tomar el valor de lo que ingrese el usuario al preguntarle lo que quiere hacer.
  entrada = ''

  # Se analiza si la entrada del usuario es válida o no.
  while entrada not in entradas_validas:

    # Se le pregunta al usuario si es un usuario, un administrador o si quiere salir de la página. Lo que ingrese será el nuevo valor de la variable entrada.

    entrada = input("Para comenzar, teclea: \n 1: Si eres un usuario. \n 2: Si eres un administrador.\nregistrar: Si quieres registrar un nuevo usuario\ncerrar: Si quieres salir del programa. \n \n")

    # Si la entrada no es válida, le manda un mensaje de error.
    if entrada not in entradas_validas:
      print('''

      +++++++++++++++++++++++++++++++++++++++++++++++++

      Lo sentimos, esta no es una opción valida. 
      Vuelve a intentarlo. 
      ''')
      
  # Si el usuario decidió salir del programa, se cambia la variable "terminar_programa" a True.
  if entrada == "cerrar":
    terminar_programa = True

  elif entrada == "registrar":
    usuario_valido = False
    while not usuario_valido:

      print("+++++++++++++++++++++++++++++\n")
      entrada_usuario_nuevo = input("Por favor ingresa un nuevo nombre de usuario.\nSi deseas regresar a la pantalla de inicio teclea: inicio\nSi deseas cerrar el programa teclea: cerrar\n\n")

      # Si se ingresó 'inicio', se regresa a la pantalla de inicio.
      if entrada_usuario_nuevo == "inicio":
        pantalla_de_inicio = True
        break

      # Si se eligió cerrar, el programa termina.
      elif entrada_usuario_nuevo == "cerrar":
        terminar_programa = True
        break 

      elif entrada_usuario_nuevo != "inicio" and entrada_usuario_nuevo != "cerrar":
        # Para evitar errores se revisa que el nomnre de usuario no haya sido registrado previamento como otro usuario o administrador y que no sea parte de las opciones de navegación.
        if not(entrada_usuario_nuevo in usuarios or entrada_usuario_nuevo in opciones_navegacion or entrada_usuario_nuevo in entradas_validas or entrada_usuario_nuevo in administradores):

          # Se introducen dos variables, la nueva contrasenia y la confirmacion de la contraenia.
          entrada_contrasenia_nueva = 0
          entrada_confirmacion_constrasenia = 1

          # Mientras las contraseñas no sean iguales se corre el siguiente código
          while entrada_contrasenia_nueva != entrada_confirmacion_constrasenia:

            print("++++++++++++++++++++++++++++++\n")

            # Se le pide al usuario que ingrese su contraseña, además se le da la oportunidad de volver a la página de inicio o volver al programa.
            entrada_contrasenia_nueva = input("\nPor favor ingresa una contraseña:\n\nSi deseas regresar a la pantalla de inicio teclea: inicio\nSi deseas cerrar el programa teclea: cerrar\n\n")

            if entrada_contrasenia_nueva == "inicio":
              pantalla_de_inicio = True
              #Para que deje de correr el ciclo while
              usuario_valido = True
              break

            elif entrada_contrasenia_nueva == 'cerrar':
              terminar_programa =  True
              #Para que deje de correr el ciclo while
              usuario_valido = True
              break

            # Si el usuario no decidió volver al inicio o cerrar el programa, la contraseña se toma como válida. Se prosigue a la confirmación
            else:  

              print("++++++++++++++++++++++\n")

              # El usuario debe confirmar su contraseña, además se le da la opción de volver al inicio o cerrar el programa
              entrada_confirmacion_constrasenia = input("Por favor confirme su contraseña:\n\nSi deseas regresar a la pantalla de inicio teclea: inicio\nSi deseas cerrar el programa teclea: cerrar\n\n")

              if entrada_confirmacion_constrasenia == "inicio":
                pantalla_de_inicio = True
                #Para que deje de correr el ciclo while
                usuario_valido = True
                break

              elif entrada_confirmacion_constrasenia == 'cerrar':
                terminar_programa = True
                #Para que deje de correr el ciclo while
                usuario_valido = True
                break  
              
              # Si las contraseñas no coinciden se muestra un mensaje de error
              elif entrada_contrasenia_nueva != entrada_confirmacion_constrasenia:

                print('''
                +++++++++++++++++++++++++++++++
            
                Las contraseñas no coinciden.
                Inténtalo de nuevo
               ''')

              # Si las contraseñas coinciden se añade el nombre de usuario y contraseña a las listas correspondientes.
              else:
                usuarios.append(entrada_usuario_nuevo)
                contrasenias_usuarios.append(entrada_contrasenia_nueva)
                # Para terminar el ciclo while.
                usuario_valido = True
                pantalla_de_inicio = True

        # si el nombre de usuario no es uno válido, se muestra un mensaje de error.
        else:
          print('''
          ++++++++++++++++++++++++++++++

          Este usuario no es valido.
          Por favor escoge otro nombre ''')

  # Si la entrada corresponde a un usuario se sigue al siguiente nivel de interacción. 
  elif entrada == "1":
    # Se muestran los usuarios válidos

    print("+++++++++++++++++++++++++++++++++++++++++++++\n")
    # Se declara la variable entrada_usuario, la cual se va a modificar con la entrada del usuario
    entrada_usuario = 0

    # Si la entrada del usuario  no está en la lista de usuarios o en la lista de las otras opciones se va a repetir el siguiente ciclo while..
    while entrada_usuario not in usuarios and entrada_usuario not in opciones_navegacion:

      # Se le pide al usuario que ingrese su nombre de usuario o si quiere volver a la pantalla de inicio o salir del programa
      entrada_usuario = input("\nTeclea tu nombre de usuario\nSi quieres regresar a la pantalla de inicio teclea: inicio.\nSi quieres cerrar el programa teclea: cerrar\n\n")

      # Si la entrada del usuario está en la lista de usuarios valida. Se prosigue a pedir su contraseña
      
      if entrada_usuario in usuarios:

        # Se define la variable constrasenia, la cual va a tomar su valor dependiendo del usuario que quiere ingresar.
        contrasenia = ''

        # Esto se va a hacer con un ciclo for y viendo en qué indice el usuario que ingresó la persona coincide con el usuario en la lista de usuarios.
        for i in range(len(usuarios)):
          # Cuando se de la coincidencia, se asigna la contrasenia y se interrumpe el ciclo.
          if usuarios[i] == entrada_usuario:
            contrasenia = contrasenias_usuarios[i]
            break   

        # Se saluda al usuario    
        print('''
        +++++++++++++++++++++++++++++++++++++++++

        Hola, {0}
        '''.format(entrada_usuario))

        # Se crea la variable entrada_contrasenia la cual tomará su valor cuando el ingresario ingrese algo al programa
        entrada_contrasenia = 0

        intentos_restantes = 5

        # Mientras la contraseña sea incorrecta se va a continuar este ciclo while hasta que se acabe el número de intentos.

        while entrada_contrasenia != contrasenia:

          entrada_contrasenia = input("\nPara continuar ingresa tu contraseña.\nSi quieres volver a la pantalla de inicio teclea: {0}  \nSi quieres cerrar el programa teclea: {1}\n\n ".format(opciones_navegacion[0], opciones_navegacion[1]))

          # Si la contraseña no es válida se muestra al usuario un mensaje y los números de intentos restantes.

          if entrada_contrasenia == opciones_navegacion[0]:
            pantalla_de_inicio = True
            break

          elif entrada_contrasenia == opciones_navegacion[1]:
            terminar_programa = True
            break  

          elif entrada_contrasenia != contrasenia:
            intentos_restantes -= 1
            print('''
            ++++++++++++++++++++++++++++++++++++++++++++
            Lo sentimos esta contraseña no es válida. 
            
            Numero de intentos restantes: {0}
            
            '''.format(intentos_restantes))
            
            if intentos_restantes == 0:
              intentos_restantes = 5
              print(''''
              ++++++++++++++++++++++++++++++++++++++++++
              ¡Has excedido el número de intentos! 
              Por seguridad se cerrará el programa
              
              ''')
              
              # La variable para terminar el programa se vuelve True
              terminar_programa = True

              # Se interrumpe el ciclo while
              break 

            elif entrada_contrasenia == contrasenia:
              continue

            '''AQUÍ HAY UN BUG QUE HAY QUE ARREGLAR '''

        if entrada_contrasenia == contrasenia:
          administrador = False
          menu = True
          persona = entrada_usuario
    
      # Si la entrada del usuario es una de los elementos de la lista de opciones se sigue lo siguiente:
      elif entrada_usuario in opciones_navegacion:

        # Si el usuario teclea 'inicio', regresa a la pantalla de inicio
        if entrada_usuario == opciones_navegacion[0]:
          pantalla_de_inicio = True
          break

        # Si teclea 'cerrar' termina el programa  
        elif entrada_usuario == opciones_navegacion[1]:
          terminar_programa = True
          break
        else:
          print('''
          ++++++++++++++++++++++++++++++++++++++++
          Algo ha salido mal. El programador cometió un error.''')  


      elif entrada_usuario not in usuarios and entrada_usuario not in opciones_navegacion:
        print('''
        ++++++++++++++++++++++++++++++++++++

        Lo sentimos, tu entrada no es válida. 
        Inténtalo de nuevo''')

      else:
        print('''
          ++++++++++++++++++++++++++++++++++++

          Algo ha salido mal. El programador cometió un error.''')        

  # Si la entrada corresponde a un administrador se sigue al siguiente nivel de interacción.
  elif entrada == "2":
    # Se muestran los administradores válidos

    # Se declara la variable entrada_administrador, la cual se va a modificar con la entrada del administrador
    entrada_administrador = 0

    print("+++++++++++++++++++++++++++++++++++++++++++++\n")

    # Si la entrada del administrador  no está en la lista de administradores o en la lista de las otras opciones se va a repetir el siguiente ciclo while..
    while entrada_administrador not in administradores and entrada_administrador not in opciones_navegacion:

      # Se le pide al administrador que ingrese su nombre de administrador o si quiere volver a la pantalla de inicio o salir del programa
      entrada_administrador = input("\nTeclea tu nombre de administrador:\nSi quieres regresar a la pantalla de inicio teclea: inicio.\nSi quieres cerrar el programa teclea: cerrar\n\n")

      # Si la entrada del administrador está en la lista de administradores valida. Se prosigue a pedir su contraseña
      
      if entrada_administrador in administradores:

        # Se define la variable constrasenia, la cual va a tomar su valor dependiendo del administrador que quiere ingresar.
        contrasenia = ''
        # Esto se va a hacer con un ciclo for y viendo en qué indice el administrador que ingresó la persona coincide con el administrador en la lista de administradores.
        for i in range(len(administradores)):
          # Cuando se de la coincidencia, se asigna la contrasenia y se interrumpe el ciclo.
          if administradores[i] == entrada_administrador:
            contrasenia = contrasenias_administradores[i]
            break   

        # Se saluda al administrador    
        print('''
        +++++++++++++++++++++++++++++++++++++++++
        
        Hola, {0}
        '''.format(entrada_administrador))

        # Se crea la variable entrada_contrasenia la cual tomará su valor cuando el ingresario ingrese algo al programa
        entrada_contrasenia = 0

        intentos_restantes = 5

        # Mientras la contraseña sea incorrecta se va a continuar este ciclo while hasta que se acabe el número de intentos.

        while entrada_contrasenia != contrasenia:
          entrada_contrasenia = input("\nPara continuar ingresa tu contraseña.\nSi quieres volver a la pantalla de inicio teclea: {0}\nSi quieres cerrar el programa teclea: {1}\n\n".format(opciones_navegacion[0], opciones_navegacion[1]))

          # Si la contraseña no es válida se muestra al administrador un mensaje y los números de intentos restantes.

          if entrada_contrasenia != contrasenia:
            intentos_restantes -= 1
            print('''
            ++++++++++++++++++++++++++++++++++++++++++++
            
            Lo sentimos esta contraseña no es válida. 
            
            Numero de intentos restantes: {0}
            
            '''.format(intentos_restantes))

            # Si se excede el número de intentos se cierra el programa.
            if intentos_restantes == 0:
              intentos_restantes = 5
              print('''
              ++++++++++++++++++++++++++++++++++++++++++
              
              ¡Has excedido el número de intentos!
              Por seguridad se cerrará el programa
              
              ''')
              
              # La variable para terminar el programa se vuelve True
              terminar_programa = True

              # Se interrumpe el ciclo while
              break 

            elif entrada_contrasenia == contrasenia:
              administrador = True
              persona = entrada_administrador
              menu = True
              continue

            '''AQUÍ HAY UN BUG QUE HAY QUE ARREGLAR AL PONER LA SENTENCIA ELSE'''

        if entrada_contrasenia == opciones_navegacion[0]:
          pantalla_de_inicio = True
          break

        elif entrada_contrasenia == opciones_navegacion[1]:
          terminar_programa = True
          break  


        # Si la contraseña es correcta se activa la opción de ver el menú, se indica que la persona es un administrador y se asigna el nombre de administrador a la variable persona
        if entrada_contrasenia == contrasenia:
          administrador = True
          menu = True
          persona = entrada_administrador

      # Si la entrada del administrador es una de los elementos de la lista de opciones se sigue lo siguiente:
      elif entrada_administrador in opciones_navegacion:

        # Si el administrador teclea 'inicio', regresa a la pantalla de inicio
        if entrada_administrador == opciones_navegacion[0]:
          pantalla_de_inicio = True
          break

        # Si teclea 'cerrar' termina el programa  
        elif entrada_administrador == opciones_navegacion[1]:
          terminar_programa = True
          break
        else:
          print('''
          ++++++++++++++++++++++++++++++++++++++++

          Algo ha salido mal. El programador cometió un error.''')  


      elif entrada_administrador not in administradores and entrada_administrador not in opciones_navegacion:
        print('''
        
        ++++++++++++++++++++++++++++++++++++++++++++

        Lo sentimos, tu entrada no es válida. 
        Inténtalo de nuevo''')

      else:
        print('''
          ++++++++++++++++++++++++++++++++++++

          Algo ha salido mal. El programador cometió un error.''') 
  
  # si la variable del menu es cierta, éste se muestra. Ésta variable se vuelve cierta cuando el usuario o administrador iniciaron sesión de forma exitosa.

  while menu:
    # Se cambia la variable menu a False para no generar un ciclo infinito
    menu = False

    # Se crea una cadena que indique si el usuario que ingresó es un administrador o no.
    es_administrador = "No"
    if administrador:
      es_administrador = 'Sí'

    # Se muestra un mensaje de bienvenida, si es un administrador o no y las opciones que tiene.
    print(''' 
    ++++++++++++++++++++++++++++++++++++++++
    
    Bienvenid@, {0}!
    Eres administrador: {1}

    '''.format(persona, es_administrador))

    print('''
    Nuestros productos se dividen en las siguientes categorías: ''')

    for categoria in categorias_productos:
      print(categoria)

    print('''

    Estas son las opciones que puedes consultar: 
    
    ''')

    for opcion in opciones_menu:
      print(opcion[0], opcion[1])

    # Se crea la variable entrada_menu, la cual se modificará al momento de que el usuario ingrese lo que quiere hacer
    entrada_menu = ''

    # Se hace una lista con las entradas válidas
    entradas_menu_validas = []
    for opcion in opciones_menu:
      entradas_menu_validas.append(str(opcion[0]))

    # Si la entrada no es válida se repite el siguiente cicli:
    while entrada_menu not in entradas_menu_validas and entrada_menu not in opciones_navegacion[0:2]: #Se hizo un slicing a las opciones de navegación para evitar errores
      entrada_menu = input('''
    
      Ingresa el número de la opción que quieres consultar de nuestro menú

      Si quieres volver a la pantalla de inicio teclea: inicio
    
      Si quieres cerrar el programa teclea: cerrar. 
    
      ''' ) 

      if  entrada_menu not in entradas_menu_validas and entrada_menu not in opciones_navegacion[0:2]:
        print('''
        +++++++++++++++++++++++++++++++++++++

        Lo sentimos, esa no es una opción válida. Intenta de nuevo.
        
        ''') 

    # Si la entrada está en el menú de navegación, se inicia o se cierra el programa.
    if entrada_menu in opciones_navegacion[0:2]:
      if entrada_menu == "inicio":
        pantalla_de_inicio = True
        break

      elif entrada_menu == "cerrar":
        terminar_programa = True
        break 

      else:
        print("El programador cometió un error") 

    # Si la variable entrada_menu es una de las opciones válidas.
    elif entrada_menu in entradas_menu_validas:

      # Se define la variable entrada de navegación, la cual se va a modificar con la entrada del usuario.


        # Ciclo para determinar si la sección elegida es la correspondiente al administrador.
      for opcion in opciones_menu:

        if opcion[0] == entrada_menu and entrada_menu != entradas_menu_validas[-1]:
          seccion_admin = False
          break

        elif opcion[0] == entrada_menu and entrada_menu == entradas_menu_validas[-1]:
          seccion_admin = True
          break

      # Si no se está en la sección de admin:
      
      if not seccion_admin:
        if opcion[2] == categorias_expandidas:

          print('''
          +++++++++++++++++++++++++++++++++++++
          
          Estos son los datos correspondientes a cada categoría
          
          ''')
          
          for lista in opcion[2]:
            print("Categoria: {0}".format(lista[0]))
            print("Stock: {0}, Ventas: {1}, Búsquedas: {2}, \n Devoluciones: {3}, Ventas/Búsquedas: {4}, Devoluciones/Ventas: {5}".format(lista[1], lista[2], lista[3], lista[4], lista[5], lista[6]))
            print("\n\n")


        else:  

          if opcion[3] > len(opcion[2]):
            lista_por_usar = opcion[2]
          else:
            lista_por_usar = opcion[2][:opcion[3]]    

          mensajes_desglose = ["Id del producto: {0}", "Nombre del producto: {0}", "Precio MXN: {0}", "Categoria: {0}", "Productos disponibles: {0} ", "Número de búsquedas: {0}", "Número de compras: {0}", "Calificación promedio: {0}", "Desglose de calificaciones: ", "Número de devoluciones: {0}"]

          print("++++++++++++++++++++++++++++++++++++++\n")

          print(opcion[4])

          for i in range(len(lista_por_usar)):
            print("Posición: {0}".format(i+1))
            for j in range(len(mensajes_desglose)):
              if j != 8:
                print(mensajes_desglose[j].format(lista_por_usar[i][j]))

              else:
                print(mensajes_desglose[j])
                for elemento in lista_por_usar[i][j]:
                  print(elemento)

            print("\n\n")

          "Código para reordenar la lista por categoría"
          reordenar_por_categoria = ""
          while reordenar_por_categoria != "si" and reordenar_por_categoria != "no":

            reordenar_por_categoria = input("¿Deseas reordenar la lista anterior por categorìa? (si/no)\n\n")

            if reordenar_por_categoria != "si" and reordenar_por_categoria != "no":
              print("+++++++++++++++++++++\n\nLo sentimos, esta opción no es válida. Intente de nuevo")

          # Si se dice que sí se quiere reordenar la lista por categoría se sigue lo siguiente.
          if reordenar_por_categoria == "si":
            
            # Se genera una copia de la lista usada para protegerla
            copia_lista_por_usar = []
            for producto in lista_por_usar:
              lista = []
              for elemento in producto:
                lista.append(elemento)
              copia_lista_por_usar.append(lista)
            
            # Código para reordenar la lista por actegoría
            lista_por_usar_categoria = []
            while copia_lista_por_usar:
              minimo = copia_lista_por_usar[0][3]
              lista = copia_lista_por_usar[0]
              for i in range(len(copia_lista_por_usar)):
                if minimo > copia_lista_por_usar[i][3]:
                  minimo = copia_lista_por_usar[i][3]
                  lista = copia_lista_por_usar[i]
              lista_por_usar_categoria.append(lista)
              copia_lista_por_usar.remove(lista)
            
            print("+++++++++++++++++++++\n\nEstos son los productos ordenados por categoría")
            # Código para enlistar los productos
            categoria_mostradas = []
            for i in range(len(lista_por_usar_categoria)):
              # Código para que muestre el nombre de la categoría para que ingrese a una nueva.
              categoria =  lista_por_usar_categoria[i][3]
              
              if categoria not in categoria_mostradas:
                categoria_mostradas.append(categoria)
                print("+++++ {0} +++++\n".format(categoria))
              
              #print("Posición: {0}".format(i+1))

              for j in range(len(mensajes_desglose)):
                if j != 8:
                  print(mensajes_desglose[j].format(lista_por_usar_categoria[i][j]))

                else:
                  print(mensajes_desglose[j])
                  for elemento in lista_por_usar_categoria[i][j]:
                    print(elemento)

              print("\n\n")

        # Código para que el usuario idique lo que quiere hacer.              
        entrada_navegacion = ''

        while entrada_navegacion not in  opciones_navegacion:
              
          entrada_navegacion = input('''

          ++++++++++++++++++++++++++++++++++++

          Si quieres volver al menú principal teclea: menu

          Si quieres cerrar sesión y volver a la pantalla de inicio teclea: inicio

          Si quieres cerrar el programa teclea: cerrar
          ''')   

          if entrada_navegacion not in opciones_navegacion:
            print("\nLo sentimos, esta no es una opción válida. Intente de nuevo.\n")
            
        if entrada_navegacion == "menu":
          menu = True
        
        elif entrada_navegacion == "inicio":
          pantalla_de_inicio = True
          
        elif entrada_navegacion == "cerrar":
          terminar_programa = True
          
      # Si se quiere acceder a la sección del administrador se sigue lo siguiente:            
      else:

        # Si la persona que quiere ingresar al menú de administrador no lo es se muestra un mensaje.

        if not administrador:

          print(''' 
          +++++++++++++++++++++++++++++++++++++++++

          Lo sentimos, no tienes permiso para acceder a esta opción. Si eres un administrador cierra sesión e ingresa como administrador. ''')

          # Se le pide al usuario que indique qué es lo 
          entrada_navegacion = ''

          while entrada_navegacion not in  opciones_navegacion:
                
            entrada_navegacion = input('''

            ++++++++++++++++++++++++++++++++++++

            Si quieres volver al menú principal teclea: menu

            Si quieres cerrar sesión y volver a la pantalla de inicio teclea: inicio

            Si quieres cerrar el programa teclea: cerrar

              ''')

            if entrada_navegacion not in opciones_navegacion:
              print("\nLo sentimos, esta no es una opción válida. Intente de nuevo.\n")
              mostrar_lista = False


          if entrada_navegacion == "menu":
            menu = True

          elif entrada_navegacion == "inicio":
            pantalla_de_inicio = True

          elif entrada_navegacion == "cerrar":
            terminar_programa = True  

            # En caso de que sea administrador, se procede a mostrar el menu  

        # Si la persona es administrador se sigue lo siguiente
        else:
          
          # Variable que si es cierta se muestra el menu del administrador
          menu_administrador = True

          while menu_administrador:
            # Se cambia la variable menu_administrador a False para evitar un loop infinito
            menu_administrador = False

            #  Se despliquega el menu del administrador
            print('''
            +++++++++++++++++++++++++++++++++++++++
          
            Estas son las opciones que puedes consultar

            ''')

            for opcion in opciones_menu_admin:
              print(opcion[0], opcion[1])

            print("\n\n")

            # Se introducen las opciones de navegacion en el menu del administrador
            entradas_admin_validas = []
            for opcion in opciones_menu_admin:
              entradas_admin_validas.append(opcion[0])

            # Se le pide al administrador que ingrese lo que desea hacer
            entrada_admin = ''
            while entrada_admin not in entradas_admin_validas and entrada_admin not in opciones_navegacion:

              entrada_admin = input("\nIngresa el numero de la opción que quieras consultar:\nSi quieres volver al menu principal teclea: menu.\nSi quieres volver a la pantalla de inicio teclea: inicio.\nSi quieres cerrar el programa teclea: cerrar\n\n")  

              if entrada_admin not in entradas_admin_validas and entrada_admin not in opciones_navegacion:
                print('''
                ++++++++++++++++++++++++++++
                Lo sentimos, esa no es una opción válida.
                Intenta de nuevo.''')

            # Se introducen las consecuencias de ingresar "menu" , "inicio" y cerrar
            if entrada_admin == "menu":
              menu = True
              break
            elif entrada_admin == "inicio":
              pantalla_de_inicio = True
              break
            elif entrada_admin == "cerrar":
              terminar_programa = True
              break


            # Si se ingresó una de las opciones del menu se sigue lo siguiente:
            elif entrada_admin in entradas_admin_validas:
              
              # Las listas que corresponden a cada entrada del menú son distintas, se va a agrupar dichas listas de acuerdo al formato que tengan.
              tipo_lista = 0
              for opcion in opciones_menu_admin:
                if entrada_admin == opcion[0]:
                  if opcion[2] == productos_menos_buscados_sin_ceros or opcion [2] == productos_menos_comprados_sin_ceros or opcion[2] == productos_peor_calificados_sin_ceros or opcion[2] == productos_mas_devueltos_sin_ceros or opcion[2] == productos_expandidos_calif_ordenada:
                    tipo_lista = 1
                    break
                  
                  elif opcion[2] == productos_menos_buscados_ceros or opcion[2] == productos_menos_comprados_ceros:
                    tipo_lista = 2
                    break 

                  elif opcion[2] == analisis_mensual_compras or opcion[2] ==   analisis_mensual_calif:
                    tipo_lista = 3
                    break

                  elif opcion[2] == "ingresos":
                    tipo_lista = 4
                    break

              # Si la lista es del tipo 4, se muestra el análisis anual y mensual de ventas e ingresos.
              if tipo_lista == 4:

                # Se va a mostrar el reporte anual
                print('''

                  +++++++++++++++++++++++++
        
                  Reporte anual de ventas: 
        
                  ''')

                # Mensajes a imprimir cuando se desglose la lista correspondiente a cada año
                mensajes_eval_anual = ["Año: {0}", "Ventas: {0}", "Ingreso MXN: {0}", "Devoluciones: {0}", "Ganancia MXN: {0}"]
                
                for anio in evaluacion_anual:
                  for i in range(len(mensajes_eval_anual)):
                    print(mensajes_eval_anual[i].format(anio[i]))
                
                  print("\n\n")

                # Ahora se muestra el análisis mensual  

                print('''

                +++++++++++++++++++++++++
              
                Reporte mensual de ventas: 
              
                ''') 

                # Mesajes a mostrar cuando se desglose la lista.

                mensajes_eval_mensual =  ["Mes: {0}\n\n", "Año: {0}", "Ventas: {0}", "Ingreso: {0}", "Devoluciones: {0}", "Ganancia: {0}"]

                # Desglose de la lista
                for i in range(len(evaluacion_mensual_ordenada)):
                  print(mensajes_eval_mensual[0].format(meses_nombres_con_ventas[i]))

                  for j in range(1,len(evaluacion_mensual_ordenada[i])):
                  
                    for k in range(1,len(mensajes_eval_mensual)):
                      print(mensajes_eval_mensual[k].format(evaluacion_mensual_ordenada[i][j][k-1]))

                    print("\n")  

                  print("\n")

                # Se le pide al administrador que indique qué es lo que quiere hacer. Puede volver al menu del administrador, al menu principal, al menú de inicio o cerrar el programa.
                entrada_navegacion_admin = ""
                entradas_validas = ["menu administrador", "menu principal", "inicio", "cerrar"]

                while entrada_navegacion_admin not in entradas_validas:
                  
                  entrada_navegacion_admin = input("Si quieres volver al menu del administrador, teclea: menu administrador.\nSi quieres volver al menú principal, teclea: menu principal.\nSi quieres volver a la pantalla de inicio, teclea: inicio\nSi quieres cerrar el programa teclea: cerrar\n\n")

                if entrada_navegacion_admin == "menu administrador":
                  menu_administrador = True
                elif entrada_navegacion_admin == "menu principal":
                  menu = True
                elif entrada_navegacion_admin == "inicio":
                  pantalla_de_inicio = True
                elif entrada_navegacion_admin == "cerrar":
                  terminar_programa = True  

              #Si la lista es del tipo 2, se sigue otro método para explorar su contenido.

              elif tipo_lista == 2:
                print("+++++++++++++++++++\n")
                print(opcion[4])
                print("\n")

                # Mensajes a desglosar cuando se muestren los datos
                mensajes_desglose_corto = ["Id producto: {0}", "Nombre_producto: {0}", "Precio: {0}", "Categoria: {0}", "Artículos disponibles: {0}"]

                posicion = 0
                for elemento in opcion[2]:
                  posicion += 1
                  print(posicion)
                  for i in range(len(mensajes_desglose_corto)):
                    print(mensajes_desglose_corto[i].format(elemento[i]))

                  print("\n")


                "Código para reordenar la lista por categoría"

                reordenar_por_categoria = ""
                while reordenar_por_categoria != "si" and reordenar_por_categoria != "no":

                  reordenar_por_categoria = input("¿Deseas reordenar la lista anterior por categorìa? (si/no)\n\n")

                  if reordenar_por_categoria != "si" and reordenar_por_categoria != "no":
                    print("+++++++++++++++++++++\n\nLo sentimos, esta opción no es válida. Intente de nuevo")

                if reordenar_por_categoria == "si":
                  
                  # Se genera una copia de la lista usada para protegerla
                  copia_lista_por_usar = []
                  for producto in opcion[2]:
                    lista = []
                    for elemento in producto:
                      lista.append(elemento)
                    copia_lista_por_usar.append(lista)
                  
                  # Código para reordenar la lista por actegoría
                  lista_por_usar_categoria = []
                  while copia_lista_por_usar:
                    minimo = copia_lista_por_usar[0][3]
                    lista = copia_lista_por_usar[0]
                    for i in range(len(copia_lista_por_usar)):
                      if minimo > copia_lista_por_usar[i][3]:
                        minimo = copia_lista_por_usar[i][3]
                        lista = copia_lista_por_usar[i]
                    lista_por_usar_categoria.append(lista)
                    copia_lista_por_usar.remove(lista)

                  print("+++++++++++++++++++++\n\nEstos son los productos ordenados por categoría")  

                  # Código para enlistar los productos
                  categoria_mostradas = []
                  for i in range(len(lista_por_usar_categoria)):
                    # Código para que muestre el nombre de la categoría para que ingrese a una nueva.
                    categoria =  lista_por_usar_categoria[i][3]
                    if categoria not in categoria_mostradas:
                      categoria_mostradas.append(categoria)
                      print("+++++ {0} +++++\n".format(categoria))

                    #print("Posición: {0}".format(i+1))
                    for j in range(len(mensajes_desglose_corto)):
                      if j != 8:
                        print(mensajes_desglose_corto[j].format(lista_por_usar_categoria[i][j]))

                      else:
                        print(mensajes_desglose_corto[j])
                        for elemento in lista_por_usar_categoria[i][j]:
                          print(elemento)

                    print("\n\n")  

                # Código para que el administrador indique qué es lo que quiere hacer.
                entrada_navegacion_admin = ""
                entradas_validas = ["menu administrador", "menu principal", "inicio", "cerrar"]

                while entrada_navegacion_admin not in entradas_validas:
                  
                  entrada_navegacion_admin = input("Si quieres volver al menu del administrador, teclea: menu administrador.\nSi quieres volver al menú principal, teclea: menu principal.\nSi quieres volver a la pantalla de inicio, teclea: inicio\nSi quieres cerrar el programa teclea: cerrar\n\n")

                if entrada_navegacion_admin == "menu administrador":
                  menu_administrador = True
                elif entrada_navegacion_admin == "menu principal":
                  menu = True
                elif entrada_navegacion_admin == "inicio":
                  pantalla_de_inicio = True
                elif entrada_navegacion_admin == "cerrar":
                  terminar_programa = True  

              # Si la lista es del tipo 1 se sigue otro método para visualizar sus datos
              elif tipo_lista == 1:

                print("+++++++++++++++++++\n")
                print(opcion[4])
                print("\n")

                mensajes_desglose = ["Id del producto: {0}", "Nombre del producto: {0}", "Precio MXN: {0}", "Categoria: {0}", "Productos disponibles: {0} ", "Número de búsquedas: {0}", "Número de compras: {0}", "Calificación promedio: {0}", "Desglose de calificaciones: ", "Número de devoluciones: {0}"]

                # Código para mostrar los datos.
                posicion = 0
                for elemento in opcion[2]:
                  posicion += 1
                  print("Posición: {0}".format(posicion))
                  
                  # Si es la lista que contiene las calificcaciones utilizando la métrica se añade la calificación. Es el único caso especial de este tipo de lista
                  if opcion[2] == productos_expandidos_calif_ordenada:
                    print("Calificacion {0}".format(elemento[-1]))
                  for i in range(len(mensajes_desglose)):
                    if i != 8:
                      print(mensajes_desglose[i].format(elemento[i]))
                    else:
                      print(mensajes_desglose[i])
                      for x in elemento[i]:
                        print(x) 
                  print("\n\n")
                

                "Código para reordenar la lista por categoría"

                # Se le pregunta al administrador si quiere ordenar la lista de acuerdo a la categoría.

                reordenar_por_categoria = ""
                while reordenar_por_categoria != "si" and reordenar_por_categoria != "no":

                  reordenar_por_categoria = input("¿Deseas reordenar la lista anterior por categorìa? (si/no)\n\n")

                  if reordenar_por_categoria != "si" and reordenar_por_categoria != "no":
                    print("+++++++++++++++++++++\n\nLo sentimos, esta opción no es válida. Intente de nuevo")

                if reordenar_por_categoria == "si":
                  
                  # Se genera una copia de la lista usada para protegerla
                  copia_lista_por_usar = []
                  for producto in opcion[2]:
                    lista = []
                    for elemento in producto:
                      lista.append(elemento)
                    copia_lista_por_usar.append(lista)
                  
                  # Código para reordenar la lista por categoría
                  lista_por_usar_categoria = []

                  while copia_lista_por_usar:
                    minimo = copia_lista_por_usar[0][3]
                    lista = copia_lista_por_usar[0]
                    for i in range(len(copia_lista_por_usar)):
                      if minimo > copia_lista_por_usar[i][3]:
                        minimo = copia_lista_por_usar[i][3]
                        lista = copia_lista_por_usar[i]
                    lista_por_usar_categoria.append(lista)
                    copia_lista_por_usar.remove(lista)

                  print("+++++++++++++++++++++\n\nEstos son los productos ordenados por categoría") 
                  
                  categorias_mostradas = []
                  for elemento in lista_por_usar_categoria:
                    categoria = elemento[3]
                    if categoria not in categorias_mostradas:
                      categorias_mostradas.append(categoria)
                      print("+++++ {0} +++++\n".format(categoria))

                    #print("Posición: {0}".format(posicion))
                    
                    # Si es la lista que contiene las calificaciones utilizando la métrica se añade la calificación. Es el único caso especial de este tipo de lista
                    if lista_por_usar_categoria == productos_expandidos_calif_ordenada:
                      print("Calificacion {0}".format(elemento[-1]))
                    for i in range(len(mensajes_desglose)):
                      if i != 8:
                        print(mensajes_desglose[i].format(elemento[i]))
                      else:
                        print(mensajes_desglose[i])
                        for x in elemento[i]:
                          print(x) 
                    print("\n\n") 
 

                # Código para que el administrador indique qué es lo que quiere hacer.
                entrada_navegacion_admin = ""
                entradas_validas = ["menu administrador", "menu principal", "inicio", "cerrar"]

                while entrada_navegacion_admin not in entradas_validas:
                  
                  entrada_navegacion_admin = input("Si quieres volver al menu del administrador, teclea: menu administrador.\nSi quieres volver al menú principal, teclea: menu principal.\nSi quieres volver a la pantalla de inicio, teclea: inicio\nSi quieres cerrar el programa teclea: cerrar\n\n")

                if entrada_navegacion_admin == "menu administrador":
                  menu_administrador = True
                elif entrada_navegacion_admin == "menu principal":
                  menu = True
                elif entrada_navegacion_admin == "inicio":
                  pantalla_de_inicio = True
                elif entrada_navegacion_admin == "cerrar":
                  terminar_programa = True        


              # El tipo 3 de listas es el más complicado, pues su formato de sus elementos es de la siguiente manera:
              # [año, mes, [[...], [...], ..., [...]] ]
              elif tipo_lista == 3:
                
                # Se muestra un nuevo menu donde el administrador puede escoger de qué mes quiere revisar la información

                # Se crea la variable sel_meses para que se muestre el menú
                sel_meses = True
                while sel_meses:
                  # Se cambia la variable a False para evitar loops infinitos.
                  sel_meses = False

                  # Se muestran las opciones.
                  print('''
                  ++++++++++++++++++++++++++++++++++++ 
                  
                  Estos son los meses para los que se tienen datos:

                  ''')

                  for i in range(len(meses_anios_str_ordenada)):
                    print(str(i+1), "Año: {0}".format(meses_anios_str_ordenada[i][0]), "Mes: {0}".format(meses_anios_str_ordenada[i][1]))

                  # Se le pide al administrador que ingrese la opción que deseé.
                  seleccion = ''
                  selecciones_validas = []
                  for i in range(len(meses_anios_str_ordenada)):
                    selecciones_validas.append(str(i+1))

                  # El administrador ahora también puede volver a la pantalla del menú del administrador, además de las otras opciones recurrerntes.
                  opciones_navegacion_admin = ["inicio", "cerrar", "menu principal", "menu administrador"]

                  # Código si se ingresa una entrada no válida.
                  while seleccion not in selecciones_validas and seleccion not in opciones_navegacion_admin:
                    
                    seleccion = input("\nElige el numero de la opción que quieras revisar.\nSi quieres volver al menu del administrador, teclea: menu administrador.\nSi quieres volver al menú principal, teclea: menu principal.\nSi quieres volver a la pantalla de inicio, teclea: inicio\nSi quieres cerrar el programa teclea: cerrar\n\n")

                    if seleccion not in selecciones_validas and seleccion not in opciones_navegacion_admin:
                      print("++++++++++++++++++++\n\nLo sentimos, esta no es una opción válida.\nIntenta de nuevo.")

                  # Si se selecciona una opción de navegación se regresa al nivel de exploración requerido.
                  if seleccion in opciones_navegacion_admin:
                    if seleccion == "cerrar":
                      terminar_programa = True
                      break
                    elif seleccion == 'inicio':
                      pantalla_de_inicio = True
                      break
                    elif seleccion == "menu principal":
                      menu = True
                      break
                    elif seleccion == "menu administrador":
                      menu_administrador = True
                      break

                  # Si la seleccion es válida se muestran los datos del mes.
                  elif seleccion in selecciones_validas:
                    lista_mes = opcion[2][int(seleccion) - 1]

                    # Mensajes a desglosar
                    mensajes_desglose_mes = ["Id del producto: {0}", "Nombre del producto: {0}", "Precio MXN: {0}", "Categoria: {0}", "Número de compras: {0}", "Calificación promedio: {0}", "Número de devoluciones: {0}"]

                    print("+++++++++++++++++++++\n\n")

                    palabras = "más comprados"
                    if opcion[2] == analisis_mensual_calif:
                      palabras = "con mejores reseñas"

                    print("En esta lista se muestran los productos {0} en:\n\n".format(palabras))  

                    print("Año: {0}".format(lista_mes[0]))
                    print("Mes: {0}\n".format(lista_mes[1]))

                    # Presentación de los datos
                    lista_a_usar = lista_mes[2]

                    posicion = 0
                    for elemento in lista_a_usar:
                      posicion += 1
                      print("Posición: {0}".format(posicion))
                      for i in range(len(mensajes_desglose_mes)):
                        print(mensajes_desglose_mes[i].format(elemento[i]))

                      print("\n\n")

                    # Código para que el administrador indique qué es lo que quiere hacer, puede seleccionar un nuevo, mes, volver al menu de admiistrador, al menú principal, a la pantalla de inicio o cerrar el programa.

                    entradas_validas = ["inicio", "cerrar", "menu principal", "menu administrador", "seleccionar mes"]

                    entrada = ''

                    while entrada not in entradas_validas:
                      entrada = input("\nSi quieres revisar otro mes teclea: seleccionar mes.\nSi quieres volver al menu del administrador teclea: menu administrador.\nSi quieres volver al menú principal teclea: menu principal.\n Si quieres volver a la pantalla de inicio teclea: inicio.\nSi quieres cerrar el programa teclea: cerrar\n\n")


                    if entrada == 'seleccionar mes':
                      sel_meses = True

                    elif entrada == 'menu administrador':
                      menu_administrador = True
                      break
                    elif entrada == 'menu principal':
                      menu = True
                      break
                    elif entrada == 'inicio':
                      pantalla_de_inicio = True
                      break
                    elif entrada == 'cerrar':
                      terminar_programa = True 
                      break

              else:
                print("Hubo un error")
                  
    
    
  # Si la variable terminar programa es True, se muestra un mensaje de salida y termina el ciclo while, terminando el programa.
  if terminar_programa:
    print(mensaje_despedida)
    break

  






"-----------------------------------------------------"


