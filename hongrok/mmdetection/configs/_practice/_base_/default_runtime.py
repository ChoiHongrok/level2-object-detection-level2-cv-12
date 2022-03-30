checkpoint_config = dict(interval=1, save_last=True, max_keep_ckpts=2)
# yapf:disable

# log_config = dict(
#     interval=50,
#     hooks=[
#         dict(type='TextLoggerHook'),
#         # dict(type='TensorboardLoggerHook'),
#         dict(type='WandbLoggerHook',
#                 init_kwargs = dict(project='detection',
#                                     entity='yolo12',
#                                     name = 'hongrok_'+'cascadeRCNN_swin_focal_gradClip50',
#         ) 
#         )
#     ])
# yapf:enable
custom_hooks = [dict(type='NumClassCheckHook')]

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]

# disable opencv multithreading to avoid system being overloaded
opencv_num_threads = 0
# set multi-process start method as `fork` to speed up the training
mp_start_method = 'fork'
