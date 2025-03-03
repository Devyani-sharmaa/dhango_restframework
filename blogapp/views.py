from django.shortcuts import render
from .models import Blog
from .serializers import UpdateUserProfileSerializer, UserRegistrationSerializer,BlogSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated



def home(request):
    return render(request, 'index.html')


def blog_list_page(request):
    blogs = Blog.objects.all()  # Fetch all blogs from the database
    return render(request, 'blog_list.html', {'blogs': blogs})  # Pass blogs to the template


# Render the blog details page
def blog_detail_page(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blog_detail.html', {'blog': blog})

# Render the user profile update page
@permission_classes([IsAuthenticated])
def update_profile_page(request):
    return render(request, 'update_profile.html')

# Render the create blog page
@permission_classes([IsAuthenticated])
def create_blog_page(request):
    return render(request, 'create_blog.html')

# Create your views here.
@api_view(["POST"])
def register_user(request):
    serializer=UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user=request.user
    serializer=UpdateUserProfileSerializer(user,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_blog(request):
    user = request.user
    serializer=BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=user)
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def blog_list(request):
    blogs=Blog.objects.all()
    serializer=BlogSerializer(blogs,many=True)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_blog(request,pk):
    user=request.user
    blog=Blog.objects.get(id=pk)
    if blog.author!=user:
        return Response({"error":"You are not the author of this blog"},status=status.HTTP_403_FORBIDDEN)
    serializer=BlogSerializer(blog,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    user = request.user 
    if blog.author != user:
        return Response({"error": "You are not the author of this blog"}, status=status.HTTP_403_FORBIDDEN)
    blog.delete()
    return Response({"message": "Blog deleted successfully"}, status=status.HTTP_204_NO_CONTENT)