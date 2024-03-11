# coding: utf-8

"""
    WhatsApp Business API

    See https://developers.facebook.com/docs/whatsapp

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from whats_app_business_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from whats_app_business_python_sdk.api_response import AsyncGeneratorResponse
from whats_app_business_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from whats_app_business_python_sdk import schemas  # noqa: F401

from whats_app_business_python_sdk.model.upload_media_response import UploadMediaResponse as UploadMediaResponseSchema

from whats_app_business_python_sdk.type.upload_media_response import UploadMediaResponse

from ...api_client import Dictionary
from whats_app_business_python_sdk.pydantic.upload_media_response import UploadMediaResponse as UploadMediaResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationMsword = schemas.BinarySchema
SchemaForRequestBodyApplicationPdf = schemas.BinarySchema
SchemaForRequestBodyApplicationVndMsExcel = schemas.BinarySchema
SchemaForRequestBodyApplicationVndMsPowerpoint = schemas.BinarySchema
SchemaForRequestBodyAudioAcc = schemas.BinarySchema
SchemaForRequestBodyAudioAmr = schemas.BinarySchema
SchemaForRequestBodyAudioMp4 = schemas.BinarySchema
SchemaForRequestBodyAudioMpeg = schemas.BinarySchema
SchemaForRequestBodyAudioOgg = schemas.BinarySchema
SchemaForRequestBodyCodecsopus = schemas.BinarySchema
SchemaForRequestBodyImageJpeg = schemas.BinarySchema
SchemaForRequestBodyImagePng = schemas.BinarySchema
SchemaForRequestBodyTextPlain = schemas.BinarySchema
SchemaForRequestBodyVideoMp4 = schemas.BinarySchema


request_body_body = api_client.RequestBody(
    content={
        'application/msword': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationMsword),
        'application/pdf': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationPdf),
        'application/vnd.ms-excel': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndMsExcel),
        'application/vnd.ms-powerpoint': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndMsPowerpoint),
        'audio/acc': api_client.MediaType(
            schema=SchemaForRequestBodyAudioAcc),
        'audio/amr': api_client.MediaType(
            schema=SchemaForRequestBodyAudioAmr),
        'audio/mp4': api_client.MediaType(
            schema=SchemaForRequestBodyAudioMp4),
        'audio/mpeg': api_client.MediaType(
            schema=SchemaForRequestBodyAudioMpeg),
        'audio/ogg': api_client.MediaType(
            schema=SchemaForRequestBodyAudioOgg),
        'codecs=opus': api_client.MediaType(
            schema=SchemaForRequestBodyCodecsopus),
        'image/jpeg': api_client.MediaType(
            schema=SchemaForRequestBodyImageJpeg),
        'image/png': api_client.MediaType(
            schema=SchemaForRequestBodyImagePng),
        'text/plain': api_client.MediaType(
            schema=SchemaForRequestBodyTextPlain),
        'video/mp4': api_client.MediaType(
            schema=SchemaForRequestBodyVideoMp4),
    },
    required=True,
)
_auth = [
    'bearerAuth',
]
SchemaFor200ResponseBodyApplicationJson = UploadMediaResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UploadMediaResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UploadMediaResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _upload_media_mapped_args(
        self,
        body: typing.IO,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        args.body = body if body is not None else _body
        return args

    async def _aupload_media_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/msword',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Upload-Media
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/media',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_body.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _upload_media_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/msword',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Upload-Media
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/media',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_body.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UploadMediaRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupload_media(
        self,
        body: typing.IO,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_media_mapped_args(
            body=body,
        )
        return await self._aupload_media_oapg(
            body=args.body,
            **kwargs,
        )
    
    def upload_media(
        self,
        body: typing.IO,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_media_mapped_args(
            body=body,
        )
        return self._upload_media_oapg(
            body=args.body,
        )

class UploadMedia(BaseApi):

    async def aupload_media(
        self,
        body: typing.IO,
        validate: bool = False,
        **kwargs,
    ) -> UploadMediaResponsePydantic:
        raw_response = await self.raw.aupload_media(
            body=body,
            **kwargs,
        )
        if validate:
            return RootModel[UploadMediaResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(UploadMediaResponsePydantic, raw_response.body)
    
    
    def upload_media(
        self,
        body: typing.IO,
        validate: bool = False,
    ) -> UploadMediaResponsePydantic:
        raw_response = self.raw.upload_media(
            body=body,
        )
        if validate:
            return RootModel[UploadMediaResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(UploadMediaResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        body: typing.IO,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_media_mapped_args(
            body=body,
        )
        return await self._aupload_media_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        body: typing.IO,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_media_mapped_args(
            body=body,
        )
        return self._upload_media_oapg(
            body=args.body,
        )
