Python 运行说明

1) 进入目录：
   cd rknn-yolov5-python

2) 图片推理：
   ./run_demo.sh --img-config configs/yolov5_img.json

3) 视频推理：
   ./run_demo.sh --video-config configs/yolov5_thread_pool.json

configs为对应参数加载的地方，自行在configs目录中查看

说明：
- 输出视频默认保存为当前目录的 thread_pool_result.mp4
- 如需直接用 python3 命令，可先设置：
  export LD_LIBRARY_PATH=$(pwd)/build:$LD_LIBRARY_PATH
  python3 python_demo.py --video-config configs/yolov5_thread_pool.json
