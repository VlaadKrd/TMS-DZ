Создать pipeline для деплоя микросервисов приложения simple-java-project:

должен запускаться в случае успешного завершения пайплайна сборки;
должен выполнять параллельный деплой микросервисов;
в качестве деплоя можно просто запустить контейнеры на Jenkins мастере (агенте), т.к. пуш образов в репозиторий еще не разбирали.