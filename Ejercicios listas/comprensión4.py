import os
ficheros_python = [f for f in os.listdir('.') if f.endswith('.py') and f.startswith('c')]
print(ficheros_python)
