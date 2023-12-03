import unittest
from unittest.mock import Mock
import reddit_pb2
from reddit_utils import get_most_upvoted_reply

class TestGetMostUpvotedReply(unittest.TestCase):
    def setUp(self):
        # Create a mock instance of your gRPC client
        self.mock_client = Mock()

    def test_get_most_upvoted_reply_success(self):
        # Setup mock data for Post details
        mock_post_details = reddit_pb2.Post(postId="1", title="Test Post", content="Test Content")

        # Setup mock data for TopCommentsResponse
        mock_comment_overviews = [
            reddit_pb2.CommentOverview(comment=reddit_pb2.Comment(commentId="2", score=10), hasReplies=True),
            reddit_pb2.CommentOverview(comment=reddit_pb2.Comment(commentId="3", score=5), hasReplies=False)
        ]
        mock_top_comments = reddit_pb2.TopCommentsResponse(commentsOverview=mock_comment_overviews)

        # Setup mock data for CommentThreadResponse
        mock_comment_threads = [
            reddit_pb2.CommentThread(parentComment=reddit_pb2.Comment(commentId="4"), childComments=[
                reddit_pb2.Comment(commentId="5", score=20),
                reddit_pb2.Comment(commentId="6", score=15)
            ])
        ]
        mock_comment_replies = reddit_pb2.CommentThreadResponse(commentThreads=mock_comment_threads)

        # Configure the mock client
        self.mock_client.fetch_post_details.return_value = mock_post_details
        self.mock_client.get_top_comments.return_value = mock_top_comments
        self.mock_client.expand_comment_thread.return_value = mock_comment_replies

        # Call the function with the mock client
        most_upvoted_reply = get_most_upvoted_reply(self.mock_client, "1", 2, 2)

        # Validate the result
        self.assertIsNotNone(most_upvoted_reply)
        self.assertEqual(most_upvoted_reply.commentId, "5")

    def test_get_most_upvoted_reply_no_post(self):
        # Setup mock client to return None for post details
        self.mock_client.fetch_post_details.return_value = None

        # Expect the function to return None
        result = get_most_upvoted_reply(self.mock_client, "1", 2, 2)
        self.assertIsNone(result)

    # Additional test cases can be added here

if __name__ == '__main__':
    unittest.main()
