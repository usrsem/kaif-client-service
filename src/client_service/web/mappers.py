import generated.kaif_client_service_pb2 as pb2
import client_service.domain.dtos as dtos


def client_grpc_to_dto(client: pb2.Client) -> dtos.Client:
    return dtos.Client(
        telegram_id=client.telegram_id,
        telegram_username=client.telegram_username,
        telegram_fullname=client.telegram_fullname)


def client_dto_to_grpc(client: dtos.Client) -> pb2.Client:
    return pb2.Client(
        telegram_id=client.telegram_id,
        telegram_username=client.telegram_username,
        telegram_fullname=client.telegram_fullname)
    
