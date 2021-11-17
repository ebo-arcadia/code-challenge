# A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.
#
# He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
#
# His mother looks out of a window 1.5 meters from the ground.
#
# How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?
#
# Three conditions must be met for a valid experiment:
# Float parameter "h" in meters must be greater than 0
# Float parameter "bounce" must be greater than 0 and less than 1
# Float parameter "window" must be less than h.
# If all three conditions above are fulfilled, return a positive integer, otherwise return -1.
#
# Note:
# The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.
#
# Examples:
# - h = 3, bounce = 0.66, window = 1.5, result is 3
#
# - h = 3, bounce = 1, window = 1.5, result is -1
#
# (Condition 2) not fulfilled).

# pseudocode
# if the condition is met (height, bounce_rate, window)
#   set variable current_height stores current_height
#   set variable count stores total times ball passing the window
#       while current_height is greater than the window
#           recursively add times ball passing the window
#           recursively reset new height stores in current_height
#       return count
# else:
# invalid and return -1


def bouncing_ball(height, bounce_rate, window):
    if height > 0 and 1 > bounce_rate > 0 and window < height:
        count = 1
        height = height * bounce_rate
        while height > window:
            count += 2
            height = height * bounce_rate
        return count
    else:
        return -1


def efficient_bouncing_ball(h, b, w):
    if not h > 0 and 1 > b > 0 and h > w:
        return -1
    count = 0
    while h > w:
        count += 1
        h *= b
        if h > w:
            count += 1
    return count or -1


h = 10
b = 0.66
w = 1.5
print("testing bouncing_ball: ", bouncing_ball(height=h, bounce_rate=b, window=w))
print("testing efficient_bouncing_ball: ", efficient_bouncing_ball(h=h, b=b, w=w))
