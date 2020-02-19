from rest_framework import mixins, viewsets, status, response
from rest_framework.decorators import api_view

from . import models
from . import serializers


class AccountViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    """
        API endpoint that allows accounts to be viewed.

        list:
        Return all the accounts available.

        create:
        Create an account.

        retrieve:
        Return a given account.
    """
    # model = models.Account
    # serializer_class = serializers.AccountSerializer
    queryset = models.Account.objects.all()

    def get_serializer_class(self):
        serializer_class = serializers.AccountSerializer
        if self.action == 'update':
            serializer_class = serializers.AccountUpdateSerializer
        return serializer_class

    def update(self, request, pk=None):
        super().update(request, pk)
        account = self.get_object()
        serialized_account = serializers.AccountSerializer(account)
        return response.Response(data=serialized_account.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def fizz_buzz(request):
    """
        API view to run program FizzBuzz and send response to client.
    """
    
    # store x query param if it is at request
    x = int(request.query_params.get('x', None))
    if x:
        limit = x
    else:
        limit = 100

    # store string result to send in Response
    str_result=""
    for i in range(1, limit):
        if i % 3 == 0 and i % 5 == 0:
            str_result += "FizzBuzz"
        elif i % 3 == 0:
            str_result += "Fizz"
        elif i % 5 == 0:
            str_result += "Buzz"
        else:
            str_result += str(i)

    return response.Response(data={"x": limit, "fizzbuzz": str_result}, status=status.HTTP_200_OK)

