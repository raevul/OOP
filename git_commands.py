Основные команды
git init
git add .
git commit -m 'comment'
git push origin master
git pull origin master
git branch name_of_branch

индекс - это промежуточная область

git init - .git - создает папку .git
git remote add name name_ssh - в name_ssh вводится ssh ключ
добавляет удаленный репозиторий который находиться на сервере(github) в мою локальный репозиторий
или же связываем удаленный репозиторий с локальной репозиторией
git pull origin master - стягиваем изменения из ветки master(или с какой либо ветки)
git status - показывает изменения
git add . - добавляет папки в индекс
git commit -m 'comment' - добавляет все папки которые находятся в индексе во внутреннюю базу данных
git push --set-upstream origin name_of_branch - пушит код в новую(созданную) ветку
git branch - менеджер веток, можно видеть список веток и выбрать нужную ветку
git branch name_of_branch - создает новую ветку с названием name_of_branch
git checkout name_of_branch - переключается на ветку с названием name_of_branch
git push name_of_branch (origin master) - отправляет код в удаленный репозиторий
git reset name_of_file - удаляет папку из индекса
git clone - клонирует папку из удаленной репозитории в локалку
gitignore - в гитигнор закидываем папки и файлы которые не хотим запушить например окружение, медиапапки, скрытые файлы
git log - история изменений
git merge - стягивает коммиты с одной ветки на другую
