# Guía para manejar Notebooks en GitHub

## Configuración inicial (una sola vez)

### Con GitHub Desktop (Recomendado 👍)
1. Hacer fork del repositorio del profesor
2. Abrir GitHub Desktop
3. Clonar tu fork: `File > Clone repository`
4. Agregar repo del profesor como "upstream":
   - `Repository > Repository settings > Remote > Add`
   - Nombre: `upstream`
   - URL: la del repositorio del profesor

### Si prefieres VS Code
1. Hacer fork del repositorio
2. Instalar la extensión "Jupyter" en VS Code
3. Clonar tu fork
4. Agregar el upstream (repo del profesor):
   ```bash
   git remote add upstream https://github.com/PROFESOR/REPO.git
   ```

## Workflow diario recomendado

### 1. Antes de empezar a trabajar
- Abrir GitHub Desktop
- Fetch y Pull desde upstream para tener los últimos cambios del profesor
- Si hay conflictos, resolverlos primero

### 2. Al trabajar con los notebooks
- Guardar frecuentemente (Ctrl+S o ⌘+S)
- Ejecutar las celdas en orden
- Si modificas algo del profesor, mejor duplica la celda y modifica la copia

### 3. Antes de hacer commit
- Guardar el notebook
- Ejecutar "Restart & Run All" para verificar que todo funcione
- Hacer commit y push a tu fork

## Resolver conflictos en notebooks

### En GitHub Desktop (Más fácil)
1. Cuando aparezca un conflicto:
   - GitHub Desktop te avisará
   - Click en "Open in Visual Studio Code"
2. En VS Code verás algo así:
   ```
   <<<<<<< HEAD
   # Tu código
   =======
   # Código del profesor
   >>>>>>> upstream/main
   ```
3. Elegir qué mantener:
   - Puedes quedarte con tu código
   - O con el del profesor
   - O mezclar ambos
4. Guardar y hacer commit

### Tip importante 💡
Si el conflicto es muy complejo:
1. Guarda tu notebook con otro nombre
2. Acepta los cambios del profesor
3. Copia y pega tu código celda por celda
4. Así mantienes una copia de seguridad por si acaso

## Problemas comunes

### "No puedo hacer push al upstream"
- Es normal, porque ese es el repo del profesor
- Asegúrate de hacer push a tu fork (origin)

### "Your branch is behind"
- Significa que el profesor subió cambios nuevos
- Usa GitHub Desktop para hacer fetch y merge del upstream

### El notebook no funciona después de un merge
1. Guarda una copia de tu trabajo
2. Acepta los cambios del profesor
3. Vuelve a agregar tus cambios poco a poco
4. Ejecuta todo para verificar que funcione

## Consejos para evitar problemas
1. **SIEMPRE** actualiza desde upstream antes de empezar
2. Haz commits frecuentes con mensajes claros
3. Si vas a modificar código del profesor, duplica la celda
4. Mantén backups de tus cambios importantes
5. Si tienes dudas, pregunta al profesor antes de hacer cambios grandes

## Secuencia para actualizar desde el profesor

### En GitHub Desktop
1. Fetch from upstream
2. Merge upstream into main
3. Resolver conflictos si aparecen
4. Push to origin

### En VS Code
```bash
git fetch upstream
git merge upstream/main
# Resolver conflictos si hay
git push
```
