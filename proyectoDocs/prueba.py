import googleapiclient.discovery

# Crea un cliente de la API de Google Drive.
client = googleapiclient.discovery.build('drive', 'v3')

# Obtén la clave de API de servicio.
key_file = open('service_account.json', 'r')
key = key_file.read()

# Autentícate con la clave de API de servicio.
client.auth.credentials = ServiceAccountCredentials.from_service_account_file(
    'service_account.json',
    scopes=['https://www.googleapis.com/auth/drive']
)

# Haz una solicitud a la API de Google Drive.
files = client.files().list(
    pageSize=10,
    fields='nextPageToken, files(id, name)'
).execute()

# Imprime los nombres de los archivos.
for file in files['files']:
    print(file['name'])
