list1=`netstat -nat|grep -i "16010"|wc -l`
list2=`netstat -nat|grep -i "16011"|wc -l`
list3=`netstat -nat|grep -i "16012"|wc -l`
list4=`netstat -nat|grep -i "16013"|wc -l`
list5=`netstat -nat|grep -i "16014"|wc -l`
list6=`netstat -nat|grep -i "16015"|wc -l`
list7=`netstat -nat|grep -i "16017"|wc -l`
list8=`netstat -nat|grep -i "16018"|wc -l`
list9=`netstat -nat|grep -i "16019"|wc -l`
echo $(($list1+$list2+list3+list4+list5+list6+list7+list8+list9))
