import grpc
import reddit_pb2
import reddit_pb2_grpc

class ParallelUniverseRedditClient:
    def __init__(self, host="localhost", port=50051):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = reddit_pb2_grpc.RedditServiceStub(self.channel)

    def submit_post(self, title, content, author_id, imageUrl=None, videoUrl=None):
        post_request = reddit_pb2.PostCreationRequest(
            title=title,
            content=content,
            authorId=author_id
        )
        # Set the image URL or video URL if provided
        if imageUrl:
            post_request.imageUrl = imageUrl
        elif videoUrl:
            post_request.videoUrl = videoUrl

        return self.stub.CreatePost(post_request)

    def vote_on_post(self, post_id, is_upvote=True):
        vote_request = reddit_pb2.PostVoteRequest(
            postId=post_id,
            isUpvote=is_upvote
        )
        return self.stub.VoteOnPost(vote_request)

    def fetch_post_details(self, post_id):
        details_request = reddit_pb2.PostDetailsRequest(postId=post_id)
        return self.stub.GetPostDetails(details_request)

    def submit_comment(self, author_id, content, parent_post_id=None, parent_comment_id=None):
        comment_request = reddit_pb2.CommentCreationRequest(
            authorId=author_id,
            content=content
        )
        # Set parent post/comment ID if provided
        if parent_post_id:
            comment_request.parentPostId = parent_post_id
        elif parent_comment_id:
            comment_request.parentCommentId = parent_comment_id

        return self.stub.CreateComment(comment_request)

    def vote_on_comment(self, comment_id, is_upvote=True):
        vote_request = reddit_pb2.CommentVoteRequest(
            commentId=comment_id,
            isUpvote=is_upvote
        )
        return self.stub.VoteOnComment(vote_request)

    def get_top_comments(self, post_id, count):
        top_comments_request = reddit_pb2.TopCommentsRequest(
            postId=post_id,
            count=count
        )
        return self.stub.GetTopComments(top_comments_request)

    def expand_comment_thread(self, comment_id, depth):
        thread_request = reddit_pb2.CommentThreadRequest(
            commentId=comment_id,
            depth=depth
        )
        return self.stub.GetCommentThread(thread_request)

    def disconnect(self):
        self.channel.close()


def main():
    client = ParallelUniverseRedditClient(host="localhost", port=50051)
    new_post_response = client.submit_post(
        title="Parallel Universe Post", content="Exploring the multiverse!", author_id="multi_user_1"
    )
    print(f"New Post by {new_post_response.authorId}: {new_post_response.title} - {new_post_response.content} [{new_post_response.publicationDate}]")
    client.disconnect()

if __name__ == "__main__":
    main()