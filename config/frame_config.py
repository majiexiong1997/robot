

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

'''当前行为状态'''
action_type = {
    'start_script':1,
    'continue_action':2,
    'action_end_script':3,

}


module_type = {
    'test1':1,
    'test2':2,
}
