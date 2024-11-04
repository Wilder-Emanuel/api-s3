import boto3

def lambda_handler(event, context):
    try:
        # Entrada
        nombre_bucket = event['body']['bucket']  # Acceso al nombre del bucket en el cuerpo del evento
        s3 = boto3.client('s3')  # Inicializar el cliente de S3

        # Proceso
        s3.create_bucket(Bucket=nombre_bucket)

        # Salida
        return {
            'statusCode': 200,
            'body': f'Bucket {nombre_bucket} creado con éxito.'
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': f'No se pudo crear el bucket {nombre_bucket}. Error: {str(e)}'
        }
