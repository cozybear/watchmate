from rest_framework.throttling import UserRateThrottle

class ReviewCreateThrottle(UserRateThrottle):
    scope = 'review-create'


class ReviewListThrottle(UserRateThrottle):
    scope = 'review-list'

# class UserReviewMinuteThrottle(UserRateThrottle):
#     scope = 'user-review-min'

# class UserReviewHourThrottle(UserRateThrottle):
#     scope = 'user-review-min'