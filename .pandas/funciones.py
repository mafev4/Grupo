def promedio(na, nc):
    try:
        df = pd.read_csv(na)
        
        if nc not in df.columns:
            return "No existe la columna"

        return df[nc].mean()

    except Exception as e:
        return f"Error al procesar la columna"
    
def desviacion(nombre_archivo, nombre_columna):
    try:
        if nombre_archivo.endswith(".csv"):
            df = pd.read_csv(nombre_archivo)
        elif nombre_archivo.endswith(".xlsx") or nombre_archivo.endswith(".xls"):
            df = pd.read_excel(nombre_archivo)
        else:
            print("Formato de archivo no soportado.")
            return None
        
        if nombre_columna not in df.columns:
            print("No existe la columna")
            return None
        
        return df[nombre_columna].std()

    except FileNotFoundError:
        print("No se encontró el archivo.")
        return None
    
def percentil(na, nc):
    try:
        df = pd.read_csv(na)

        if nc not in df.columns:
            return "Error al procesar la columna"

        p25 = df[nc].quantile(0.25)
        p50 = df[nc].quantile(0.50)
        p75 = df[nc].quantile(0.75)

        return p25, p50, p75

    except Exception as e:
        return f"Error al procesar la columna"