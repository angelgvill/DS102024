import sys
from pathlib import Path

class AutoImporter:
    def __init__(self, base_dir=None):
        """
        Inicializa la clase AutoImporter y añade automáticamente
        todos los subdirectorios de `base_dir` al sys.path.

        :param base_dir: Directorio base desde donde buscar subdirectorios.
                         Si no se especifica, utiliza el directorio actual (Path.cwd()).
        """
        self.base_dir = Path(base_dir) if base_dir else Path.cwd()
        self._add_subdirectories_to_sys_path()

    def _add_subdirectories_to_sys_path(self):
        """
        Añade todos los subdirectorios de `self.base_dir` a sys.path.
        """
        for subdir in self.base_dir.rglob('*'):
            if subdir.is_dir() and str(subdir) not in sys.path:
                sys.path.append(str(subdir))

# Ejemplo de uso
#if __name__ == "__main__":
    # Instancia la clase AutoImporter con el directorio actual
    #importer = AutoImporter()

    # O puedes especificar un directorio base explícito
    # importer = AutoImporter("/ruta/a/tu/directorio")

    # Ahora puedes importar módulos desde cualquier subdirectorio
