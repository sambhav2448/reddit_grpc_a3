# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reddit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0creddit.proto\x12\x06reddit\"\x16\n\x04User\x12\x0e\n\x06userId\x18\x01 \x01(\t\"\x87\x02\n\x04Post\x12\x0e\n\x06postId\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x12\n\x08imageUrl\x18\x04 \x01(\tH\x00\x12\x12\n\x08videoUrl\x18\x05 \x01(\tH\x00\x12\x15\n\x08\x61uthorId\x18\x06 \x01(\tH\x01\x88\x01\x01\x12\r\n\x05score\x18\x07 \x01(\x05\x12!\n\x05state\x18\x08 \x01(\x0e\x32\x12.reddit.Post.State\x12\x17\n\x0fpublicationDate\x18\t \x01(\t\"+\n\x05State\x12\n\n\x06NORMAL\x10\x00\x12\n\n\x06LOCKED\x10\x01\x12\n\n\x06HIDDEN\x10\x02\x42\x0b\n\tmediaTypeB\x0b\n\t_authorId\"\xef\x01\n\x07\x43omment\x12\x11\n\tcommentId\x18\x01 \x01(\t\x12\x16\n\x0cparentPostId\x18\x02 \x01(\tH\x00\x12\x19\n\x0fparentCommentId\x18\x03 \x01(\tH\x00\x12\x10\n\x08\x61uthorId\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\r\n\x05score\x18\x06 \x01(\x05\x12$\n\x05state\x18\x07 \x01(\x0e\x32\x15.reddit.Comment.State\x12\x17\n\x0fpublicationDate\x18\x08 \x01(\t\"\x1f\n\x05State\x12\n\n\x06NORMAL\x10\x00\x12\n\n\x06HIDDEN\x10\x01\x42\x0c\n\nparentType\"\x8e\x01\n\x13PostCreationRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x12\n\x08imageUrl\x18\x03 \x01(\tH\x00\x12\x12\n\x08videoUrl\x18\x04 \x01(\tH\x00\x12\x15\n\x08\x61uthorId\x18\x05 \x01(\tH\x01\x88\x01\x01\x42\x0b\n\tmediaTypeB\x0b\n\t_authorId\"3\n\x0fPostVoteRequest\x12\x0e\n\x06postId\x18\x01 \x01(\t\x12\x10\n\x08isUpvote\x18\x02 \x01(\x08\"$\n\x12PostDetailsRequest\x12\x0e\n\x06postId\x18\x01 \x01(\t\"|\n\x16\x43ommentCreationRequest\x12\x16\n\x0cparentPostId\x18\x01 \x01(\tH\x00\x12\x19\n\x0fparentCommentId\x18\x02 \x01(\tH\x00\x12\x10\n\x08\x61uthorId\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\tB\x0c\n\nparentType\"9\n\x12\x43ommentVoteRequest\x12\x11\n\tcommentId\x18\x01 \x01(\t\x12\x10\n\x08isUpvote\x18\x02 \x01(\x08\"3\n\x12TopCommentsRequest\x12\x0e\n\x06postId\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\"G\n\x0f\x43ommentOverview\x12 \n\x07\x63omment\x18\x01 \x01(\x0b\x32\x0f.reddit.Comment\x12\x12\n\nhasReplies\x18\x02 \x01(\x08\"H\n\x13TopCommentsResponse\x12\x31\n\x10\x63ommentsOverview\x18\x01 \x03(\x0b\x32\x17.reddit.CommentOverview\"8\n\x14\x43ommentThreadRequest\x12\x11\n\tcommentId\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\"_\n\rCommentThread\x12&\n\rparentComment\x18\x01 \x01(\x0b\x32\x0f.reddit.Comment\x12&\n\rchildComments\x18\x02 \x03(\x0b\x32\x0f.reddit.Comment\"F\n\x15\x43ommentThreadResponse\x12-\n\x0e\x63ommentThreads\x18\x01 \x03(\x0b\x32\x15.reddit.CommentThread2\xd5\x03\n\rRedditService\x12\x37\n\nCreatePost\x12\x1b.reddit.PostCreationRequest\x1a\x0c.reddit.Post\x12\x33\n\nVoteOnPost\x12\x17.reddit.PostVoteRequest\x1a\x0c.reddit.Post\x12:\n\x0eGetPostDetails\x12\x1a.reddit.PostDetailsRequest\x1a\x0c.reddit.Post\x12@\n\rCreateComment\x12\x1e.reddit.CommentCreationRequest\x1a\x0f.reddit.Comment\x12<\n\rVoteOnComment\x12\x1a.reddit.CommentVoteRequest\x1a\x0f.reddit.Comment\x12I\n\x0eGetTopComments\x12\x1a.reddit.TopCommentsRequest\x1a\x1b.reddit.TopCommentsResponse\x12O\n\x10GetCommentThread\x12\x1c.reddit.CommentThreadRequest\x1a\x1d.reddit.CommentThreadResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reddit_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USER']._serialized_start=24
  _globals['_USER']._serialized_end=46
  _globals['_POST']._serialized_start=49
  _globals['_POST']._serialized_end=312
  _globals['_POST_STATE']._serialized_start=243
  _globals['_POST_STATE']._serialized_end=286
  _globals['_COMMENT']._serialized_start=315
  _globals['_COMMENT']._serialized_end=554
  _globals['_COMMENT_STATE']._serialized_start=509
  _globals['_COMMENT_STATE']._serialized_end=540
  _globals['_POSTCREATIONREQUEST']._serialized_start=557
  _globals['_POSTCREATIONREQUEST']._serialized_end=699
  _globals['_POSTVOTEREQUEST']._serialized_start=701
  _globals['_POSTVOTEREQUEST']._serialized_end=752
  _globals['_POSTDETAILSREQUEST']._serialized_start=754
  _globals['_POSTDETAILSREQUEST']._serialized_end=790
  _globals['_COMMENTCREATIONREQUEST']._serialized_start=792
  _globals['_COMMENTCREATIONREQUEST']._serialized_end=916
  _globals['_COMMENTVOTEREQUEST']._serialized_start=918
  _globals['_COMMENTVOTEREQUEST']._serialized_end=975
  _globals['_TOPCOMMENTSREQUEST']._serialized_start=977
  _globals['_TOPCOMMENTSREQUEST']._serialized_end=1028
  _globals['_COMMENTOVERVIEW']._serialized_start=1030
  _globals['_COMMENTOVERVIEW']._serialized_end=1101
  _globals['_TOPCOMMENTSRESPONSE']._serialized_start=1103
  _globals['_TOPCOMMENTSRESPONSE']._serialized_end=1175
  _globals['_COMMENTTHREADREQUEST']._serialized_start=1177
  _globals['_COMMENTTHREADREQUEST']._serialized_end=1233
  _globals['_COMMENTTHREAD']._serialized_start=1235
  _globals['_COMMENTTHREAD']._serialized_end=1330
  _globals['_COMMENTTHREADRESPONSE']._serialized_start=1332
  _globals['_COMMENTTHREADRESPONSE']._serialized_end=1402
  _globals['_REDDITSERVICE']._serialized_start=1405
  _globals['_REDDITSERVICE']._serialized_end=1874
# @@protoc_insertion_point(module_scope)