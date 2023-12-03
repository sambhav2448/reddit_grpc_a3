def get_most_upvoted_reply(client, post_id, max_comments, max_replies):
    post_details = client.fetch_post_details(post_id)
    if not post_details:
        return None

    top_comments_response = client.get_top_comments(post_id, max_comments)
    if not top_comments_response or not top_comments_response.commentsOverview:
        return None

    # Extract the actual Comment objects from CommentOverview
    top_comments = [overview.comment for overview in top_comments_response.commentsOverview]

    top_comment = max(top_comments, key=lambda c: c.score, default=None)
    if not top_comment:
        return None

    comment_replies_response = client.expand_comment_thread(top_comment.commentId, max_replies)
    if not comment_replies_response or not comment_replies_response.commentThreads:
        return None

    # Assuming each CommentThread has a list of child comments, and you want the top reply from the first thread
    comment_replies = comment_replies_response.commentThreads[0].childComments
    top_reply = max(comment_replies, key=lambda c: c.score, default=None)

    return top_reply
