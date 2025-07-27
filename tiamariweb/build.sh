#!/usr/bin/env bash

# Migraciones de base de datos
python manage.py migrate

# Crear superusuario automáticamente (opcional y más avanzado — mejor hacerlo manualmente si puedes)
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell
