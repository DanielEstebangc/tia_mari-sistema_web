#!/usr/bin/env bash

# Instala las dependencias
pip install -r requirements.txt

# Aplica migraciones automáticamente
python manage.py migrate

# (Opcional) Puedes crear el superusuario con datos fijos si quieres
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell