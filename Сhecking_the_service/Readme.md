## Проверка работоспособности службы windows 

for windows 10

Задача кода - обнаружить остановку службы.

### Set
- Сhecking_service.py - основной код
- Сhecking_service_params.py - переменные и чтение ini
- Сhecking_service.ini - конфигурационный файл
- report.txt - создается в случае наступления события
   - неправильно указано имя службы
   - служба не запущена

##### Сhecking_service.ini 
* count_max - количество прогонов в случае, если сервис продолжает работать
* time_sleep - таймаут между прогонами, в секундах
* ser_name - наименование сервиса который отслеживаем

ser_name:  Службы -> Свойства службы -> Общее -> Имя службы

### Как работает
Настраиваем ini. В случае неверно указанного имени службы, код сообщит об ошибке в
файле report.txt. В случае если служба остановлена, код так же сообщит об этом и прекратит работу.
В случае если служба найдена и работает, то код прекратит свое выполнение когда исчерпает количество указанных вами попыток.