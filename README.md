This project uses a robotic arm and Turtlebot 3 to pick items from a virtual factory, place them on a conveyor belt, and then move them to a loading dock.

## 패키지 빌드
--------------------------------------------------------------------

```console
cd ~/b3_ws
colcon build
source install/setup.bash
```
## 실행하는 순서
--------------------------------------------------------------------

### 1. 서버 시작
```console
ros2 run manipulator_amr server
```
