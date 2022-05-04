import bouncing_balls


def test_bouncing_ball():
    result_1 = bouncing_balls.bouncing_ball(2, 0.5, 1)
    result_2 = bouncing_balls.bouncing_ball(3, 0.66, 1.5)
    result_3 = bouncing_balls.bouncing_ball(30, 0.66, 1.5)
    result_4 = bouncing_balls.bouncing_ball(30, 0.75, 1.5)
    result_5 = bouncing_balls.bouncing_ball(30, 0.4, 10)
    result_6 = bouncing_balls.bouncing_ball(40, 0.4, 10)
    result_7 = bouncing_balls.bouncing_ball(10, 0.6, 10)
    result_8 = bouncing_balls.bouncing_ball(40, 1, 10)
    result_9 = bouncing_balls.bouncing_ball(-5, 0.66, 1.5)
    result_10 = bouncing_balls.bouncing_ball(5, -1, 1.5)
    result_11 = bouncing_balls.bouncing_ball(4, 0.25, 1)

    assert result_1 == 1
    assert result_2 == 3
    assert result_3 == 15
    assert result_4 == 21
    assert result_5 == 3
    assert result_6 == 3
    assert result_7 == -1
    assert result_8 == -1
    assert result_9 == -1
    assert result_10 == -1
    assert result_11 == 1