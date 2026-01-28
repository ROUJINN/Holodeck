#!/usr/bin/env python3
"""
检查 Objaverse 资产数据库中哪些资产文件缺失

用法:
    python check_missing_assets.py
"""

import os

import compress_json

from ai2holodeck.constants import OBJATHOR_ANNOTATIONS_PATH, OBJATHOR_ASSETS_DIR


def check_missing_assets():
    print("=" * 60)
    print("检查 Objaverse 资产文件")
    print("=" * 60)
    print(f"资产目录: {OBJATHOR_ASSETS_DIR}")
    print(f"注释文件: {OBJATHOR_ANNOTATIONS_PATH}")
    print()

    # 加载数据库
    print("加载资产数据库...")
    annotations = compress_json.load(OBJATHOR_ANNOTATIONS_PATH)
    print(f"数据库中共有 {len(annotations)} 个资产")
    print()

    # 检查每个资产
    missing_assets = []
    existing_assets = []

    print("检查资产文件存在性...")
    for asset_id in annotations.keys():
        asset_path = os.path.join(OBJATHOR_ASSETS_DIR, asset_id, f"{asset_id}.pkl.gz")
        if os.path.exists(asset_path):
            existing_assets.append(asset_id)
        else:
            missing_assets.append(asset_id)

    # 打印统计结果
    print()
    print("=" * 60)
    print("检查结果")
    print("=" * 60)
    print(
        f"✅ 存在的资产: {len(existing_assets)} ({len(existing_assets) / len(annotations) * 100:.1f}%)"
    )
    print(
        f"❌ 缺失的资产: {len(missing_assets)} ({len(missing_assets) / len(annotations) * 100:.1f}%)"
    )
    print()

    if missing_assets:
        print("缺失的资产 ID（前20个）:")
        for asset_id in missing_assets[:20]:
            print(f"  - {asset_id}")
        if len(missing_assets) > 20:
            print(f"  ... 还有 {len(missing_assets) - 20} 个")

        # 保存完整列表
        output_file = "missing_assets.txt"
        with open(output_file, "w") as f:
            for asset_id in missing_assets:
                f.write(f"{asset_id}\n")
        print()
        print(f"完整的缺失资产列表已保存到: {output_file}")

    print()
    print("=" * 60)
    print("建议")
    print("=" * 60)
    if len(missing_assets) > len(annotations) * 0.5:
        print("⚠️  缺失资产超过50%，可能需要重新下载资产数据库")
        print("   请检查资产下载是否完整")
    elif len(missing_assets) > 0:
        print("✅ 资产检索器已更新，会自动跳过缺失的资产")
        print("   这不会影响场景生成，系统会自动选择可用的替代资产")
    else:
        print("🎉 所有资产文件完整，无需任何操作")


if __name__ == "__main__":
    check_missing_assets()
