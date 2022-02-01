from src.blib import blib_init, Banner, Files

blib_init(out='out/', src='img/')
code = '9.116.116.1327.1327.768.788.1.0.0.316.127.143.1080.3840.764.764.1.0.0.512.116.116.240.120.764.764.1.1.90.512.116.116.240.120.644.764.1.1.90.512.116.116.240.120.524.764.1.1.90.512.116.116.240.120.884.764.1.1.90.512.116.116.240.120.1004.764.1.1.90.512.116.116.240.120.764.609.1.1.90.512.116.116.240.120.884.609.1.1.90.512.116.116.240.120.524.609.1.1.90.512.116.116.240.120.644.609.1.1.90.512.116.116.240.120.1004.609.1.1.90.512.116.116.240.120.1004.454.1.1.90.512.116.116.240.120.884.454.1.1.90.512.116.116.240.120.764.454.1.1.90.512.116.116.240.120.644.454.1.1.90.512.116.116.240.120.524.454.1.1.90.512.116.116.240.120.524.919.1.1.90.512.116.116.240.120.644.919.1.1.90.512.116.116.240.120.764.919.1.1.90.512.116.116.240.120.884.919.1.1.90.512.116.116.240.120.1004.919.1.1.90.512.116.116.240.120.1004.1074.1.1.90.512.116.116.240.120.884.1074.1.1.90.512.116.116.240.120.764.1074.1.1.90.512.116.116.240.120.644.1074.1.1.90.512.116.116.240.120.524.1074.1.1.90.424.143.116.120.120.579.684.1.0.0.424.143.116.120.120.698.684.1.0.0.424.143.116.120.120.818.684.1.0.0.424.143.116.120.120.938.684.1.0.0.424.143.116.120.120.938.526.1.0.0.424.143.116.120.120.819.526.1.0.0.424.143.116.120.120.699.526.1.0.0.424.143.116.120.120.579.526.1.0.0.424.143.116.120.120.457.526.1.0.0.424.143.116.120.120.457.684.1.0.0.424.143.116.120.120.457.841.1.0.0.424.143.116.120.120.457.996.1.0.0.424.143.116.120.120.578.996.1.0.0.424.143.116.120.120.699.996.1.0.0.424.143.116.120.120.818.996.1.0.0.424.143.116.120.120.938.996.1.0.0.424.143.116.120.120.1059.996.1.0.0.424.143.116.120.120.1059.840.1.0.0.424.143.116.120.120.938.840.1.0.0.424.143.116.120.120.818.840.1.0.0.424.143.116.120.120.698.840.1.0.0.424.143.116.120.120.578.840.1.0.0.424.143.116.120.120.1059.681.1.0.0.424.143.116.120.120.1059.525.1.0.0.424.143.116.120.120.1059.375.1.0.0.424.143.116.120.120.939.375.1.0.0.424.143.116.120.120.820.375.1.0.0.424.143.116.120.120.699.375.1.0.0.424.143.116.120.120.578.375.1.0.0.424.143.116.120.120.455.375.1.0.0.424.143.116.120.120.455.375.1.0.0.424.143.116.120.120.579.1147.1.0.0.424.143.116.120.120.699.1147.1.0.0.424.143.116.120.120.819.1147.1.0.0.424.143.116.120.120.939.1147.1.0.0.512.127.127.60.60.1186.764.1.0.0.512.127.127.60.60.1226.764.1.0.0.512.127.127.60.60.1266.764.1.0.0.512.127.127.60.60.1306.764.1.0.0.512.127.127.60.60.1346.764.1.0.0.512.127.127.60.60.1386.764.1.0.0.512.127.127.60.60.1426.764.1.0.0.512.127.127.60.60.1466.764.1.0.0.512.127.127.60.60.1186.704.1.0.0.512.127.127.60.60.1226.704.1.0.0.512.127.127.60.60.1266.704.1.0.0.512.127.127.60.60.1306.704.1.0.0.512.127.127.60.60.1346.704.1.0.0.512.127.127.60.60.1386.704.1.0.0.512.127.127.60.60.1426.704.1.0.0.512.127.127.60.60.1466.704.1.0.0.512.127.127.60.60.342.764.1.1.0.512.127.127.60.60.302.764.1.0.0.512.127.127.60.60.262.764.1.0.0.512.127.127.60.60.222.764.1.0.0.512.127.127.60.60.182.764.1.0.0.512.127.127.60.60.142.764.1.0.0.512.127.127.60.60.102.764.1.0.0.512.127.127.60.60.62.764.1.0.0.512.127.127.60.60.62.704.1.0.0.512.127.127.60.60.102.704.1.0.0.512.127.127.60.60.142.704.1.0.0.512.127.127.60.60.182.704.1.0.0.512.127.127.60.60.222.704.1.0.0.512.127.127.60.60.262.704.1.0.0.512.127.127.60.60.302.704.1.0.0.512.127.127.60.60.342.704.1.0.0'

b = Banner(code).rescale(0.5).crop(650, 500).save(Files.Format.PNG)