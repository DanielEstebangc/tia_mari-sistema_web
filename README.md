# 📦 Sistema de Inventario y Pedidos - Tía Mari

Este es un sistema web desarrollado en Django para gestionar clientes, productos y pedidos de forma eficiente. Está diseñado para negocios que requieren llevar control de stock, registro de pedidos y flujo de entrega.

## 🚀 Funcionalidades principales

- Gestión de productos con stock disponible.
- Registro de pedidos con múltiples productos por pedido.
- Actualización automática del stock al realizar un pedido.
- Validación de stock antes de guardar.
- Vistas separadas para:
  - Lista de productos
  - Lista de clientes
  - Lista de pedidos
- Detalle de cada pedido con opción para cambiar su estado (Entregado / Cancelado).
- Devolución de stock al cancelar un pedido.
- Página de inicio con navegación intuitiva.

## 🛠️ Tecnologías usadas

- **Backend:** Django  
- **Frontend:** HTML5, Bootstrap 5  
- **Base de datos:** MySQL (compatible con PostgreSQL y SQLite)  
- **ORM:** Django ORM

## ⚙️ Instalación

```bash
# 1. Clona este repositorio:
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo

# 2. Crea y activa un entorno virtual:
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# 3. Instala las dependencias:
pip install -r requirements.txt

# 4. Configura tu base de datos en settings.py si no usas SQLite.

# 5. Aplica las migraciones:
python manage.py makemigrations
python manage.py migrate

# 6. Ejecuta el servidor:
python manage.py runserver
```
## 📂 Estructura básica del proyecto

```bash
tia_mari/
├── inventario/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
├── tia_mari/         # Configuración general del proyecto
├── manage.py
└── README.md
```
##📌 Próximas mejoras
Exportación de pedidos a PDF o Excel.

Historial de pedidos por cliente.

Sistema de usuarios y autenticación.

Dashboard con gráficas y estadísticas.

##💡 Créditos
Desarrollado por Daniel Esteban Galvis Cataño con 💙 usando Django.
