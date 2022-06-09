# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import generated.kaif_client_service_pb2 as kaif__client__service__pb2


class ClientServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddClient = channel.unary_unary(
                '/ClientService/AddClient',
                request_serializer=kaif__client__service__pb2.Client.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetClient = channel.unary_unary(
                '/ClientService/GetClient',
                request_serializer=kaif__client__service__pb2.ClientRequest.SerializeToString,
                response_deserializer=kaif__client__service__pb2.Client.FromString,
                )
        self.GetAllClients = channel.unary_unary(
                '/ClientService/GetAllClients',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=kaif__client__service__pb2.ClientsList.FromString,
                )
        self.UpdateClient = channel.unary_unary(
                '/ClientService/UpdateClient',
                request_serializer=kaif__client__service__pb2.Client.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ClientServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllClients(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddClient': grpc.unary_unary_rpc_method_handler(
                    servicer.AddClient,
                    request_deserializer=kaif__client__service__pb2.Client.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetClient': grpc.unary_unary_rpc_method_handler(
                    servicer.GetClient,
                    request_deserializer=kaif__client__service__pb2.ClientRequest.FromString,
                    response_serializer=kaif__client__service__pb2.Client.SerializeToString,
            ),
            'GetAllClients': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllClients,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=kaif__client__service__pb2.ClientsList.SerializeToString,
            ),
            'UpdateClient': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateClient,
                    request_deserializer=kaif__client__service__pb2.Client.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ClientService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClientService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientService/AddClient',
            kaif__client__service__pb2.Client.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientService/GetClient',
            kaif__client__service__pb2.ClientRequest.SerializeToString,
            kaif__client__service__pb2.Client.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllClients(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientService/GetAllClients',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            kaif__client__service__pb2.ClientsList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientService/UpdateClient',
            kaif__client__service__pb2.Client.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)