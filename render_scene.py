#!/usr/bin/env python3
"""
从已生成的场景 JSON 文件渲染不同视角的图片和视频

使用方法:
    # 渲染顶视图
    python render_scene.py --scene path/to/scene.json --mode top_down_frame

    # 渲染房间多角度图片（每个房间4个角度）
    python render_scene.py --scene path/to/scene.json --mode room_image

    # 渲染房间视频（360度旋转）
    python render_scene.py --scene path/to/scene.json --mode room_video
"""

import os
import sys
from argparse import ArgumentParser

import compress_json

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ai2holodeck.constants import OBJATHOR_ASSETS_DIR
from ai2holodeck.generation.utils import (
    get_room_images,
    get_top_down_frame,
    room_video,
)


def main():
    parser = ArgumentParser(description="从场景 JSON 渲染不同视角的图片")
    parser.add_argument(
        "--scene",
        required=True,
        help="场景 JSON 文件路径",
    )
    parser.add_argument(
        "--mode",
        choices=["top_down_frame", "room_image", "room_video"],
        default="top_down_frame",
        help="渲染模式: top_down_frame(顶视图), room_image(房间多角度), room_video(360度视频)",
    )
    parser.add_argument(
        "--objaverse_asset_dir",
        default=OBJATHOR_ASSETS_DIR,
        help="资产目录路径",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=1024,
        help="图片宽度（默认: 1024）",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=1024,
        help="图片高度（默认: 1024）",
    )
    parser.add_argument(
        "--output",
        help="输出文件路径（可选，默认保存在场景同目录）",
    )

    args = parser.parse_args()

    # 检查场景文件
    if not os.path.exists(args.scene):
        print(f"❌ 错误: 场景文件不存在: {args.scene}")
        sys.exit(1)

    print(f"📂 加载场景: {args.scene}")
    scene = compress_json.load(args.scene)

    if "query" not in scene:
        scene["query"] = os.path.basename(args.scene).replace(".json", "")

    # 获取保存目录
    scene_dir = os.path.dirname(args.scene)
    scene_name = os.path.basename(args.scene).replace(".json", "")

    print(f"🎨 渲染模式: {args.mode}")
    print(f"📐 分辨率: {args.width}x{args.height}")

    if args.mode == "top_down_frame":
        # 渲染顶视图
        print("🖼️  正在渲染顶视图...")
        image = get_top_down_frame(
            scene, args.objaverse_asset_dir, args.width, args.height
        )

        output_path = args.output or os.path.join(
            scene_dir, f"{scene_name}_top_down.png"
        )
        image.save(output_path)
        print(f"✅ 顶视图已保存: {output_path}")

    elif args.mode == "room_image":
        # 渲染房间多角度图片
        print("🖼️  正在渲染房间多角度图片（每个房间4个角度）...")
        room_images = get_room_images(
            scene, args.objaverse_asset_dir, args.width, args.height
        )

        saved_files = []
        for room_name, images in room_images.items():
            for i, image in enumerate(images):
                output_path = os.path.join(
                    scene_dir, f"{scene_name}_{room_name}_angle{i}.png"
                )
                image.save(output_path)
                saved_files.append(output_path)

        print(f"✅ 共保存 {len(saved_files)} 张图片:")
        for f in saved_files:
            print(f"   - {f}")

    elif args.mode == "room_video":
        # 渲染360度旋转视频
        print("🎥 正在渲染360度旋转视频（这可能需要几分钟）...")
        video = room_video(scene, args.objaverse_asset_dir, args.width, args.height)

        output_path = args.output or os.path.join(scene_dir, f"{scene_name}_video.mp4")
        video.write_videofile(output_path, fps=30)
        print(f"✅ 视频已保存: {output_path}")

    print("\n🎉 渲染完成!")


if __name__ == "__main__":
    main()
