import os, sys
# Добавляем корень репозитория в sys.path чтобы импортировался пакет app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
