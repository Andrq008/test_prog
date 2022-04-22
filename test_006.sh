#!/bin/bash
if [[ ! $(df -h | grep -wo /dev/shm) ]]
then
 echo -e 'Subject:MINT\n\nРазмонтировался 111\nБыла попытка монтировать обратно' | sendmail -v 107@maverik.ru > /dev/null 2>&1
elif [[ ! $(df -h | grep -wo /boot/efi) ]]
then
 mount /dev/sda1 /boot/efi
 echo -e 'Subject:MINT\n\nРазмонтировался 222\nБыла попытка монтировать обратно' | sendmail -v 107@maverik.ru > /dev/null 2>&1
elif [[ ! $(df -h | grep -wo /run/lock) ]]
then
 echo -e 'Subject:MINT\n\nРазмонтировался 333\nБыла попытка монтировать обратно' | sendmail -v 107@maverik.ru > /dev/null 2>&1
fi
if [[ $(df -h | grep /dev/sda5 | awk '{print $5}') > 64% ]]
then
 mem_space=$(df -h | grep /dev/sda5 | awk '{print $4}')
 echo -e "Subject:Mint\n\nОсталось $mem_space памяти /dev/sda5\nНужно произвести чистку сервера" | sendmail -v 107@maverik.ru > /dev/null 2>&1
fi
if [[ $(du -sh /root/) > 995 ]]
then
 echo -e "Subject:Mint\n\nКаталог занимает много памяти\nНужно произвести чистку" | sendmail -v 107@maverik.ru > /dev/null 2>&1
fi
