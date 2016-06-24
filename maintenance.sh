#!/bin/bash
check_maintenance=`grep 'zqt-product-%' /usr/local/nginx/conf/nginx.conf|wc -l`
check_product=`grep 'zqt-maintenance-%' /usr/local/nginx/conf/nginx.conf|wc -l`

recover(){
   if [ $check_product == 1 ];then
      mv /usr/local/nginx/conf/nginx.conf /usr/local/nginx/conf/nginx.conf.maintenance_2016-06-24  
      mv /usr/local/nginx/conf/nginx.conf.hufu /usr/local/nginx/conf/nginx.conf 
      /etc/init.d/nginx configtest && /etc/init.d/nginx reload
   else
      echo "The nginx profile is error!"
      exit 0
   fi
}

maintenance(){
   if [ $check_maintenance == 1 ];then
      mv /usr/local/nginx/conf/nginx.conf /usr/local/nginx/conf/nginx.conf.hufu
      mv /usr/local/nginx/conf/nginx.conf.maintenance_2016-06-24  /usr/local/nginx/conf/nginx.conf
      /etc/init.d/nginx configtest && /etc/init.d/nginx reload
   else 
      echo "The nginx profile is error!"
      exit 0
   fi
}

case "$1" in
 recover)
        recover
        RETVAL=$?
        ;;
 maintenance)
        maintenance
        RETVAL=$?
        ;;
 *)
        echo $"Usage: $0 {recover|maintenance}"
        RETVAL=2
esac

exit $RETVAL
