#!/usr/bin/env python

#-*-coding:utf-8-*-

import socket

import subprocess

import sys

from datetime import datetime

subprocess.call('clear', shell=True)#Ekranı Temizle

try:

    remoteServer    = raw_input("Tarama yapılacak siteyi veya İp Adresini Giriniz: ")# Girdi Al

    remoteServerIP  = socket.gethostbyname(remoteServer)

    # Taramayla ilgili bilgi veriliyor hangi ip'yi taradığımızı gösteriyor...

    print "-" * 60

    print "Lütfen bekleyiniz,tarama yapılıyor...", remoteServerIP

    print "-" * 60

    t1 = datetime.now()#Taramaya başladığındaki zamanı alıyoruz...

    try:

        for port in range(1,1024):#Portları 1-1023'e kadar tarıyoruz..

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            result = sock.connect_ex((remoteServerIP, port))

            if result == 0:

                print "Port {}: 	 Açık".format(port)            sock.close()

    #Bu exceptleri koymamızın sebebi programın kırılmasını önlüyoruz.

    except KeyboardInterrupt:#Ctrl+c basıp basmadığımızı kontrol ediyoruz.

        print "Ctrl+C'ye bastınız..."

        sys.exit()#program sonlandırılıyor..

    except socket.error:#Servera bağlanıp bağlanılmadığını kontrol ediyoruz.

        print "Server'a bağlanılamadı."

        sys.exit()

    t2 = datetime.now()# İkinci kere zaman alınıyor.

    total =  t2 - t1 #Tarama işleminin ne kadar sürdüğünü buluyoruz.

    # Bilgiler Ekrana basılıyor..

    print ("Tarama:{} sürede tamamlandı".format(total))

except socket.gaierror:

    sys.stderr.write("Girilen Değer {} uygun formatta değil!!!!\n".format(remoteServer))
    
       
      
       
        
       
            
      
       
   
