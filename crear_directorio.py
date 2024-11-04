def crear_directorio(event, context):
    try:
        # Entrada
        bucket_name = event['body']['bucket_name']  # Nombre del bucket
        directory_name = event['body']['directory_name']  # Nombre del directorio
        s3 = boto3.client('s3')  # Inicializar el cliente de S3

        # Proceso
        s3.put_object(Bucket=bucket_name, Key=(directory_name + '/'))  # Agregar barra al final

        # Salida
        return {
            'statusCode': 200,
            'body': f'Directorio {directory_name} creado en el bucket {bucket_name}.'
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': f'No se pudo crear el directorio {directory_name} en el bucket {bucket_name}. Error: {str(e)}'
        }
