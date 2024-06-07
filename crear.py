import psycopg2

host = "localhost"
database = "postgres"
user = "postgres"
password = "1802877"
port = 5432

def connect():
    return psycopg2.connect(dbname=database, user=user, password=password, host=host, port=port)

def create_televisor(serie, marca, nombre_cliente, apellido_cliente, numero_cedula):
    conn = connect()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO public.televisores (serie, marca, nombre_cliente, apellido_cliente, numero_cedula) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (serie, marca, nombre_cliente, apellido_cliente, numero_cedula))
        conn.commit()
        print("New television record inserted successfully.")
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def read_televisores():
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM public.televisores")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def find_televisor_by_serie(serie):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM public.televisores WHERE serie = %s", (serie,))
        row = cursor.fetchone()
        if row:
            print(row)
        else:
            print("Television not found.")
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_televisor(serie, marca, nombre_cliente, apellido_cliente, numero_cedula):
    conn = connect()
    cursor = conn.cursor()
    try:
        sql = "UPDATE public.televisores SET marca = %s, nombre_cliente = %s, apellido_cliente = %s, numero_cedula = %s WHERE serie = %s"
        cursor.execute(sql, (marca, nombre_cliente, apellido_cliente, numero_cedula, serie))
        conn.commit()
        print("Television record updated successfully.")
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def delete_televisor(serie):
    conn = connect()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM public.televisores WHERE serie = %s"
        cursor.execute(sql, (serie,))
        conn.commit()
        print("Television record deleted successfully.")
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

# Example usage:

# Create a new television
create_televisor("TV12345", "Samsung", "saara", "dana", "1234567890")

# Read all televisions
read_televisores()

# Find a television by serial number
find_televisor_by_serie("TV12345")

# Update a television
update_televisor("TV12345", "Sony", "ala", "sera", "0987654321")

find_televisor_by_serie("TV12345")


# Delete a television
delete_televisor("TV12345")

find_televisor_by_serie("TV12345")