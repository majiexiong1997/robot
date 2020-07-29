
timer_type = {

    'step': 1,  # 步骤定时
    'action': 2,  # 行为超时定时
    'sleep': 3,
    'release_timer': 4,

}
'''操作结果'''
action_result = {
    'success': 1,
    'step_done': 2,
    'man_jump': 3,
    'action_done': 4,
    "step_time_out": 5,
}
'''事件定义'''
action_event = {
    'switch_module_step': 1,
    'switch_action_step': 2,
    'switch_next_action': 3,
    'step_time_out': 4

}
action_type = {
    'login_script':1,
}
