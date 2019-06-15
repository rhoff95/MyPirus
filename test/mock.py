def get_daily_mock():
    data = {
        '2019-06-14': {'1. open': '1089.7400', '2. high': '1094.7600', '3. low': '1081.4800', '4. close': '1086.3000',
                       '5. volume': '1226731'},
        '2019-06-13': {'1. open': '1084.7100', '2. high': '1096.5900', '3. low': '1082.5700', '4. close': '1091.0100',
                       '5. volume': '1040661'},
        '2019-06-12': {'1. open': '1079.9500', '2. high': '1082.5200', '3. low': '1069.6000', '4. close': '1079.1000',
                       '5. volume': '1183650'},
        '2019-06-11': {'1. open': '1096.9900', '2. high': '1104.0100', '3. low': '1079.5700', '4. close': '1081.0400',
                       '5. volume': '1675817'},
        '2019-06-10': {'1. open': '1077.0000', '2. high': '1094.8400', '3. low': '1075.2800', '4. close': '1082.7600',
                       '5. volume': '1425464'},
        '2019-06-07': {'1. open': '1054.2800', '2. high': '1073.4300', '3. low': '1051.1500', '4. close': '1068.3700',
                       '5. volume': '2191357'},
        '2019-06-06': {'1. open': '1046.2100', '2. high': '1050.0000', '3. low': '1035.5100', '4. close': '1047.7600',
                       '5. volume': '1451026'},
        '2019-06-05': {'1. open': '1055.0000', '2. high': '1056.8100', '3. low': '1033.0000', '4. close': '1044.6400',
                       '5. volume': '2349436'},
        '2019-06-04': {'1. open': '1044.4900', '2. high': '1058.4400', '3. low': '1036.0300', '4. close': '1054.4900',
                       '5. volume': '3025564'},
        '2019-06-03': {'1. open': '1066.9300', '2. high': '1067.0000', '3. low': '1027.0300', '4. close': '1038.7400',
                       '5. volume': '4844480'},
        '2019-05-31': {'1. open': '1105.6400', '2. high': '1113.4000', '3. low': '1103.3500', '4. close': '1106.5000',
                       '5. volume': '1579481'},
        '2019-05-30': {'1. open': '1120.1500', '2. high': '1126.8000', '3. low': '1115.9000', '4. close': '1121.4100',
                       '5. volume': '904419'},
        '2019-05-29': {'1. open': '1132.7000', '2. high': '1135.0000', '3. low': '1111.9500', '4. close': '1119.9400',
                       '5. volume': '1811510'},
        '2019-05-28': {'1. open': '1141.4800', '2. high': '1156.4900', '3. low': '1138.6700', '4. close': '1139.5600',
                       '5. volume': '1047554'},
        '2019-05-24': {'1. open': '1152.0000', '2. high': '1154.3600', '3. low': '1136.7100', '4. close': '1138.6100',
                       '5. volume': '927651'},
        '2019-05-23': {'1. open': '1146.0700', '2. high': '1150.0500', '3. low': '1133.1600', '4. close': '1145.3400',
                       '5. volume': '1260657'},
        '2019-05-22': {'1. open': '1151.2500', '2. high': '1163.7800', '3. low': '1151.0000', '4. close': '1155.8500',
                       '5. volume': '941279'},
        '2019-05-21': {'1. open': '1154.4800', '2. high': '1158.0000', '3. low': '1143.3100', '4. close': '1154.4400',
                       '5. volume': '1028248'},
        '2019-05-20': {'1. open': '1153.0000', '2. high': '1153.0000', '3. low': '1138.1300', '4. close': '1144.6600',
                       '5. volume': '1530126'},
        '2019-05-17': {'1. open': '1175.8300', '2. high': '1186.2900', '3. low': '1166.4200', '4. close': '1168.7800',
                       '5. volume': '1268050'},
        '2019-05-16': {'1. open': '1171.8400', '2. high': '1194.1600', '3. low': '1168.4500', '4. close': '1184.5000',
                       '5. volume': '1765388'},
        '2019-05-15': {'1. open': '1122.5500', '2. high': '1178.3000', '3. low': '1121.4000', '4. close': '1170.8000',
                       '5. volume': '2965117'},
        '2019-05-14': {'1. open': '1142.3200', '2. high': '1144.8700', '3. low': '1123.5300', '4. close': '1124.8600',
                       '5. volume': '2019550'},
        '2019-05-13': {'1. open': '1145.2400', '2. high': '1151.9700', '3. low': '1125.5000', '4. close': '1136.5900',
                       '5. volume': '2281686'},
        '2019-05-10': {'1. open': '1168.8400', '2. high': '1176.2800', '3. low': '1146.3700', '4. close': '1167.6400',
                       '5. volume': '1582460'},
        '2019-05-09': {'1. open': '1162.6000', '2. high': '1174.0700', '3. low': '1154.6400', '4. close': '1167.9700',
                       '5. volume': '1477752'},
        '2019-05-08': {'1. open': '1177.2900', '2. high': '1184.2700', '3. low': '1167.6300', '4. close': '1170.7800',
                       '5. volume': '1276022'},
        '2019-05-07': {'1. open': '1185.8100', '2. high': '1194.7700', '3. low': '1165.0000', '4. close': '1178.8600',
                       '5. volume': '1830238'},
        '2019-05-06': {'1. open': '1172.0000', '2. high': '1195.4300', '3. low': '1171.1500', '4. close': '1193.4600',
                       '5. volume': '1588684'},
        '2019-05-03': {'1. open': '1177.4100', '2. high': '1191.4000', '3. low': '1173.5500', '4. close': '1189.5500',
                       '5. volume': '2079376'},
        '2019-05-02': {'1. open': '1172.6000', '2. high': '1179.3800', '3. low': '1158.3300', '4. close': '1166.5100',
                       '5. volume': '2254890'},
        '2019-05-01': {'1. open': '1197.5000', '2. high': '1199.2500', '3. low': '1171.6700', '4. close': '1173.3200',
                       '5. volume': '3717018'},
        '2019-04-30': {'1. open': '1190.6300', '2. high': '1200.9800', '3. low': '1183.0000', '4. close': '1198.9600',
                       '5. volume': '6658855'},
        '2019-04-29': {'1. open': '1280.5100', '2. high': '1296.9700', '3. low': '1271.7100', '4. close': '1296.2000',
                       '5. volume': '3618362'},
        '2019-04-26': {'1. open': '1273.3800', '2. high': '1278.9100', '3. low': '1265.0000', '4. close': '1277.4200',
                       '5. volume': '1361419'},
        '2019-04-25': {'1. open': '1270.3000', '2. high': '1272.8000', '3. low': '1258.0000', '4. close': '1267.3400',
                       '5. volume': '1567161'},
        '2019-04-24': {'1. open': '1270.5900', '2. high': '1274.0000', '3. low': '1259.8100', '4. close': '1260.0500',
                       '5. volume': '1169797'},
        '2019-04-23': {'1. open': '1256.6400', '2. high': '1274.4300', '3. low': '1251.9700', '4. close': '1270.5900',
                       '5. volume': '1593449'},
        '2019-04-22': {'1. open': '1236.6700', '2. high': '1254.3400', '3. low': '1233.3700', '4. close': '1253.7600',
                       '5. volume': '954419'},
        '2019-04-18': {'1. open': '1245.0000', '2. high': '1245.9400', '3. low': '1239.4100', '4. close': '1241.4700',
                       '5. volume': '1237788'},
        '2019-04-17': {'1. open': '1237.0000', '2. high': '1245.1000', '3. low': '1232.9000', '4. close': '1240.1400',
                       '5. volume': '1518286'},
        '2019-04-16': {'1. open': '1230.0000', '2. high': '1235.9800', '3. low': '1225.0400', '4. close': '1231.9100',
                       '5. volume': '1131099'},
        '2019-04-15': {'1. open': '1224.0900', '2. high': '1229.3000', '3. low': '1214.5600', '4. close': '1226.5300',
                       '5. volume': '1189974'},
        '2019-04-12': {'1. open': '1215.6200', '2. high': '1223.0500', '3. low': '1213.2900', '4. close': '1222.7300',
                       '5. volume': '1215610'},
        '2019-04-11': {'1. open': '1208.9000', '2. high': '1212.7400', '3. low': '1204.5400', '4. close': '1209.5900',
                       '5. volume': '849947'},
        '2019-04-10': {'1. open': '1205.0900', '2. high': '1208.9400', '3. low': '1200.6600', '4. close': '1206.4500',
                       '5. volume': '775456'},
        '2019-04-09': {'1. open': '1201.8900', '2. high': '1207.1500', '3. low': '1198.3800', '4. close': '1202.6900',
                       '5. volume': '983840'},
        '2019-04-08': {'1. open': '1211.1100', '2. high': '1213.9500', '3. low': '1204.6900', '4. close': '1208.2800',
                       '5. volume': '1087588'},
        '2019-04-05': {'1. open': '1219.3000', '2. high': '1220.3900', '3. low': '1210.0300', '4. close': '1211.4500',
                       '5. volume': '1001044'},
        '2019-04-04': {'1. open': '1211.2900', '2. high': '1220.5500', '3. low': '1209.0400', '4. close': '1219.4500',
                       '5. volume': '1051089'},
        '2019-04-03': {'1. open': '1212.7000', '2. high': '1220.6000', '3. low': '1205.0800', '4. close': '1210.8100',
                       '5. volume': '1109614'},
        '2019-04-02': {'1. open': '1200.0500', '2. high': '1205.8100', '3. low': '1191.2400', '4. close': '1205.5400',
                       '5. volume': '914413'},
        '2019-04-01': {'1. open': '1187.5400', '2. high': '1200.2000', '3. low': '1186.3600', '4. close': '1198.9800',
                       '5. volume': '1385595'},
        '2019-03-29': {'1. open': '1180.1800', '2. high': '1183.9700', '3. low': '1166.3800', '4. close': '1176.8900',
                       '5. volume': '1544615'},
        '2019-03-28': {'1. open': '1175.5000', '2. high': '1177.2500', '3. low': '1163.4300', '4. close': '1172.2700',
                       '5. volume': '1120122'},
        '2019-03-27': {'1. open': '1191.9200', '2. high': '1191.9200', '3. low': '1164.2300', '4. close': '1178.0100',
                       '5. volume': '1471402'},
        '2019-03-26': {'1. open': '1205.1900', '2. high': '1207.6500', '3. low': '1181.7600', '4. close': '1189.8400',
                       '5. volume': '1537606'},
        '2019-03-25': {'1. open': '1199.5600', '2. high': '1209.4400', '3. low': '1190.0000', '4. close': '1197.3800',
                       '5. volume': '1378849'},
        '2019-03-22': {'1. open': '1228.8500', '2. high': '1233.6300', '3. low': '1206.0000', '4. close': '1207.6500',
                       '5. volume': '1721133'},
        '2019-03-21': {'1. open': '1220.0000', '2. high': '1236.4400', '3. low': '1216.5800', '4. close': '1236.1300',
                       '5. volume': '1407480'},
        '2019-03-20': {'1. open': '1201.4000', '2. high': '1229.9900', '3. low': '1199.5900', '4. close': '1226.4300',
                       '5. volume': '2075442'},
        '2019-03-19': {'1. open': '1191.7200', '2. high': '1203.4000', '3. low': '1189.4600', '4. close': '1202.4600',
                       '5. volume': '1489407'},
        '2019-03-18': {'1. open': '1189.6900', '2. high': '1194.9500', '3. low': '1181.4800', '4. close': '1188.5500',
                       '5. volume': '1222203'},
        '2019-03-15': {'1. open': '1198.0000', '2. high': '1201.7200', '3. low': '1187.0100', '4. close': '1190.3000',
                       '5. volume': '2593338'},
        '2019-03-14': {'1. open': '1199.0200', '2. high': '1204.7000', '3. low': '1191.2300', '4. close': '1192.5300',
                       '5. volume': '1365072'},
        '2019-03-13': {'1. open': '1205.9300', '2. high': '1207.1200', '3. low': '1197.9100', '4. close': '1199.0600',
                       '5. volume': '1294354'},
        '2019-03-12': {'1. open': '1182.3000', '2. high': '1205.7100', '3. low': '1182.3000', '4. close': '1197.2500',
                       '5. volume': '2110979'},
        '2019-03-11': {'1. open': '1152.0000', '2. high': '1179.9100', '3. low': '1151.5700', '4. close': '1179.2600',
                       '5. volume': '1501633'},
        '2019-03-08': {'1. open': '1133.9000', '2. high': '1153.4500', '3. low': '1130.2000', '4. close': '1149.9700',
                       '5. volume': '1184732'},
        '2019-03-07': {'1. open': '1160.5000', '2. high': '1163.5800', '3. low': '1141.7100', '4. close': '1150.8500',
                       '5. volume': '1504328'},
        '2019-03-06': {'1. open': '1171.7600', '2. high': '1174.7400', '3. low': '1163.0500', '4. close': '1164.9400',
                       '5. volume': '1180052'},
        '2019-03-05': {'1. open': '1156.0000', '2. high': '1176.4900', '3. low': '1153.0200', '4. close': '1169.1900',
                       '5. volume': '2004723'},
        '2019-03-04': {'1. open': '1154.5600', '2. high': '1165.5200', '3. low': '1138.2500', '4. close': '1153.4200',
                       '5. volume': '1774467'},
        '2019-03-01': {'1. open': '1131.0000', '2. high': '1150.0000', '3. low': '1131.0000', '4. close': '1148.5200',
                       '5. volume': '1704258'},
        '2019-02-28': {'1. open': '1119.0000', '2. high': '1133.9900', '3. low': '1118.4100', '4. close': '1126.5500',
                       '5. volume': '1371355'},
        '2019-02-27': {'1. open': '1114.0100', '2. high': '1125.7300', '3. low': '1108.5600', '4. close': '1122.8900',
                       '5. volume': '1104881'},
        '2019-02-26': {'1. open': '1114.3700', '2. high': '1126.4300', '3. low': '1106.7000', '4. close': '1122.0100',
                       '5. volume': '1751261'},
        '2019-02-25': {'1. open': '1121.9300', '2. high': '1125.4000', '3. low': '1114.1100', '4. close': '1117.3300',
                       '5. volume': '1310362'},
        '2019-02-22': {'1. open': '1109.7000', '2. high': '1117.2500', '3. low': '1100.5000', '4. close': '1116.5600',
                       '5. volume': '1471783'},
        '2019-02-21': {'1. open': '1118.7800', '2. high': '1119.1500', '3. low': '1097.9800', '4. close': '1104.2100',
                       '5. volume': '1663980'},
        '2019-02-20': {'1. open': '1128.8800', '2. high': '1130.9300', '3. low': '1111.7500', '4. close': '1120.5900',
                       '5. volume': '1204533'},
        '2019-02-19': {'1. open': '1116.6400', '2. high': '1129.6400', '3. low': '1116.6400', '4. close': '1126.5100',
                       '5. volume': '1099259'},
        '2019-02-15': {'1. open': '1139.3000', '2. high': '1139.3000', '3. low': '1116.7200', '4. close': '1119.6300',
                       '5. volume': '1391348'},
        '2019-02-14': {'1. open': '1125.0000', '2. high': '1136.1300', '3. low': '1117.0900', '4. close': '1129.2000',
                       '5. volume': '1055297'},
        '2019-02-13': {'1. open': '1133.0400', '2. high': '1142.8500', '3. low': '1126.0000', '4. close': '1128.6300',
                       '5. volume': '1402087'},
        '2019-02-12': {'1. open': '1111.0100', '2. high': '1132.8600', '3. low': '1111.0100', '4. close': '1127.5800',
                       '5. volume': '1751771'},
        '2019-02-11': {'1. open': '1103.7500', '2. high': '1113.4300', '3. low': '1100.0000', '4. close': '1102.1200',
                       '5. volume': '924881'},
        '2019-02-08': {'1. open': '1094.8800', '2. high': '1105.1000', '3. low': '1094.2400', '4. close': '1102.3800',
                       '5. volume': '1088327'},
        '2019-02-07': {'1. open': '1111.8200', '2. high': '1111.9900', '3. low': '1093.5900', '4. close': '1105.9100',
                       '5. volume': '1914877'},
        '2019-02-06': {'1. open': '1149.2700', '2. high': '1154.0000', '3. low': '1118.3600', '4. close': '1122.8900',
                       '5. volume': '2412820'},
        '2019-02-05': {'1. open': '1129.6300', '2. high': '1152.7700', '3. low': '1123.6000', '4. close': '1151.8700',
                       '5. volume': '4114790'},
        '2019-02-04': {'1. open': '1119.0100', '2. high': '1142.3400', '3. low': '1117.5100', '4. close': '1141.4200',
                       '5. volume': '3920591'},
        '2019-02-01': {'1. open': '1122.2900', '2. high': '1134.4000', '3. low': '1114.2500', '4. close': '1118.6200',
                       '5. volume': '1655813'},
        '2019-01-31': {'1. open': '1112.2400', '2. high': '1127.6700', '3. low': '1105.2500', '4. close': '1125.8900',
                       '5. volume': '2011572'},
        '2019-01-30': {'1. open': '1077.3600', '2. high': '1099.5200', '3. low': '1076.6400', '4. close': '1097.9900',
                       '5. volume': '1472647'},
        '2019-01-29': {'1. open': '1081.0400', '2. high': '1084.7300', '3. low': '1066.0200', '4. close': '1070.0600',
                       '5. volume': '985248'},
        '2019-01-28': {'1. open': '1090.0700', '2. high': '1093.3700', '3. low': '1074.6100', '4. close': '1079.8600',
                       '5. volume': '1466714'},
        '2019-01-25': {'1. open': '1094.2300', '2. high': '1103.3600', '3. low': '1091.8000', '4. close': '1101.5100',
                       '5. volume': '1163788'},
        '2019-01-24': {'1. open': '1082.5100', '2. high': '1088.0000', '3. low': '1070.0200', '4. close': '1084.0000',
                       '5. volume': '1455948'},
        '2019-01-23': {'1. open': '1086.8600', '2. high': '1092.9500', '3. low': '1067.5700', '4. close': '1084.4100',
                       '5. volume': '1259738'}}
    meta_data = {'1. Information': 'Daily Prices (open, high, low, close) and Volumes',
                 '2. Symbol': 'GOOGL',
                 '3. Last Refreshed': '2019-06-14',
                 '4. Output Size': 'Compact',
                 '5. Time Zone': 'US/Eastern'}

    return data, meta_data
