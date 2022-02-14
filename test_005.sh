#!/bin/bash
if [[ $(ssh root@192.168.0.200 "df -h | grep /dev/sdb1" | awk '{print $5}') > 85% ]]
then
echo -e 'Subject:Backup\n\nОсталось мало памяти\nНужно произвести чистку сервера' | sendmail -v 107@maverik.ru > /dev/null 2>&1
fi
