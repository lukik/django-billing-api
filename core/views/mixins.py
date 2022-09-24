from django.http import Http404
from rest_framework.response import Response
from rest_framework import mixins, viewsets, status, pagination
from core.api_exceptions import FieldIsRequired, RecordNotFound


class ListCreateRetrieveUpdateViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                                      mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                                      viewsets.GenericViewSet):
    """
    A viewset that provides `list`, `create`, `retrieve`, `update` actions.

    To use it, override the class and set the `.queryset` and `.serializer_class` attributes.
    """
    pass


class ListRetrieveUpdateViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides `list`, `create`, `retrieve`, `update` actions.

    To use it, override the class and set the `.queryset` and `.serializer_class` attributes.
    """
    pass


class ListCreateRetrieveViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides `list`, `create`, `retrieve`, `update` actions.

    To use it, override the class and set the `.queryset` and `.serializer_class` attributes.
    """
    pass


class ListRetrieveViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,  viewsets.GenericViewSet):
    """
    A viewset that provides `list`, `retrieve`, actions only.

    To use it, override the class and set the `.queryset` and `.serializer_class` attributes.
    """
    pass


class BulkCreateListModelMixin(object):
    """
    The name refers to Bulk Create & List Model Mixin
    Inherit this when you want to provide for bulk create
    source: http://stackoverflow.com/a/40253309/1082673
    """
    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(BulkCreateListModelMixin, self).get_serializer(*args, **kwargs)


class NoPagePagination(pagination.LimitOffsetPagination):
    """
    If a query is sent with a parameter no_page, then make the pagination to be zero
    source: https://stackoverflow.com/a/47642367
    source: https://www.django-rest-framework.org/api-guide/pagination/#custom-pagination-styles
    """
    def paginate_queryset(self, queryset, request, view=None):
        if 'no_page' in request.query_params:
            return None
        return self.standard_queryset(queryset, request, view)

    def standard_queryset(self, queryset, request, view=None):
        """
        This is copied direct from the pagination.LimitOffsetPagination.paginate_queryset in DRF code
        """
        self.count = self.get_count(queryset)
        self.limit = self.get_limit(request)
        if self.limit is None:
            return None

        self.offset = self.get_offset(request)
        self.request = request
        if self.count > self.limit and self.template is not None:
            self.display_page_controls = True

        if self.count == 0 or self.offset > self.count:
            return []
        return list(queryset[self.offset:self.offset + self.limit])


class DeleteViewSet(mixins.DestroyModelMixin):
    """
    A viewset that provides `destroy` action.

    To use it, override the class and set the `.queryset` and `.serializer_class` attributes.
    """
    def _requires_delete_reason(self):
        if 'delete_reason' not in self.request.data.keys():
            raise FieldIsRequired("Delete Reason field is required", "delete_reason")
        else:
            return ''

    def _delete_object(self):

        try:
            instance = self.get_object()
            instance.changeReason = self.request.data['delete_reason']
            self.perform_destroy(instance)
        except Http404:
            raise RecordNotFound()

    def destroy(self, request, *args, **kwargs):
        try:
            # ToDo: Figure out how to check if you are authorized to delete the resource
            if 'delete_reason' not in request.data.keys():
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={'errors': 'delete_reason: Invalid Delete Reason'})
            else:
                instance = self.get_object()
                # print(instance)
                instance.changeReason = request.data['delete_reason']
                self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

