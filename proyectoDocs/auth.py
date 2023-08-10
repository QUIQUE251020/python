import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Aquí deberás reemplazar 'ruta/a/tu/archivo/credenciales.json'
CREDENTIALS_FILE = r'C:\Users\tecnologia\Documents\Programacion\python\proyectoDocs\credenciales.json'
SCOPES = ['https://www.googleapis.com/auth/documents']

def authenticate_and_get_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('docs', 'v1', credentials=creds)
    return service

# Obtén el servicio autenticado
service = authenticate_and_get_service()

# Aquí puedes continuar con tus operaciones utilizando 'service' para interactuar con Google Docs
# Por ejemplo, podrías crear un nuevo documento
def create_document_with_title(title):
    service = authenticate_and_get_service()

    # Crear un nuevo documento con el título proporcionado
    document = {
        'title': title
    }
    created_document = service.documents().create(body=document).execute()

    print(f'Documento creado con el título: {title}')
    print(f'ID del documento: {created_document["documentId"]}')

create_document_with_title("Enero")

