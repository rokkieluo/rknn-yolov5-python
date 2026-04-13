import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--module-dir", default="build", help="Directory containing rknn_yolov5 module")
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument("--img-config", help="Config path for image inference")
    mode_group.add_argument("--video-config", help="Config path for video inference")
    args = parser.parse_args()

    sys.path.insert(0, args.module_dir)
    import rknn_yolov5

    if args.img_config:
        print("=== Image Detections ===")
        img_dets = rknn_yolov5.get_yolov5_img_detections(args.img_config)
        print(f"count={len(img_dets)}")
        for i, det in enumerate(img_dets[:5]):
            print(
                f"[{i}] class={det.class_name} conf={det.confidence:.3f} "
                f"box=({det.x},{det.y},{det.width},{det.height})"
            )
        return

    # --video-config: realtime print detection data
    print("=== Thread Pool Realtime Detection Data ===")

    def on_frame(frame_id, detections):
        for det in detections:
            print(
                f"frame={frame_id} class={det.class_name} conf={det.confidence:.3f} "
                f"box=({det.x},{det.y},{det.width},{det.height})"
            )

    rknn_yolov5.stream_yolov5_thread_pool_detections(args.video_config, on_frame)


if __name__ == "__main__":
    main()
