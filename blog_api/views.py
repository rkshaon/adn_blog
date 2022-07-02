from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from blog_adn.utility import auth_user

from blog_api.models import Post
from blog_api.models import Comment

from blog_api.serializers import PostSerializer
from blog_api.serializers import CommentSerializer

@api_view(['GET'])
def get_all_post(request):
    posts = Post.objects.all()
    post_serializer = PostSerializer(posts, many=True)
    data = post_serializer.data

    return Response({
        'status': True,
        'data': data
    })

@api_view(['GET'])
def get_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post_serializer = PostSerializer(post)
    data = post_serializer.data

    return Response({
        'status': True,
        'data': data
    })

@api_view(['POST'])
def add_post(request):
    user = auth_user(request)

    data = request.data
    data['added_by'] = user.id

    post_serializer = PostSerializer(data=data)

    if post_serializer.is_valid():
        post_serializer.save()
    else:
        return Response({
            'status': False,
            'data': post_serializer.errors
        })

    return Response({
        'status': True,
    })

@api_view(['DELETE'])
def delete_post(request, post_id):
    user = auth_user(request)
    post = Post.objects.get(id=post_id)

    if user.id != post.added_by.id:
        return Response({
            'status': False,
            'message': 'You are not authorized to delete this post'
        })

    post.delete()

    return Response({
        'status': True,
        'message': 'Post deleted successfully'
    })

@api_view(['POST'])
def add_comment(request, post_id):
    user = auth_user(request)

    data = request.data
    data['post'] = post_id
    data['added_by'] = user.id

    comment_serializer = CommentSerializer(data=data)

    if comment_serializer.is_valid():
        comment_serializer.save()
    else:
        return Response({
            'status': False,
            'data': comment_serializer.errors
        })

    return Response({
        'status': True,
    })

@api_view(['GET'])
def get_all_comment(request, post_id):
    comments = Comment.objects.filter(post=post_id)
    comment_serializer = CommentSerializer(comments, many=True)
    data = comment_serializer.data

    return Response({
        'status': True,
        'data': data
    })