# Ejemplos de uso de plot1d

## Instalación de dependencias

Primero asegúrate de tener matplotlib instalado:
```bash
pip install matplotlib
# O si usas hvplot:
pip install hvplot holoviews
```

## Uso básico

### 1. Plotear una variable en un tiempo específico (índice)
```bash
ncv plot1d archivo.nc h -t 0
```

### 2. Plotear múltiples variables
```bash
ncv plot1d archivo.nc h H -t 5
```

### 3. Usar fecha/hora en lugar de índice
```bash
ncv plot1d archivo.nc temp -t "2020-01-15"
ncv plot1d archivo.nc temp -t "2020-01-15 12:00:00"
```

## Operaciones entre variables

### 4. Plotear diferencia entre variables
```bash
ncv plot1d archivo.nc "h-H" -t 10
```

### 5. Plotear magnitud de velocidad
```bash
ncv plot1d archivo.nc "sqrt(u**2 + v**2)" -t 0
```

### 6. Combinar variables simples y operaciones
```bash
ncv plot1d archivo.nc h H "h-H" -t 0
```

## Guardar gráficos

### 7. Guardar como PNG
```bash
ncv plot1d archivo.nc h -t 0 -o plot.png
```

### 8. Guardar como PDF
```bash
ncv plot1d archivo.nc h H -t 5 -o results.pdf
```

### 9. Guardar como SVG (vectorial)
```bash
ncv plot1d archivo.nc "h-H" -t 10 -o figure.svg
```

## Usar hvplot en lugar de matplotlib

### 10. Plot interactivo con hvplot
```bash
ncv plot1d archivo.nc h -t 0 --hvplot
```

### 11. Plot interactivo guardado a HTML
```bash
ncv plot1d archivo.nc h H -t 0 --hvplot -o interactive.html
```

## Ejemplos avanzados

### 12. Plotear conversión de temperatura
```bash
ncv plot1d archivo.nc temp "temp-273.15" -t 0 -o temp_comparison.png
```

### 13. Plotear energía cinética
```bash
ncv plot1d archivo.nc "0.5*(u**2 + v**2)" -t 20 -o kinetic_energy.png
```

### 14. Múltiples operaciones complejas
```bash
ncv plot1d archivo.nc u v "sqrt(u**2 + v**2)" -t 0 --hvplot
```

## Notas

- **Dimensión espacial**: El comando detecta automáticamente qué dimensión usar para el eje X (lon, lat, x, depth, etc.)
- **Tiempo**: Puedes especificar el tiempo como:
  - Índice entero: `-t 0`, `-t 10`
  - Fecha: `-t "2020-01-01"`
  - Fecha y hora: `-t "2020-01-01 12:30:00"`
- **Múltiples variables**: Puedes plotear tantas como quieras en el mismo gráfico
- **Operaciones**: Usa comillas para expresiones con operadores: `"h-H"`, `"temp*2"`
- **Formato de salida**: matplotlib detecta automáticamente el formato por la extensión (.png, .pdf, .svg, etc.)
