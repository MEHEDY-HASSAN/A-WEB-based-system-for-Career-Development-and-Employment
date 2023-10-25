from rest_framework import serializers
from PostApp.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('PostID',
                  'ProfileID',
                  'ProfileName',
                  'ProfilePicture',
                  'PostDate',
                  'PostImage',
                  'PostMessage',
                  'PostLikeCnt',
                  'PostLikeList',
                  'PostCommentCnt',
                  'PostCommentList',
                  'PostTag')