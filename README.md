# python-p1

Обновить pip

    python -m pip install --upgrade pip
    
Установка tensorflow
    
    pip install tensorflow

Если процессор не поддерживает AVX, то будет возникать ошибка
ImportError: DLL load failed: A dynamic link library (DLL) initialization routine failed. (Win 10) 
или ImportError: DLL load failed with error code -1073741795 (Win 7),
Тогда нужно устанавливать неофициальную сборку из репозитория
https://github.com/fo40225/tensorflow-windows-wheel

    pip install https://raw.githubusercontent.com/fo40225/tensorflow-windows-wheel/master/1.12.0/py36/CPU/sse2/tensorflow-1.12.0-cp36-cp36m-win_amd64.whl
    
Запуск tensorboard

    tensorboard --logdir=log_simple_graph --host=127.0.0.1
    
Создание дистрибутива пакета
    
    py -3 setup.py sdist

UNIX-подобных ОС

    python3 setup.py sdist
