import subprocess

def ejecutar_script(script):
    try:
        subprocess.run(['python', script], check=True)
        print(f"El script {script} se ejecutó correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script {script}: {e}")

scripts = ['rutas.py', 'incremento2.py', 'exportar_tablas.py', 'importar_registros.py']

for script in scripts:
    ejecutar_script(script)