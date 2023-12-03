import grpc
from concurrent import futures
import reddit_pb2
import reddit_pb2_grpc
import uuid
from datetime import datetime
import threading
from db import thread_posts, thread_comments

class ParallelUniverseRedditService(reddit_pb2_grpc.RedditService):

    lock_for_posts = threading.Lock()
    lock_for_comments = threading.Lock()

    def CreatePost(self, request, context):
        unique_post_id = str(uuid.uuid4())
        post_title = request.title
        post_content = request.content
        author_id = request.authorId
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_post = reddit_pb2.Post(
            postId=unique_post_id,
            title=post_title,
            content=post_content,
            authorId=author_id,
            score=0,
            state=reddit_pb2.Post.State.NORMAL,
            publicationDate=current_time
        )

        if request.HasField("mediaType"):
            if request.mediaType.WhichOneof("type") == "imageUrl":
                new_post.imageUrl = request.mediaType.imageUrl
            elif request.mediaType.WhichOneof("type") == "videoUrl":
                new_post.videoUrl = request.mediaType.videoUrl

        with self.lock_for_posts:
            thread_posts[unique_post_id] = new_post

        return new_post

    def modify_post_score(self, request, context, increment):
        post_id = request.postId
        with self.lock_for_posts:
            if post_id in thread_posts:
                if increment:
                    thread_posts[post_id].score += 1
                else:
                    thread_posts[post_id].score -= 1
                return thread_posts[post_id]
            else:
                context.set_details("Post not found.")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return reddit_pb2.Post()

    def get_post_details(self, request, context):
        post_id = request.postId
        if post_id in thread_posts:
            return thread_posts[post_id]
        else:
            context.set_details("Post not found.")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return reddit_pb2.Post()

    def create_new_comment(self, request, context):
        unique_comment_id = str(uuid.uuid4())
        author_id = request.authorId
        comment_content = request.content
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_comment = reddit_pb2.Comment(
            commentId=unique_comment_id,
            authorId=author_id,
            content=comment_content,
            score=0,
            state=reddit_pb2.Comment.State.NORMAL,
            publicationDate=current_time
        )

        if request.HasField("parentType"):
            if request.parentType.WhichOneof("type") == "parentPostId":
                new_comment.parentPostId = request.parentType.parentPostId
            elif request.parentType.WhichOneof("type") == "parentCommentId":
                new_comment.parentCommentId = request.parentType.parentCommentId

        with self.lock_for_comments:
            thread_comments[unique_comment_id] = new_comment

        return new_comment

    def modify_comment_score(self, request, context, increment):
        comment_id = request.commentId
        with self.lock_for_comments:
            if comment_id in thread_comments:
                if increment:
                    thread_comments[comment_id].score += 1
                else:
                    thread_comments[comment_id].score -= 1
                return thread_comments[comment_id]
            else:
                context.set_details("Comment not found.")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return reddit_pb2.Comment()

    # Implement other methods like RetrieveTopNComments and ExpandCommentBranch...
    # ...

def start_parallel_universe_reddit_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reddit_pb2_grpc.add_RedditServiceServicer_to_server(ParallelUniverseRedditService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Parallel Universe Reddit Server running on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    start_parallel_universe_reddit_server()
