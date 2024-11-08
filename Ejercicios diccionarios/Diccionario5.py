notas = {
 'Matemáticas': 7,
 'Física': 8,
 'Historia': 9
}
minimo=10
for asignatura,nota in notas.items():
    if nota < minimo:
        asignatura_min=asignatura
print(f'{asignatura_min}')