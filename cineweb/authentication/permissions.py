from rest_framework.permissions import BasePermission

class isAdmin(BasePermission):

    def has_Permission(self,request,View):

        return bool(request.user and request.user.is_authenticated  and request.user.role=='Admin')
    
class isUser(BasePermission):

    def has_Permission(self,request,View):

        return bool(request.user and request.user.is_authenticated  and request.user.role=='User')

