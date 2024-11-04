def lambda_handler(event, context):
    try:
        # Entrada
        bucket_name = event['body']['bucket_name']  # Nombre del bucket
        directory_name = event['body']['directory_name']  # Nombre del directorio
        file_name = event['body']['file_name']  # Nombre del archivo
        file_content = event['body']['file_content']  # Contenido del archivo
        s3 = boto3.client('s3')  # Inicializar el cliente de S3

        # Proceso
        s3.put_object(Bucket=bucket_name, Key=f'{directory_name}/{file_name}', Body=file_content)

        # Salida
        return {
            'statusCode': 200,
            'body': f'Archivo {file_name} subido a {directory_name} en el bucket {bucket_name}.'
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': f'No se pudo subir el archivo {file_name} al directorio {directory_name} en el bucket {bucket_name}. Error: {str(e)}'
        }
