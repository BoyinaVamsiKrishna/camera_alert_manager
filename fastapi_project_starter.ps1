python -m venv .myvenv
.myvenv\Scripts\activate
pip install fastapi uvicorn redis
pip freeze > requirements.txt
New-Item -Path app -ItemType Directory
New-Item -Path app\__init__.py -ItemType File
New-Item -Path app\main.py -ItemType File
New-Item -Path app\config -ItemType Directory
New-Item -Path app\config\__init__.py -ItemType File
New-Item -Path app\routers -ItemType Directory
New-Item -Path app\routers\__init__.py -ItemType File
New-Item -Path app\schemas -ItemType Directory
New-Item -Path app\schemas\__init__.py -ItemType File
New-Item -Path app\models -ItemType Directory
New-Item -Path app\models\__init__.py -ItemType File
New-Item -Path app\config\redis_config.py -ItemType File
