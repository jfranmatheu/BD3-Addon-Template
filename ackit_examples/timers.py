from addon_template.ackit import Reg


count = 0


@Reg.Deco.TIMER(first_interval=1.0, step_interval=1.0, timeout=10, one_time_only=False, persistent=True)
def timer__after_1_second__1_second_interval__for_10_seconds():
    global count
    count += 1
    print("Timer... Count", count)
