# test_android_calc
автотест appiup+python

Перед запуском необходимо загрузить все библиотеки из requirements.txt:

pip install -r requirements.txt

Для запуска из терминала:

pytest -v --apk=<путь до apk> --android_version=<версия вашей OS Android> test_android.py

ВАЖНО! Путь до APK не должен содержать пробелов а если пробелы все же есть, 
ту путь необходимо передать в кавычках

