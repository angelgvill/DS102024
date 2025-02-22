import snappy

print("python-snappy está instalado correctamente.")

try:
    data = b"Esto es una prueba de snappy."
    compressed = snappy.compress(data)
    decompressed = snappy.decompress(compressed)

    if decompressed == data:
        print("La compresión y descompresión con snappy funcionan correctamente.")
    else:
        print("Error: Los datos descomprimidos no coinciden con los datos originales.")

except Exception as e:
    print(f"Error al usar snappy: {e}")