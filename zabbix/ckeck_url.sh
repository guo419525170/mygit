#!/bin/bash
curl=/usr/bin/curl
cmscode=`curl -o /dev/null --connect-timeout 10 -s -w %{http_code} -H "Host: hengyang-cms.jtcfgame.com" hengyang-cms.jtcfgame.com/html/index.html`
managercode=`$curl -o /dev/null --connect-timeout 10 -s -w %{http_code} -H "Host: hengyang-manager.jtcfgame.com" hengyang-manager.jtcfgame.com/html/index.html`
membercode=`$curl -o /dev/null --connect-timeout 10 -s -w %{http_code} -H "Host: hengyang-member.jtcfgame.com" hengyang-member.jtcfgame.com/html/index.html`
citycode=`$curl -o /dev/null --connect-timeout 10 -s -w %{http_code} -H "Host: hengyang-city.jtcfgame.com" hengyang-city.jtcfgame.com/html/index.html`
####判断访问是否正常，持续3秒
if [ $cmscode -ne 200 ];
then
sleep 3
elif [ $managercode -ne 200 ];
then
sleep 3
elif [ $membercode -ne 200 ];
then
sleep 3
elif [ $citycode -ne 200 ];
then
sleep 3
fi

if [ $cmscode -eq 200 ] && [ $managercode -eq 200 ] && [ $membercode -eq 200 ] && [ $citycode -eq 200 ];
   then
     echo 200
  else
echo 502
fi
