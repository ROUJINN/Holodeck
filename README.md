python -m ai2holodeck.main --query "a living room" --original_scene data/scenes/a_living_room-2026-01-28-11-01-43-099349/a_living_room.json
从已有场景中接着跑


让我查看代码中已有的渲染功能： 

完美！代码已经提供了渲染功能。我来创建一个简单的脚本方便你使用： 

现在你可以用以下命令渲染不同视角的图片：

## **1. 渲染顶视图**
```bash
python render_scene.py --scene /home/lj/3D/Holodeck/data/scenes/a_living_room-2026-01-28-11-08-49-655247/a_living_room.json --mode top_down_frame
```

## **2. 渲染房间多角度图片（推荐）**
每个房间4个角度（0°, 90°, 180°, 270°）：
```bash
python render_scene.py --scene /home/lj/3D/Holodeck/data/scenes/a_living_room-2026-01-28-11-08-49-655247/a_living_room.json --mode room_image
```

## **3. 渲染360度旋转视频**
```bash
python render_scene.py --scene /home/lj/3D/Holodeck/data/scenes/a_living_room-2026-01-28-11-08-49-655247/a_living_room.json --mode room_video
```

## **自定义分辨率**
```bash
python render_scene.py --scene /home/lj/3D/Holodeck/data/scenes/a_living_room-2026-01-28-11-08-49-655247/a_living_room.json --mode room_image --width 2048 --height 2048
```

## **或者直接使用原有的 utils.py**
```bash
cd /home/lj/3D/Holodeck
python -m ai2holodeck.generation.utils --scene data/scenes/a_living_room-2026-01-28-11-08-49-655247/a_living_room.json --mode room_image
```

所有生成的图片和视频会保存在场景的同一目录下。推荐使用 `room_image` 模式，可以得到多个角度的渲染图！

Made changes.