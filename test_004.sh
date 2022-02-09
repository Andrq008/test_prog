#!/bin/bash
if [[ $(find /root/dfgdfg/ -type f -name 'gridnine*' -cmin +5 | wc -l) > 0 ]]
then
 echo 'find files'
 if [[ $(find /root/dfgdfg/ -type f -name 'gridnine*' -perm 0644) ]]
 then
  chmod 666 /root/dfgdfg/gridnine*
 else
  echo -e 'Subject:Test File\n\nФайлы найдены\nФайлы изменены\nФайлы не загрузились' | sendmail -v 107@maverik.ru
 fi
else
 echo 'no find'
fi
