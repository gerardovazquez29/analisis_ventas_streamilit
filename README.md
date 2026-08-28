📊 Dashboard de Ventas
Dashboard interactivo para visualizar ventas por producto, región y tiempo. Construido con Streamlit, Pandas y Plotly Express.

Python Streamlit License

 Demo
Agrega aquí una captura de pantalla o GIF del dashboard funcionando.
<img width="1872" height="985" alt="imagen" src="https://github.com/user-attachments/assets/47162084-7d35-437d-bf49-676695c77014" />



 Características
KPIs principales: ingreso total, unidades vendidas y ticket promedio
Filtros interactivos por región y producto
Gráfico de línea con la tendencia de ingresos por día
Gráfico de barras con el ingreso por producto
Gráfico de pastel con la participación por región
Tabla de detalle con todas las transacciones filtradas

 Tecnologías
Herramienta	Uso
Streamlit	Interfaz web del dashboard
Pandas	Carga, limpieza y agrupación de datos
Plotly Express	Gráficos interactivos

 Estructura del proyecto
data_science/
├── dasboard.py         # Código principal del dashboard
├── ventas.csv           # Dataset de ventas
├── requirements.txt     # Dependencias del proyecto
└── README.md

 Instalación
Clona el repositorio:

git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO

Crea y activa un entorno virtual:

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

Instala las dependencias:

pip install -r requirements.txt

 Uso
Corre la aplicación localmente:

streamlit run dasboard.py

Se abrirá automáticamente en http://localhost:8501.

Compartir el dashboard fuera de tu red local (opcional)
Puedes exponerlo temporalmente a internet usando ngrok:

ngrok http 8501

Esto genera una URL pública temporal (ej. https://xxxx.ngrok-free.dev) que puedes compartir mientras el túnel esté activo.

 Datos
El archivo ventas.csv contiene las columnas:

Columna	Descripción
fecha	Fecha de la venta
producto	Nombre del producto vendido
region	Región donde se realizó la venta
precio	Precio unitario
vendidos	Unidades vendidas
ingreso_total	precio × vendidos

 Próximas mejoras
 Filtro por rango de fechas
 Exportar reporte filtrado a Excel/PDF
 Conexión a base de datos en vez de CSV estático
 Despliegue permanente (Streamlit Community Cloud)


 Autor
Santiago
