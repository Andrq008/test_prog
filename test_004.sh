#!/bin/bash
if [[ $(find /mnt/c/Users/seligenenko/port/ -type f -name 'gridnine*' -cmin +3 | wc -l) > 0 ]]
then
 echo 'find files'
 if [[ $(find /mnt/c/Users/seligenenko/port/ -type f -name 'gridnine*' -perm 0644) ]]
 then
  chmod 666 /mnt/c/Users/seligenenko/port/gridnine*
 else
  echo -e 'Subject:Test File\n\nФайлы найдены\nФайлы изменены\nФайлы не загрузились' | sendmail -v 107@maverik.ru
 fi
else
 echo 'no find'
fi