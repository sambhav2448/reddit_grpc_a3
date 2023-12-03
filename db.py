import reddit_pb2

# Dictionary to store posts and comments
thread_posts = {}
thread_comments = {}

def initialize_database():
    # Populating initial dummy posts
    for post_index in range(1, 101):
        post_id = f'post_{post_index:04d}'
        thread_posts[post_id] = reddit_pb2.Post(
            postId=post_id,
            title=f"Example Post Title {post_index}",
            content="This is example post content.",
            authorId=f"user{post_index}",
            score=post_index * 10,
            state=reddit_pb2.Post.State.NORMAL,
            publicationDate="2023-12-02 14:01:56"
        )

        # Adding comments to the first post for testing purposes
        if post_index == 1:
            for comment_index in range(1, 101):
                comment_id = f'comment_{comment_index:04d}'
                thread_comments[comment_id] = reddit_pb2.Comment(
                    commentId=comment_id,
                    authorId=f"user{comment_index}",
                    content=f"Example Comment Content {comment_index}",
                    parentPostId=post_id,
                    score=100 - comment_index,
                    state=reddit_pb2.Comment.State.NORMAL,
                    publicationDate="2023-12-02 14:01:57"
                )

                # Adding replies to the first five comments
                if comment_index <= 5:
                    reply_id = f'reply_{comment_index:04d}'
                    thread_comments[reply_id] = reddit_pb2.Comment(
                        commentId=reply_id,
                        authorId=f"user{comment_index + 100}",
                        content=f"Example Reply Content {comment_index}",
                        parentCommentId=comment_id,
                        score=50 - comment_index,
                        state=reddit_pb2.Comment.State.NORMAL,
                        publicationDate="2023-12-02 14:01:58"
                    )

# Call the function to initialize the database
initialize_database()
